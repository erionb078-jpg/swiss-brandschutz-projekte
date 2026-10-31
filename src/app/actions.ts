"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";
import { STATUSES, type StatusKey } from "@/lib/types";
import { addDays, chf, today } from "@/lib/format";

const str = (fd: FormData, k: string) => {
  const v = fd.get(k);
  const s = typeof v === "string" ? v.trim() : "";
  return s === "" ? null : s;
};
const num = (fd: FormData, k: string) => {
  const s = str(fd, k);
  if (s == null) return null;
  const n = Number(s.replace(/['’\s]/g, "").replace(",", "."));
  return Number.isFinite(n) ? n : null;
};
const statusLabel = (s: string) => STATUSES.find((x) => x.key === s)?.label ?? s;

function refresh(projectId?: string) {
  revalidatePath("/", "layout");
  if (projectId) revalidatePath(`/projekte/${projectId}`);
}

// ---------- Anmeldung ----------

export async function login(_prev: string | null, fd: FormData): Promise<string | null> {
  const supabase = await createClient();
  const { error } = await supabase.auth.signInWithPassword({
    email: String(fd.get("email") ?? ""),
    password: String(fd.get("password") ?? ""),
  });
  if (error) return "E-Mail oder Passwort stimmt nicht.";
  redirect("/");
}

export async function logout() {
  const supabase = await createClient();
  await supabase.auth.signOut();
  redirect("/login");
}

// ---------- Projekte ----------

export async function setStatus(projectId: string, status: StatusKey) {
  const supabase = await createClient();
  const { data: p } = await supabase.from("projects").select("status, follow_up, offer_date").eq("id", projectId).single();
  if (!p || p.status === status) return;
  const patch: Record<string, unknown> = { status };
  if (status === "versendet") {
    if (!p.follow_up) patch.follow_up = addDays(today(), 7);
    if (!p.offer_date) patch.offer_date = today();
  }
  await supabase.from("projects").update(patch).eq("id", projectId);
  const extra = status === "versendet" && patch.follow_up ? `, nachfassen am ${String(patch.follow_up).split("-").reverse().join(".")}` : "";
  await supabase.from("events").insert({ project_id: projectId, text: `Status: ${statusLabel(status)}${extra}` });
  refresh(projectId);
}

export async function createProject(fd: FormData) {
  const supabase = await createClient();
  const services = fd.getAll("services").map(String);
  const title = str(fd, "title") ?? "Neue Anfrage";
  const { data: p, error } = await supabase
    .from("projects")
    .insert({
      title,
      location: str(fd, "location"),
      client_company: str(fd, "company"),
      services,
      description: str(fd, "description"),
      status: "anfrage",
      source: str(fd, "source"),
      owner: str(fd, "owner"),
    })
    .select("id")
    .single();
  if (error || !p) throw new Error(error?.message ?? "Projekt konnte nicht angelegt werden");

  const name = str(fd, "person");
  if (name) {
    await supabase.from("contacts").insert({
      project_id: p.id,
      name,
      company: str(fd, "company"),
      role: "Anfragender",
      phone: str(fd, "phone"),
      email: str(fd, "email"),
      address: str(fd, "location"),
    });
  }
  const due = str(fd, "due");
  await supabase.from("tasks").insert({
    project_id: p.id,
    title: name ? `${name} kontaktieren, Unterlagen und Details klären` : "Kunde kontaktieren, Details klären",
    due,
  });
  const visit = str(fd, "visit");
  if (visit) {
    await supabase.from("visits").insert({ project_id: p.id, date: visit, title: "Begehung vor Ort", participants: str(fd, "owner") });
  }
  await supabase.from("events").insert({ project_id: p.id, text: `Anfrage erfasst${str(fd, "source") ? ` (${str(fd, "source")})` : ""}` });
  refresh();
  redirect(`/projekte/${p.id}`);
}

export async function updateProject(projectId: string, fd: FormData) {
  const supabase = await createClient();
  const amount = num(fd, "amount_net");
  const { data: before } = await supabase.from("projects").select("amount_net").eq("id", projectId).single();
  await supabase
    .from("projects")
    .update({
      title: str(fd, "title") ?? "Ohne Titel",
      location: str(fd, "location"),
      client_company: str(fd, "client_company"),
      services: fd.getAll("services").map(String),
      description: str(fd, "description"),
      amount_net: amount,
      offer_ref: str(fd, "offer_ref"),
      offer_date: str(fd, "offer_date"),
      valid_until: str(fd, "valid_until"),
      follow_up: str(fd, "follow_up"),
      owner: str(fd, "owner"),
      source: str(fd, "source"),
    })
    .eq("id", projectId);
  if (amount != null && Number(before?.amount_net ?? NaN) !== amount) {
    await supabase.from("events").insert({ project_id: projectId, text: `Offertbetrag ${chf(amount)} netto` });
  }
  refresh(projectId);
  redirect(`/projekte/${projectId}`);
}

export async function deleteProject(projectId: string) {
  const supabase = await createClient();
  await supabase.from("projects").delete().eq("id", projectId);
  refresh();
  redirect("/");
}

// ---------- Teile eines Projekts ----------

export async function addTask(projectId: string, fd: FormData) {
  const title = str(fd, "title");
  if (!title) return;
  const supabase = await createClient();
  await supabase.from("tasks").insert({ project_id: projectId, title, due: str(fd, "due") });
  refresh(projectId);
}

export async function toggleTask(taskId: string, projectId: string, done: boolean) {
  const supabase = await createClient();
  const { data: t } = await supabase.from("tasks").update({ done }).eq("id", taskId).select("title").single();
  if (done && t) await supabase.from("events").insert({ project_id: projectId, text: `Erledigt: ${t.title}` });
  refresh(projectId);
}

export async function deleteTask(taskId: string, projectId: string) {
  const supabase = await createClient();
  await supabase.from("tasks").delete().eq("id", taskId);
  refresh(projectId);
}

export async function addVisit(projectId: string, fd: FormData) {
  const supabase = await createClient();
  await supabase.from("visits").insert({
    project_id: projectId,
    date: str(fd, "date"),
    title: str(fd, "title") ?? "Begehung vor Ort",
    participants: str(fd, "participants"),
    notes: str(fd, "notes"),
  });
  refresh(projectId);
}

export async function updateVisit(visitId: string, projectId: string, fd: FormData) {
  const supabase = await createClient();
  await supabase
    .from("visits")
    .update({ date: str(fd, "date"), title: str(fd, "title") ?? "Begehung vor Ort", participants: str(fd, "participants"), notes: str(fd, "notes") })
    .eq("id", visitId);
  refresh(projectId);
}

export async function addContact(projectId: string, fd: FormData) {
  const name = str(fd, "name");
  if (!name) return;
  const supabase = await createClient();
  await supabase.from("contacts").insert({
    project_id: projectId,
    name,
    company: str(fd, "company"),
    role: str(fd, "role"),
    phone: str(fd, "phone"),
    email: str(fd, "email"),
    address: str(fd, "address"),
  });
  refresh(projectId);
}

export async function updateContact(contactId: string, projectId: string, fd: FormData) {
  const supabase = await createClient();
  await supabase
    .from("contacts")
    .update({
      name: str(fd, "name") ?? "Ohne Name",
      company: str(fd, "company"),
      role: str(fd, "role"),
      phone: str(fd, "phone"),
      email: str(fd, "email"),
      address: str(fd, "address"),
    })
    .eq("id", contactId);
  refresh(projectId);
}

export async function addDocument(projectId: string, fd: FormData) {
  const name = str(fd, "name");
  const url = str(fd, "url");
  if (!name || !url) return;
  const supabase = await createClient();
  await supabase.from("documents").insert({ project_id: projectId, name, url, date: str(fd, "date") ?? today() });
  refresh(projectId);
}

export async function deleteDocument(docId: string, projectId: string) {
  const supabase = await createClient();
  await supabase.from("documents").delete().eq("id", docId);
  refresh(projectId);
}

export async function addNote(projectId: string, fd: FormData) {
  const text = str(fd, "text");
  if (!text) return;
  const supabase = await createClient();
  await supabase.from("events").insert({ project_id: projectId, text });
  refresh(projectId);
}
