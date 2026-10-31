"use client";

import Link from "next/link";
import { Suspense } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { Icon } from "@/components/Icon";
import { StatusSteps, TaskItem, ConfirmButton } from "@/components/ProjectBits";
import { AsyncForm, ErrorBox, Loading } from "@/components/Ui";
import { addContact, addDocument, addNote, addTask, addVisit, deleteDocument, deleteProject, loadProject, updateContact, useLoad } from "@/lib/db";
import { chf, chf2, dmy, initials, today } from "@/lib/format";
import type { Contact, StatusKey } from "@/lib/types";

const MONTHS = ["Jan.", "Feb.", "März", "Apr.", "Mai", "Juni", "Juli", "Aug.", "Sep.", "Okt.", "Nov.", "Dez."];

export default function Page() {
  return (
    <Suspense fallback={<Loading />}>
      <ProjectPage />
    </Suspense>
  );
}

function ProjectPage() {
  const id = useSearchParams().get("id") ?? "";
  const router = useRouter();
  const { data, error, reload } = useLoad(() => loadProject(id), [id]);
  if (error) return <ErrorBox error={error} />;
  if (!data) return <Loading />;
  const { project, contacts, visits: vs, tasks: ts, docs, events: evs } = data;
  if (!project) {
    return (
      <div className="flex flex-col items-start gap-3">
        <p>Projekt nicht gefunden.</p>
        <Link href="/" className="btn-secondary">Zu den Projekten</Link>
      </div>
    );
  }
  const t = today();

  const stepDates: Partial<Record<StatusKey, string>> = {
    anfrage: dmy(project.created_at),
    abklaerung: vs.filter((v) => v.date).map((v) => dmy(v.date)).reverse().join(" · ") || undefined,
    offerte: project.offer_date ? `${project.status === "offerte" ? "erstellt " : ""}${dmy(project.offer_date)}` : undefined,
    versendet: project.follow_up ? `nachfassen ${dmy(project.follow_up)}` : undefined,
  };
  const openCount = ts.filter((x) => !x.done).length;

  return (
    <div className="mx-auto flex max-w-[1180px] flex-col gap-5">
      <Link href="/" className="inline-flex items-center gap-1.5 text-[13.5px] text-muted hover:text-ink">
        <Icon name="back" size={14} /> Alle Projekte
      </Link>

      <header className="flex flex-wrap items-end gap-4">
        <div className="flex min-w-0 flex-col gap-1.5">
          <div className="text-xs uppercase tracking-[.12em] text-muted">
            {[project.offer_ref && `Nr. ${project.offer_ref}`, project.location, project.services.join(", ")].filter(Boolean).join(" · ")}
          </div>
          <h1 className="font-display text-[32px] font-extrabold leading-tight tracking-tight">{project.title}</h1>
          {project.client_company && <div className="text-[14.5px] text-[#4a4843]">{project.client_company}</div>}
        </div>
        <div className="ml-auto flex flex-wrap gap-2.5">
          <Link href={`/projekt/bearbeiten/?id=${id}`} className="btn-secondary">
            <Icon name="edit" size={16} /> Bearbeiten
          </Link>
        </div>
      </header>

      <StatusSteps key={project.status} projectId={id} status={project.status} dates={stepDates} onChange={reload} />

      <div className="flex flex-wrap items-start gap-5">
        <div className="flex min-w-0 flex-[999_1_520px] flex-col gap-5">
          <section className="panel" aria-labelledby="h-off">
            <div className="flex items-center justify-between gap-3">
              <h2 id="h-off" className="font-display text-[17px] font-extrabold">Offerte</h2>
              <Link href={`/projekt/bearbeiten/?id=${id}`} className="text-[13.5px] font-semibold text-brand-dark">Angaben ändern</Link>
            </div>
            <div className="grid grid-cols-2 gap-4 sm:grid-cols-4">
              <Fact label="Total netto" big value={chf(project.amount_net) ?? "—"} />
              <Fact label="Inkl. MWST 8.1 %" value={project.amount_net != null ? chf2(Number(project.amount_net) * 1.081) : "—"} />
              <Fact label="Datum" value={dmy(project.offer_date, true) || "—"} />
              <Fact label={project.status === "versendet" ? "Nachfassen" : "Gültig bis"} value={dmy(project.status === "versendet" ? project.follow_up : project.valid_until, true) || "—"} />
            </div>
            {project.description && <p className="whitespace-pre-line text-sm leading-relaxed">{project.description}</p>}
          </section>

          <section className="panel" aria-labelledby="h-beg">
            <h2 id="h-beg" className="font-display text-[17px] font-extrabold">Begehungen und Notizen</h2>
            {vs.length === 0 && <p className="text-sm text-muted">Noch keine Begehung erfasst.</p>}
            {vs.map((v, i) => (
              <article key={v.id} className={`flex gap-4 ${i > 0 ? "border-t border-[#EEEBE5] pt-3.5" : ""}`}>
                <div className="w-16 shrink-0 rounded-lg border border-line py-2 text-center">
                  {v.date ? (
                    <>
                      <div className="font-display text-xl font-extrabold">{Number(v.date.slice(8, 10))}</div>
                      <div className="muted">{MONTHS[Number(v.date.slice(5, 7)) - 1]}</div>
                    </>
                  ) : (
                    <div className="muted py-2">offen</div>
                  )}
                </div>
                <div className="flex min-w-0 flex-col gap-1.5">
                  <div className="text-[14.5px] font-semibold">{v.title}</div>
                  {v.participants && <div className="muted">{v.participants}</div>}
                  {v.notes && <p className="whitespace-pre-line text-sm leading-relaxed">{v.notes}</p>}
                </div>
              </article>
            ))}
            <details>
              <summary className="btn-secondary w-fit cursor-pointer list-none">
                <Icon name="plus" size={16} /> Begehung oder Notiz
              </summary>
              <AsyncForm run={(fd) => addVisit(id, fd)} after={reload} className="mt-3 grid gap-3 sm:grid-cols-3">
                <Input name="date" label="Datum" type="date" />
                <Input name="title" label="Titel" placeholder="Begehung vor Ort" />
                <Input name="participants" label="Dabei" placeholder="Namen" />
                <label className="flex flex-col gap-1.5 sm:col-span-3">
                  <span className="label">Notizen</span>
                  <textarea name="notes" rows={4} className="field h-auto py-2.5" placeholder="Befunde, Masse, Zugänge, Besonderheiten" />
                </label>
                <div className="sm:col-span-3"><button className="btn-primary">Speichern</button></div>
              </AsyncForm>
            </details>
          </section>

          <section className="panel" aria-labelledby="h-ver">
            <h2 id="h-ver" className="font-display text-[17px] font-extrabold">Verlauf</h2>
            <AsyncForm run={(fd) => addNote(id, fd)} after={reload} className="flex gap-2">
              <label className="sr-only" htmlFor="note">Eintrag</label>
              <input id="note" name="text" className="field" placeholder="z. B. Telefonat mit Kunde, Offerte nachgefragt" />
              <button className="btn-secondary shrink-0">Eintragen</button>
            </AsyncForm>
            <ol className="flex flex-col gap-3 text-sm">
              {evs.map((e) => (
                <li key={e.id} className="flex gap-3">
                  <span className="w-[76px] shrink-0 text-xs leading-5 text-muted">{dmy(e.date, true)}</span>
                  <span>{e.text}</span>
                </li>
              ))}
            </ol>
          </section>
        </div>

        <aside className="flex min-w-0 flex-[1_1_300px] flex-col gap-5">
          <section className="panel" aria-labelledby="h-kon">
            <h2 id="h-kon" className="font-display text-[17px] font-extrabold">Kontakt</h2>
            {contacts.map((c) => (
              <div key={c.id} className="flex flex-col gap-3 border-b border-[#EEEBE5] pb-4 last:border-0 last:pb-0">
                <div className="flex items-center gap-3">
                  <div className="flex h-11 w-11 items-center justify-center rounded-full bg-night text-sm font-semibold text-white">{initials(c.name)}</div>
                  <div className="leading-tight">
                    <div className="font-semibold">{c.name}</div>
                    <div className="muted">{[c.role, c.company].filter(Boolean).join(" · ")}</div>
                  </div>
                </div>
                <div className="text-sm leading-relaxed">
                  {c.address && <div>{c.address}</div>}
                  {c.phone && <div className="tabular-nums">{c.phone}</div>}
                  {c.email && <div className="break-all">{c.email}</div>}
                </div>
                <div className="grid grid-cols-2 gap-2">
                  {c.phone ? (
                    <a href={`tel:${c.phone.replace(/\s/g, "")}`} className="btn-secondary h-10"><Icon name="phone" size={16} /> Anrufen</a>
                  ) : (
                    <span className="btn-secondary h-10 opacity-50">Kein Telefon</span>
                  )}
                  {c.email ? (
                    <a href={`mailto:${c.email}?subject=${encodeURIComponent(project.title)}`} className="btn-secondary h-10"><Icon name="mail" size={16} /> E-Mail</a>
                  ) : (
                    <span className="btn-secondary h-10 opacity-50">Keine E-Mail</span>
                  )}
                </div>
                <details>
                  <summary className="cursor-pointer list-none text-[13px] text-muted underline">Kontakt bearbeiten</summary>
                  <ContactForm run={(fd) => updateContact(c.id, fd)} after={reload} c={c} />
                </details>
              </div>
            ))}
            <details>
              <summary className="cursor-pointer list-none text-[13px] font-semibold text-brand-dark">+ Kontakt hinzufügen</summary>
              <ContactForm run={(fd) => addContact(id, fd)} after={reload} />
            </details>
            {project.owner && (
              <div className="flex items-center gap-2.5 border-t border-[#EEEBE5] pt-3">
                <div className="flex h-[30px] w-[30px] items-center justify-center rounded-full bg-[#E9E5DE] text-[11px] font-semibold">{initials(project.owner)}</div>
                <div className="text-[13.5px] leading-tight">{project.owner}<br /><span className="muted">Zuständig, Swiss Brandschutz</span></div>
              </div>
            )}
          </section>

          <section className="panel" aria-labelledby="h-auf">
            <div className="flex items-center justify-between">
              <h2 id="h-auf" className="font-display text-[17px] font-extrabold">Aufgaben</h2>
              <span className="muted">{openCount} offen</span>
            </div>
            <div className="flex flex-col gap-2.5">
              {ts.map((x) => (
                <TaskItem key={x.id + String(x.done)} id={x.id} projectId={id} title={x.title} due={dmy(x.due)} done={x.done} overdue={!!x.due && x.due <= t} onChange={reload} />
              ))}
            </div>
            <AsyncForm run={(fd) => addTask(id, fd)} after={reload} className="flex flex-wrap gap-2">
              <label className="sr-only" htmlFor="tt">Neue Aufgabe</label>
              <input id="tt" name="title" className="field min-w-0 flex-[1_1_160px]" placeholder="Neue Aufgabe" />
              <label className="sr-only" htmlFor="td">Fällig am</label>
              <input id="td" name="due" type="date" className="field w-[150px]" />
              <button className="btn-secondary">Hinzufügen</button>
            </AsyncForm>
          </section>

          <section className="panel" aria-labelledby="h-dok">
            <h2 id="h-dok" className="font-display text-[17px] font-extrabold">Unterlagen</h2>
            <div className="flex flex-col text-sm">
              {docs.map((d) => (
                <div key={d.id} className="group flex items-center justify-between gap-2 border-b border-[#EEEBE5] py-2">
                  <a href={d.url} target="_blank" rel="noopener noreferrer" className="flex min-w-0 items-center gap-2 hover:text-brand-dark">
                    <Icon name="file" size={16} className="shrink-0 text-muted" />
                    <span className="truncate">{d.name}</span>
                  </a>
                  <span className="flex items-center gap-1">
                    <span className="muted">{dmy(d.date)}</span>
                    <button
                      type="button"
                      onClick={async () => { await deleteDocument(d.id); await reload(); }}
                      aria-label={`${d.name} entfernen`}
                      className="rounded p-1 text-muted opacity-0 hover:text-brand focus:opacity-100 group-hover:opacity-100"
                    >
                      <Icon name="trash" size={14} />
                    </button>
                  </span>
                </div>
              ))}
            </div>
            <details>
              <summary className="cursor-pointer list-none text-[13px] font-semibold text-brand-dark">+ Link zu Dokument</summary>
              <AsyncForm run={(fd) => addDocument(id, fd)} after={reload} className="mt-3 flex flex-col gap-2.5">
                <Input name="name" label="Bezeichnung" placeholder="Offerte, Plan, Protokoll" />
                <Input name="url" label="Link" type="url" placeholder="https://" />
                <button className="btn-secondary w-fit">Speichern</button>
              </AsyncForm>
            </details>
          </section>

          <div className="px-1">
            <ConfirmButton
              action={async () => {
                await deleteProject(id);
                router.replace("/");
              }}
              question={`Projekt «${project.title}» mit allen Notizen endgültig löschen?`}
            >
              Projekt löschen
            </ConfirmButton>
          </div>
        </aside>
      </div>
    </div>
  );
}

