import Link from "next/link";
import { createClient } from "@/lib/supabase/server";
import { TaskItem } from "@/components/ProjectBits";
import { dmy, today, addDays } from "@/lib/format";

export const dynamic = "force-dynamic";

type Row = { id: string; project_id: string; title: string; due: string | null; done: boolean; projects: { title: string } | null };

export default async function TasksPage() {
  const supabase = await createClient();
  const { data } = await supabase
    .from("tasks")
    .select("id, project_id, title, due, done, projects(title)")
    .eq("done", false)
    .order("due", { ascending: true, nullsFirst: false });
  const rows = (data ?? []) as unknown as Row[];
  const t = today();
  const week = addDays(t, 7);
  const groups = [
    { label: "Überfällig und heute", items: rows.filter((r) => r.due && r.due <= t) },
    { label: "Nächste 7 Tage", items: rows.filter((r) => r.due && r.due > t && r.due <= week) },
    { label: "Später", items: rows.filter((r) => r.due && r.due > week) },
    { label: "Ohne Datum", items: rows.filter((r) => !r.due) },
  ];

  return (
    <div className="mx-auto flex max-w-[860px] flex-col gap-5">
      <h1 className="font-display text-[30px] font-extrabold tracking-tight">Aufgaben</h1>
      {rows.length === 0 && <p className="text-muted">Alles erledigt.</p>}
      {groups.filter((g) => g.items.length).map((g) => (
        <section key={g.label} className="panel">
          <h2 className="font-display text-[17px] font-extrabold">{g.label}</h2>
          <div className="flex flex-col gap-3">
            {g.items.map((r) => (
              <div key={r.id} className="flex flex-col gap-0.5">
                <Link href={`/projekte/${r.project_id}`} className="text-xs font-semibold text-muted hover:text-brand-dark">{r.projects?.title}</Link>
                <TaskItem id={r.id} projectId={r.project_id} title={r.title} due={dmy(r.due)} done={r.done} overdue={!!r.due && r.due <= t} />
              </div>
            ))}
          </div>
        </section>
      ))}
    </div>
  );
}
