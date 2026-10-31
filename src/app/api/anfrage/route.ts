import { NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase/admin";

/**
 * Eingang für Anfragen von swiss-brandschutz.ch.
 * POST JSON: { name, firma, telefon, email, ort, nachricht, objekt? }
 * Header: x-anfrage-secret: <ANFRAGE_SECRET>
 */
export async function POST(req: Request) {
  if (!process.env.ANFRAGE_SECRET || req.headers.get("x-anfrage-secret") !== process.env.ANFRAGE_SECRET) {
    return NextResponse.json({ ok: false }, { status: 401 });
  }
  let b: Record<string, unknown>;
  try {
    b = await req.json();
  } catch {
    return NextResponse.json({ ok: false, error: "invalid json" }, { status: 400 });
  }
  const s = (k: string) => (typeof b[k] === "string" && (b[k] as string).trim() ? (b[k] as string).trim().slice(0, 2000) : null);

  const supabase = createAdminClient();
  const firma = s("firma");
  const ort = s("ort");
  const title = s("objekt") ?? [firma ?? s("name") ?? "Website-Anfrage", ort].filter(Boolean).join(", ");

  const { data: p, error } = await supabase
    .from("projects")
    .insert({ title, location: ort, client_company: firma, description: s("nachricht"), status: "anfrage", source: "Website", owner: "Fadil Fazliu" })
    .select("id")
    .single();
  if (error || !p) return NextResponse.json({ ok: false }, { status: 500 });

  if (s("name")) {
    await supabase.from("contacts").insert({ project_id: p.id, name: s("name"), company: firma, role: "Anfragender", phone: s("telefon"), email: s("email"), address: ort });
  }
  const tomorrow = new Date(Date.now() + 864e5).toLocaleDateString("sv-SE", { timeZone: "Europe/Zurich" });
  await supabase.from("tasks").insert({ project_id: p.id, title: `${s("name") ?? "Kunde"} kontaktieren, Unterlagen und Details klären`, due: tomorrow });
  await supabase.from("events").insert({ project_id: p.id, text: "Anfrage über Website eingegangen" });

  return NextResponse.json({ ok: true, id: p.id });
}
