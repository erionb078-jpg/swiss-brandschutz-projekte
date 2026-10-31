import Link from "next/link";
import { createClient } from "@/lib/supabase/server";
import { initials } from "@/lib/format";

export const dynamic = "force-dynamic";

type Row = { id: string; name: string; company: string | null; role: string | null; phone: string | null; email: string | null; project_id: string | null; projects: { title: string } | null };

export default async function ContactsPage() {
  const supabase = await createClient();
  const { data } = await supabase.from("contacts").select("id, name, company, role, phone, email, project_id, projects(title)").order("name");
  const rows = (data ?? []) as unknown as Row[];
  // gleiche Person bei mehreren Projekten zusammenfassen
  const people = new Map<string, Row & { projects_list: { id: string; title: string }[] }>();
  for (const r of rows) {
    const key = (r.email || r.name).toLowerCase();
    const cur = people.get(key) ?? { ...r, projects_list: [] };
    cur.phone ??= r.phone;
    cur.email ??= r.email;
    if (r.project_id && r.projects) cur.projects_list.push({ id: r.project_id, title: r.projects.title });
    people.set(key, cur);
  }

  return (
    <div className="mx-auto flex max-w-[1100px] flex-col gap-5">
      <h1 className="font-display text-[30px] font-extrabold tracking-tight">Kontakte</h1>
      <div className="grid gap-4 [grid-template-columns:repeat(auto-fill,minmax(min(100%,300px),1fr))]">
        {[...people.values()].map((c) => (
          <article key={c.id} className="panel gap-3">
            <div className="flex items-center gap-3">
              <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-full bg-night text-sm font-semibold text-white">{initials(c.name)}</div>
              <div className="min-w-0 leading-tight">
                <div className="font-semibold">{c.name}</div>
                <div className="muted truncate">{[c.role, c.company].filter(Boolean).join(" · ")}</div>
              </div>
            </div>
            <div className="text-sm leading-relaxed">
              {c.phone ? <a href={`tel:${c.phone.replace(/\s/g, "")}`} className="block tabular-nums hover:text-brand-dark">{c.phone}</a> : <span className="block text-muted">Telefon fehlt</span>}
              {c.email ? <a href={`mailto:${c.email}`} className="block break-all hover:text-brand-dark">{c.email}</a> : <span className="block text-muted">E-Mail fehlt</span>}
            </div>
            <div className="flex flex-wrap gap-1.5">
              {c.projects_list.map((p) => (
                <Link key={p.id} href={`/projekte/${p.id}`} className="rounded-full bg-sand px-2.5 py-1 text-xs font-medium hover:bg-[#ECE5D8]">{p.title}</Link>
              ))}
            </div>
          </article>
        ))}
      </div>
    </div>
  );
}
