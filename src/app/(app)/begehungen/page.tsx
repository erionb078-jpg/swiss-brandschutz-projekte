"use client";

import Link from "next/link";
import { ErrorBox, Loading } from "@/components/Ui";
import { loadVisits, useLoad, type VisitRow } from "@/lib/db";
import { dmy, today } from "@/lib/format";

function List({ items }: { items: VisitRow[] }) {
  return (
    <div className="flex flex-col">
      {items.map((r) => (
        <Link key={r.id} href={`/projekt/?id=${r.project_id}`} className="flex gap-4 border-b border-[#EEEBE5] py-3 last:border-0 hover:bg-[#FBFAF8]">
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
}

export default function VisitsPage() {
  const { data: rows, error } = useLoad(loadVisits);
  if (error) return <ErrorBox error={error} />;
  if (!rows) return <Loading />;
  const t = today();
  const upcoming = rows.filter((r) => !r.date || r.date >= t).reverse();
  const past = rows.filter((r) => r.date && r.date < t);

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
