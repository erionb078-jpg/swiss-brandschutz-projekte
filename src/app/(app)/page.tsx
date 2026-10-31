"use client";

import Link from "next/link";
import { Board, type CardData } from "@/components/Board";
import { Icon } from "@/components/Icon";
import { ErrorBox, Loading } from "@/components/Ui";
import { loadBoard, useLoad } from "@/lib/db";
import { chf, dmy, addDays, today, shortName } from "@/lib/format";

type Tone = "red" | "amber" | "green" | "blue";

export default function BoardPage() {
  const { data, error, reload } = useLoad(loadBoard);
  if (error) return <ErrorBox error={error} />;
  if (!data) return <Loading />;

  const { projects: ps, contacts, tasks } = data;
  const t = today();
  const soon = addDays(t, 3);
  const byId = new Map(ps.map((p) => [p.id, p]));

  const cards: CardData[] = ps.map((p) => {
    const c = contacts.find((x) => x.project_id === p.id);
    const open = tasks.filter((x) => x.project_id === p.id);
    const overdue = open.find((x) => x.due && x.due <= t);
    let flag: { text: string; tone: Tone } | null = null;
    if (p.status === "versendet" && p.follow_up && p.follow_up <= t) flag = { text: "Nachfassen fällig", tone: "red" };
    else if (overdue) flag = { text: p.status === "anfrage" ? "Rückmeldung fällig" : "Fällig: " + cut(overdue.title), tone: "red" };
    else if (p.status === "versendet" && p.follow_up) flag = { text: `Nachfassen ${dmy(p.follow_up)}`, tone: "amber" };
    else if (open[0]) flag = { text: cut(open[0].title), tone: "amber" };
    else if (p.status === "offerte") flag = { text: "Bereit zum Versand", tone: "green" };
    return {
      id: p.id,
      title: p.title,
      status: p.status,
      sub: [p.client_company, shortName(c?.name)].filter(Boolean).join(" · "),
      line: p.description ? firstSentence(p.description) : p.services.join(", "),
      services: p.services,
      amount: chf(p.amount_net),
      date: dmy(p.offer_date ?? p.created_at),
      foot: p.amount_net == null ? (p.offer_ref ? `Nr. ${p.offer_ref}` : p.source ?? "") : p.valid_until ? `gültig bis ${dmy(p.valid_until)}` : "",
      owner: p.owner,
      flag,
    };
  });

  const active = ps.filter((p) => !["auftrag", "absage"].includes(p.status));
  const offered = active.filter((p) => ["offerte", "versendet"].includes(p.status)).reduce((s, p) => s + Number(p.amount_net ?? 0), 0);

  const todo: { id: string; text: string; tone: "red" | "amber" }[] = [];
  for (const p of ps) {
    if (p.status === "versendet" && p.follow_up && p.follow_up <= t) todo.push({ id: p.id, text: `${p.title}: nachfassen`, tone: "red" });
  }
  for (const x of tasks) {
    const p = byId.get(x.project_id);
    if (!p || p.status === "absage") continue;
    if (x.due && x.due <= t) todo.push({ id: p.id, text: `${short(p.title)}: ${cut(x.title, 46)} · seit ${dmy(x.due)}`, tone: "red" });
  }
  for (const x of tasks) {
    const p = byId.get(x.project_id);
    if (!p || p.status === "absage" || todo.length >= 4) continue;
    if ((x.due && x.due > t && x.due <= soon) || !x.due) todo.push({ id: p.id, text: `${short(p.title)}: ${cut(x.title, 46)}`, tone: "amber" });
  }

  return (
    <div className="flex flex-col gap-5">
      <header className="flex flex-wrap items-center gap-x-4 gap-y-3">
        <h1 className="font-display text-[30px] font-extrabold tracking-tight">Projekte</h1>
        <span className="text-sm text-muted">
          {active.length} aktiv · {chf(offered)} offeriert
        </span>
        <Link href="/neu/" className="btn-primary ml-auto">
          <Icon name="plus" size={16} /> Neue Anfrage
        </Link>
      </header>

      {todo.length > 0 && (
        <section aria-label="Heute zu tun" className="flex flex-wrap items-center gap-2.5 rounded-[10px] border border-line bg-white px-4 py-3.5">
          <span className="mr-1.5 font-display text-[15px] font-extrabold">Heute</span>
          {todo.slice(0, 5).map((x, i) => (
            <Link
              key={i}
              href={`/projekt/?id=${x.id}`}
              className={`inline-flex items-center gap-2 rounded-lg px-3 py-2 text-[13.5px] font-medium ${x.tone === "red" ? "bg-brand-soft text-brand-dark" : "bg-sand"}`}
            >
              <span className={`h-[7px] w-[7px] rounded-full ${x.tone === "red" ? "bg-brand" : "bg-[#9A6A12]"}`} />
              {x.text}
            </Link>
          ))}
        </section>
      )}

      <Board cards={cards} onChanged={reload} />
    </div>
  );
}

function cut(s: string, n = 30) {
  return s.length > n ? s.slice(0, n - 1).trimEnd() + "…" : s;
}
function short(s: string) {
  return s.split(/[,·]/)[0].trim();
}
function firstSentence(s: string) {
  const one = s.split(/(?<=\.)\s/)[0];
  return cut(one.replace(/\.$/, ""), 60);
}
