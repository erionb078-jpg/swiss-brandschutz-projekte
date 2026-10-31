"use client";

import { useOptimistic, useTransition } from "react";
import { STEPS, type StatusKey } from "@/lib/types";
import { setStatus, toggleTask, deleteTask } from "@/lib/db";
import { Icon } from "./Icon";

export function StatusSteps({ projectId, status, dates, onChange }: { projectId: string; status: StatusKey; dates: Partial<Record<StatusKey, string>>; onChange: () => unknown }) {
  const [opt, setOpt] = useOptimistic(status);
  const [pending, start] = useTransition();
  const idx = STEPS.findIndex((s) => s.key === opt);
  const lost = opt === "absage";

  const go = (k: StatusKey) =>
    start(async () => {
      setOpt(k);
      await setStatus(projectId, k);
      await onChange();
    });

  return (
    <div className="flex flex-col gap-3">
      <ol aria-label="Projektstatus" className={`grid grid-cols-5 gap-1.5 ${pending ? "opacity-70" : ""}`}>
        {STEPS.map((s, i) => {
          const done = !lost && i < idx;
          const cur = !lost && i === idx;
          return (
            <li key={s.key}>
              <button
                type="button"
                onClick={() => go(s.key)}
                aria-current={cur ? "step" : undefined}
                className="flex w-full flex-col gap-2 rounded-md text-left focus-visible:outline-2 focus-visible:outline-night"
                title={`Status auf «${s.label}» setzen`}
              >
                <span className={`h-1.5 rounded-full ${cur ? "bg-brand" : done ? "bg-night" : "bg-[#DDD8D0]"}`} />
                <span className={`text-[13px] ${cur ? "font-semibold text-brand-dark" : done ? "font-semibold" : "text-muted"}`}>{s.label}</span>
                <span className="text-xs text-muted">{dates[s.key] ?? "—"}</span>
              </button>
            </li>
          );
        })}
      </ol>
      <div className="flex flex-wrap items-center gap-2 text-[13px]">
        {lost ? (
          <>
            <span className="rounded-full bg-[#E9E5DE] px-2.5 py-0.5 font-semibold">Absage</span>
            <button type="button" onClick={() => go("anfrage")} className="text-muted underline">Wieder öffnen</button>
          </>
        ) : (
          <button type="button" onClick={() => go("absage")} className="text-muted underline hover:text-ink">
            Als Absage markieren
          </button>
        )}
      </div>
    </div>
  );
}

export function TaskItem({ id, projectId, title, due, done, overdue, onChange }: { id: string; projectId: string; title: string; due: string; done: boolean; overdue: boolean; onChange: () => unknown }) {
  const [opt, setOpt] = useOptimistic(done);
  const [, start] = useTransition();
  return (
    <div className="group flex items-start gap-2.5 text-sm">
      <input
        type="checkbox"
        checked={opt}
        aria-label={title}
        onChange={(e) => {
          const v = e.target.checked;
          start(async () => {
            setOpt(v);
            await toggleTask(id, projectId, v);
            await onChange();
          });
        }}
        className="mt-0.5 h-[18px] w-[18px] shrink-0 accent-brand"
      />
      <span className={`flex-1 ${opt ? "text-muted line-through" : ""}`}>
        {title}
        {due && <span className={`ml-2 text-xs ${overdue && !opt ? "font-semibold text-brand" : "text-muted"}`}>{due}</span>}
      </span>
      <button
        type="button"
        aria-label="Aufgabe löschen"
        onClick={() => start(async () => { await deleteTask(id); await onChange(); })}
        className="rounded p-1 text-muted opacity-0 hover:text-brand focus:opacity-100 group-hover:opacity-100"
      >
        <Icon name="trash" size={15} />
      </button>
    </div>
  );
}

export function ConfirmButton({ action, children, question }: { action: () => Promise<void>; children: React.ReactNode; question: string }) {
  const [pending, start] = useTransition();
  return (
    <button
      type="button"
      disabled={pending}
      onClick={() => {
        if (window.confirm(question)) start(action);
      }}
      className="text-[13px] text-muted underline hover:text-brand"
    >
      {children}
    </button>
  );
}
