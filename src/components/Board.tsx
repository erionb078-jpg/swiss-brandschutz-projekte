"use client";

import Link from "next/link";
import { useMemo, useState, useTransition, useEffect } from "react";
import {
  DndContext,
  PointerSensor,
  KeyboardSensor,
  useDraggable,
  useDroppable,
  useSensor,
  useSensors,
  type DragEndEvent,
} from "@dnd-kit/core";
import { STATUSES, SERVICES, type StatusKey } from "@/lib/types";
import { setStatus } from "@/app/actions";
import { initials } from "@/lib/format";
import { Icon } from "./Icon";

export type CardData = {
  id: string;
  title: string;
  status: StatusKey;
  sub: string;
  line: string;
  services: string[];
  amount: string | null;
  date: string;
  foot: string;
  owner: string | null;
  flag: { text: string; tone: "red" | "amber" | "green" | "blue" } | null;
};

const toneClass = {
  red: "bg-brand-soft text-brand-dark",
  amber: "bg-sand text-[#6B4A0C]",
  green: "bg-[#EDF3EE] text-[#2E5E3A]",
  blue: "bg-[#EEF1F6] text-[#2C4A78]",
};

export function Board({ cards: initial }: { cards: CardData[] }) {
  const [cards, setCards] = useState(initial);
  useEffect(() => setCards(initial), [initial]);
  const [q, setQ] = useState("");
  const [svc, setSvc] = useState<string | null>(null);
  const [showDone, setShowDone] = useState(false);
  const [, start] = useTransition();
  const sensors = useSensors(useSensor(PointerSensor, { activationConstraint: { distance: 6 } }), useSensor(KeyboardSensor));

  const visible = useMemo(() => {
    const s = q.trim().toLowerCase();
    return cards.filter(
      (c) =>
        (!svc || c.services.includes(svc)) &&
        (!s || [c.title, c.sub, c.line, c.owner ?? ""].join(" ").toLowerCase().includes(s))
    );
  }, [cards, q, svc]);

  const columns = STATUSES.filter((s) => showDone || s.key !== "absage");

  function onDragEnd(e: DragEndEvent) {
    const id = String(e.active.id);
    const to = e.over?.id as StatusKey | undefined;
    if (!to) return;
    const card = cards.find((c) => c.id === id);
    if (!card || card.status === to) return;
    setCards((cs) => cs.map((c) => (c.id === id ? { ...c, status: to } : c)));
    start(() => setStatus(id, to));
  }

  return (
    <div className="flex flex-col gap-4">
      <div className="flex flex-wrap items-center gap-2">
        <label className="relative">
          <span className="sr-only">Projekt suchen</span>
          <Icon name="search" size={16} className="pointer-events-none absolute left-3 top-1/2 -translate-y-1/2 text-muted" />
          <input
            type="search"
            value={q}
            onChange={(e) => setQ(e.target.value)}
            placeholder="Objekt, Kunde, Person suchen"
            className="field w-[280px] max-w-full pl-9"
          />
        </label>
        <div role="group" aria-label="Filter Leistung" className="flex flex-wrap gap-2">
          {[null, ...SERVICES.filter((s) => s !== "Sonstiges")].map((s) => (
            <button
              key={s ?? "alle"}
              type="button"
              aria-pressed={svc === s}
              onClick={() => setSvc(s)}
              className={`h-9 rounded-full border px-3.5 text-[13px] ${svc === s ? "border-night bg-night font-semibold text-white" : "border-line-2 bg-white hover:border-night"}`}
            >
              {s ?? "Alle"}
            </button>
          ))}
        </div>
        <label className="ml-auto flex items-center gap-2 text-[13px] text-muted">
          <input type="checkbox" checked={showDone} onChange={(e) => setShowDone(e.target.checked)} className="h-4 w-4 accent-brand" />
          Absagen zeigen
        </label>
      </div>

      <DndContext sensors={sensors} onDragEnd={onDragEnd}>
        <div className="overflow-x-auto pb-2">
          <div className="flex min-w-max items-start gap-4">
            {columns.map((col) => {
              const list = visible.filter((c) => c.status === col.key);
              return (
                <Column key={col.key} id={col.key} label={col.label} count={list.length}>
                  {list.map((c) => (
                    <Card key={c.id} c={c} />
                  ))}
                  {list.length === 0 && (
                    <div className="rounded-[10px] border-[1.5px] border-dashed border-[#D2CDC4] px-3.5 py-5 text-center text-[13px] text-muted">
                      Karte hierher ziehen
                    </div>
                  )}
                </Column>
              );
            })}
          </div>
        </div>
      </DndContext>
    </div>
  );
}

function Column({ id, label, count, children }: { id: string; label: string; count: number; children: React.ReactNode }) {
  const { setNodeRef, isOver } = useDroppable({ id });
  return (
    <section
      ref={setNodeRef}
      aria-label={label}
      className={`flex w-[272px] flex-col gap-2.5 rounded-xl p-1 transition-colors ${isOver ? "bg-[#ECE8E1]" : ""}`}
    >
      <div className="flex items-center justify-between px-1 pb-1 text-xs font-semibold uppercase tracking-[.06em] text-[#4a4843]">
        <span>{label}</span>
        <span className="text-[#8a877f]">{count}</span>
      </div>
      {children}
    </section>
  );
}

function Card({ c }: { c: CardData }) {
  const { attributes, listeners, setNodeRef, transform, isDragging } = useDraggable({ id: c.id });
  const style = transform ? { transform: `translate3d(${transform.x}px, ${transform.y}px, 0)` } : undefined;
  return (
    <Link
      ref={setNodeRef}
      href={`/projekte/${c.id}`}
      style={style}
      {...listeners}
      {...attributes}
      className={`flex flex-col gap-2 rounded-[10px] border bg-white px-3.5 pb-3 pt-3.5 hover:border-night ${isDragging ? "z-10 border-night shadow-lg" : "border-line"}`}
    >
      <div className="flex items-center justify-between gap-2">
        {c.flag ? (
          <span className={`truncate rounded-full px-2 py-0.5 text-[11.5px] font-semibold ${toneClass[c.flag.tone]}`}>{c.flag.text}</span>
        ) : (
          <span />
        )}
        <span className="shrink-0 text-xs text-muted">{c.date}</span>
      </div>
      <div className="text-[15px] font-semibold leading-snug">{c.title}</div>
      {c.sub && <div className="text-[13px] text-muted">{c.sub}</div>}
      {c.line && <div className="text-[13px]">{c.line}</div>}
      <div className="flex items-center justify-between border-t border-[#EEEBE5] pt-2 text-[13px]">
        {c.amount ? <span className="font-semibold tabular-nums">{c.amount}</span> : <span className="text-[12.5px] text-muted">{c.foot}</span>}
        <span className="flex items-center gap-2">
          {c.amount && c.foot && <span className="text-xs text-muted">{c.foot}</span>}
          <span className="flex h-6 w-6 items-center justify-center rounded-full bg-[#E9E5DE] text-[10px] font-semibold" title={c.owner ?? undefined}>
            {initials(c.owner)}
          </span>
        </span>
      </div>
    </Link>
  );
}