function Fact({ label, value, big }: { label: string; value: string; big?: boolean }) {
  return (
    <div>
      <div className="muted">{label}</div>
      <div className={big ? "font-display text-2xl font-extrabold tabular-nums" : "mt-1.5 text-base font-semibold tabular-nums"}>{value}</div>
    </div>
  );
}

function Input({ name, label, type = "text", placeholder, defaultValue }: { name: string; label: string; type?: string; placeholder?: string; defaultValue?: string | null }) {
  return (
    <label className="flex min-w-0 flex-col gap-1.5">
      <span className="label">{label}</span>
      <input name={name} type={type} placeholder={placeholder} defaultValue={defaultValue ?? undefined} className="field" />
    </label>
  );
}

function ContactForm({ run, after, c }: { run: (fd: FormData) => Promise<unknown>; after: () => unknown; c?: Contact }) {
  return (
    <AsyncForm run={run} after={after} reset={!c} className="mt-3 flex flex-col gap-2.5">
      <Input name="name" label="Name" defaultValue={c?.name} />
      <Input name="role" label="Rolle" defaultValue={c?.role} placeholder="Bauleitung, Auftraggeber" />
      <Input name="company" label="Firma" defaultValue={c?.company} />
      <Input name="phone" label="Telefon" type="tel" defaultValue={c?.phone} />
      <Input name="email" label="E-Mail" type="email" defaultValue={c?.email} />
      <Input name="address" label="Adresse" defaultValue={c?.address} />
      <button className="btn-secondary w-fit">Speichern</button>
    </AsyncForm>
  );
}
