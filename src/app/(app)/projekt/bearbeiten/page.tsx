"use client";

import Link from "next/link";
import { Suspense, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { loadProject, updateProject, useLoad } from "@/lib/db";
import { Field, OwnerSelect, ServiceChips } from "@/components/Fields";
import { Icon } from "@/components/Icon";
import { ErrorBox, Loading } from "@/components/Ui";

export default function Page() {
  return (
    <Suspense fallback={<Loading />}>
      <EditProjectPage />
    </Suspense>
  );
}

function EditProjectPage() {
  const id = useSearchParams().get("id") ?? "";
  const router = useRouter();
  const [busy, setBusy] = useState(false);
  const { data, error } = useLoad(() => loadProject(id), [id]);
  if (error) return <ErrorBox error={error} />;
  if (!data) return <Loading />;
  const p = data.project;
  if (!p) return <p>Projekt nicht gefunden.</p>;
  const back = `/projekt/?id=${id}`;

  return (
    <div className="mx-auto flex max-w-[960px] flex-col gap-5">
      <Link href={back} className="inline-flex items-center gap-1.5 text-[13.5px] text-muted hover:text-ink">
        <Icon name="back" size={14} /> Zurück zum Projekt
      </Link>
      <h1 className="font-display text-[30px] font-extrabold tracking-tight">Projekt bearbeiten</h1>

      <form
        className="flex flex-col gap-5"
        onSubmit={async (e) => {
          e.preventDefault();
          setBusy(true);
          try {
            await updateProject(id, new FormData(e.currentTarget));
            router.push(back);
          } catch (err) {
            alert("Speichern fehlgeschlagen: " + (err instanceof Error ? err.message : String(err)));
            setBusy(false);
          }
        }}
      >
        <section className="panel">
          <h2 className="font-display text-[17px] font-extrabold">Objekt</h2>
          <div className="grid gap-4 sm:grid-cols-2">
            <Field name="title" label="Objekt" defaultValue={p.title} required />
            <Field name="client_company" label="Kunde (Firma)" defaultValue={p.client_company} />
            <Field name="location" label="Ort / Adresse" defaultValue={p.location} />
            <Field name="source" label="Eingang über" defaultValue={p.source} />
          </div>
          <ServiceChips selected={p.services} />
          <label className="flex flex-col gap-1.5">
            <span className="label">Beschreibung</span>
            <textarea name="description" rows={4} defaultValue={p.description ?? ""} className="field h-auto py-2.5" />
          </label>
        </section>

        <section className="panel">
          <h2 className="font-display text-[17px] font-extrabold">Offerte und Termine</h2>
          <div className="grid gap-4 sm:grid-cols-3">
            <Field name="amount_net" label="Betrag netto (CHF)" defaultValue={p.amount_net} placeholder="z. B. 26450" />
            <Field name="offer_ref" label="Offert-Nr." defaultValue={p.offer_ref} />
            <OwnerSelect defaultValue={p.owner} />
            <Field name="offer_date" label="Offertdatum" type="date" defaultValue={p.offer_date} />
            <Field name="valid_until" label="Gültig bis" type="date" defaultValue={p.valid_until} />
            <Field name="follow_up" label="Nachfassen am" type="date" defaultValue={p.follow_up} />
          </div>
        </section>

        <div className="flex flex-wrap justify-end gap-2.5">
          <Link href={back} className="btn-secondary">Abbrechen</Link>
          <button disabled={busy} className="btn-primary">{busy ? "Speichern …" : "Speichern"}</button>
        </div>
      </form>
    </div>
  );
}
