import Link from "next/link";
import { createClient } from "@/lib/supabase/server";
import { dmy, today } from "@/lib/format";

export const dynamic = "force-dynamic";

type Row = { id: string; date: string | null; title: string; participants: string | null; notes: string | null; project_id: string; projects: { title: string } | null };

export default async function VisitsPage() {
  const supabase = await createClient();
  const { data } = await supabase.from("visits").select("id, date, title, participants, notes, project_id, projects(title)").order("date", { ascending: false, nullsFirst: true });
  const rows = (data ?? []) as unknown as Row[];
  const t = today();
  const upcoming = rows.filter((r) => !r.date || r.date >= t).reverse();
  const past = rows.filter((r) => r.date && r.date < t);

  const List = ({ items }: { items: Row[] }) => (
    <div className="flex flex-col">
      {items.map((r) => (
        <Link key={r.id} href={`/projekte/${r.project_id}`} className="flex gap-4 border-b border-[#EEEBE5] py-3 last:border-0 hover:bg-[#FBFAF8]">
          <span className="w-[86px] shrink-0 text-sm font-semibold tabular-nums">{r.date ? dmy(r.date, true) : "offen"}</span>
          <span className="min-w-0 text-sm">
            <span className="font-semibold">{r.projects?.title}</span> · {r.title}
            {r.participants && <span className="block text-xs text-muted">{r.participants}</span>}
            {r.notes && <span className="mt-1 block text-[13.5px] text-[#4a4843]">{r.notes}</span>}
          </span>
        </Link>
      ))}
    </div>
  );

  return (
    <div className="mx-auto flex max-w-[860px] flex-col gap-5">
      <h1 className="font-display text-[30px] font-extrabold tracking-tight">Begehungen</h1>
      <section className="panel">
        <h2 className="font-display text-[17px] font-extrabold">Geplant</h2>
        {upcoming.length ? <List items={upcoming} /> : <p className="text-sm text-muted">Keine geplanten Begehungen. Neue Termine trägst du direkt im Projekt ein.</p>}
      </section>
      <section className="panel">
        <h2 className="font-display text-[17px] font-extrabold">Durchgeführt</h2>
        <List items={past} />
      </section>
    </div>
  );
}
