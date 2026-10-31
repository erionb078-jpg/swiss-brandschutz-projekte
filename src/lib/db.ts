"use client";

import { useCallback, useEffect, useState } from "react";
import { sb } from "./supabase";
import { STATUSES, type Contact, type Doc, type Event, type Project, type StatusKey, type Task, type Visit } from "./types";
import { addDays, chf, today } from "./format";

const statusLabel = (s: string) => STATUSES.find((x) => x.key === s)?.label ?? s;

export const str = (fd: FormData, k: string) => {
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

function must<T>(r: { data: T; error: { message: string } | null }): T {
  if (r.error) throw new Error(r.error.message);
  return r.data;
}

/** Lädt Daten und gibt [daten, fehler, neu laden] zurück. */
export function useLoad<T>(fn: () => Promise<T>, deps: unknown[] = []) {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<string | null>(null);
  // eslint-disable-next-line react-hooks/exhaustive-deps
  const load = useCallback(() => fn().then(setData).catch((e) => setError(String(e?.message ?? e))), deps);
  useEffect(() => {
    load();
  }, [load]);
  return { data, error, reload: load };
}

// ---------- Lesen ----------

export async function loadBoard() {
  const s = sb();
  const [p, c, t] = await Promise.all([
    s.from("projects").select("*").order("position").order("created_at", { ascending: false }),
    s.from("contacts").select("id, project_id, name, company").order("created_at"),
    s.from("tasks").select("id, project_id, title, due, done").eq("done", false).order("due", { ascending: true, nullsFirst: false }),
  ]);
  return { projects: must(p) as Project[], contacts: must(c) as Contact[], tasks: must(t) as Task[] };
}

export async function loadProject(id: string) {
  const s = sb();
  const [p, c, v, t, d, e] = await Promise.all([
    s.from("projects").select("*").eq("id", id).maybeSingle(),
    s.from("contacts").select("*").eq("project_id", id).order("created_at"),
    s.from("visits").select("*").eq("project_id", id).order("date", { ascending: false, nullsFirst: false }),
    s.from("tasks").select("*").eq("project_id", id).order("done").order("due", { ascending: true, nullsFirst: false }),
    s.from("documents").select("*").eq("project_id", id).order("date", { ascending: false }),
    s.from("events").select("*").eq("project_id", id).order("date", { ascending: false }).order("created_at", { ascending: false }),
  ]);
  return {
    project: must(p) as Project | null,
    contacts: must(c) as Contact[],
    visits: must(v) as Visit[],
    tasks: must(t) as Task[],
    docs: must(d) as Doc[],
    events: must(e) as Event[],
  };
}

export async function openTaskCount() {
  const { count } = await sb().from("tasks").select("id", { count: "exact", head: true }).eq("done", false).lte("due", today());
  return count ?? 0;
}

export type TaskRow = Task & { projects: { title: string } | null };
export async function loadTasks() {
  return must(await sb().from("tasks").select("id, project_id, title, due, done, projects(title)").eq("done", false).order("due", { ascending: true, nullsFirst: false })) as unknown as TaskRow[];
}

export type ContactRow = Contact & { projects: { title: string } | null };
export async function loadContacts() {
  return must(await sb().from("contacts").select("id, name, company, role, phone, email, address, project_id, projects(title)").order("name")) as unknown as ContactRow[];
}

export type VisitRow = Visit & { projects: { title: string } | null };
export async function loadVisits() {
  return must(await sb().from("visits").select("id, date, title, participants, notes, project_id, projects(title)").order("date", { ascending: false, nullsFirst: true })) as unknown as VisitRow[];
}

// ---------- Schreiben ----------

export async function setStatus(projectId: string, status: StatusKey) {
  const s = sb();
  const p = must(await s.from("projects").select("status, follow_up, offer_date").eq("id", projectId).single()) as Pick<Project, "status" | "follow_up" | "offer_date">;
  if (p.status === status) return;
  const patch: Record<string, unknown> = { status };
  if (status === "versendet") {
    if (!p.follow_up) patch.follow_up = addDays(today(), 7);
    if (!p.offer_date) patch.offer_date = today();
  }
  must(await s.from("projects").update(patch).eq("id", projectId));
  const extra = status === "versendet" && patch.follow_up ? `, nachfassen am ${String(patch.follow_up).split("-").reverse().join(".")}` : "";
  await s.from("events").insert({ project_id: projectId, text: `Status: ${statusLabel(status)}${extra}` });
}

export async function createProject(fd: FormData): Promise<string> {
  const s = sb();
  const p = must(
    await s
      .from("projects")
      .insert({
        title: str(fd, "title") ?? "Neue Anfrage",
        location: str(fd, "location"),
        client_company: str(fd, "company"),
        services: fd.getAll("services").map(String),
        description: str(fd, "description"),
        status: "anfrage",
        source: str(fd, "source"),
        owner: str(fd, "owner"),
      })
      .select("id")
      .single()
  ) as { id: string };

  const name = str(fd, "person");
  if (name) {
    await s.from("contacts").insert({ project_id: p.id, name, company: str(fd, "company"), role: "Anfragender", phone: str(fd, "phone"), email: str(fd, "email"), address: str(fd, "location") });
  }
  await s.from("tasks").insert({
    project_id: p.id,
    title: name ? `${name} kontaktieren, Unterlagen und Details klären` : "Kunde kontaktieren, Details klären",
    due: str(fd, "due"),
  });
  const visit = str(fd, "visit");
  if (visit) await s.from("visits").insert({ project_id: p.id, date: visit, title: "Begehung vor Ort", participants: str(fd, "owner") });
  await s.from("events").insert({ project_id: p.id, text: `Anfrage erfasst${str(fd, "source") ? ` (${str(fd, "source")})` : ""}` });
  return p.id;
}

export async function updateProject(projectId: string, fd: FormData) {
  const s = sb();
  const amount = num(fd, "amount_net");
  const before = must(await s.from("projects").select("amount_net").eq("id", projectId).single()) as { amount_net: number | null };
  must(
    await s
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
      .eq("id", projectId)
  );
  if (amount != null && Number(before.amount_net ?? NaN) !== amount) {
    await s.from("events").insert({ project_id: projectId, text: `Offertbetrag ${chf(amount)} netto` });
  }
}

export async function deleteProject(projectId: string) {
  must(await sb().from("projects").delete().eq("id", projectId));
}

export async function addTask(projectId: string, fd: FormData) {
  const title = str(fd, "title");
  if (!title) return;
  must(await sb().from("tasks").insert({ project_id: projectId, title, due: str(fd, "due") }));
}

export async function toggleTask(taskId: string, projectId: string, done: boolean) {
  const s = sb();
  const t = must(await s.from("tasks").update({ done }).eq("id", taskId).select("title").single()) as { title: string };
  if (done) await s.from("events").insert({ project_id: projectId, text: `Erledigt: ${t.title}` });
}

export async function deleteTask(taskId: string) {
  must(await sb().from("tasks").delete().eq("id", taskId));
}

export async function addVisit(projectId: string, fd: FormData) {
  must(
    await sb().from("visits").insert({
      project_id: projectId,
      date: str(fd, "date"),
      title: str(fd, "title") ?? "Begehung vor Ort",
      participants: str(fd, "participants"),
      notes: str(fd, "notes"),
    })
  );
}

const contactFields = (fd: FormData) => ({
  name: str(fd, "name") ?? "Ohne Name",
  company: str(fd, "company"),
  role: str(fd, "role"),
  phone: str(fd, "phone"),
  email: str(fd, "email"),
  address: str(fd, "address"),
});

export async function addContact(projectId: string, fd: FormData) {
  if (!str(fd, "name")) return;
  must(await sb().from("contacts").insert({ project_id: projectId, ...contactFields(fd) }));
}

export async function updateContact(contactId: string, fd: FormData) {
  must(await sb().from("contacts").update(contactFields(fd)).eq("id", contactId));
}

export async function addDocument(projectId: string, fd: FormData) {
  const name = str(fd, "name");
  const url = str(fd, "url");
  if (!name || !url) return;
  must(await sb().from("documents").insert({ project_id: projectId, name, url, date: str(fd, "date") ?? today() }));
}

export async function deleteDocument(docId: string) {
  must(await sb().from("documents").delete().eq("id", docId));
}

export async function addNote(projectId: string, fd: FormData) {
  const text = str(fd, "text");
  if (!text) return;
  must(await sb().from("events").insert({ project_id: projectId, text }));
}
