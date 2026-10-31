"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { createProject } from "@/lib/db";
import { Field, OwnerSelect, ServiceChips } from "@/components/Fields";
import { Icon } from "@/components/Icon";
import { addDays, today } from "@/lib/format";

export default function NewInquiryPage() {
  const router = useRouter();
  const [busy, setBusy] = useState(false);
  return (
    <div className="mx-auto flex max-w-[960px] flex-col gap-5">
      <Link href="/" className="inline-flex items-center gap-1.5 text-[13.5px] text-muted hover:text-ink">
        <Icon name="back" size={14} /> Alle Projekte
      </Link>
      <h1 className="font-display text-[30px] font-extrabold tracking-tight">Neue Anfrage</h1>

      <form
        className="flex flex-col gap-5"
        onSubmit={async (e) => {
          e.preventDefault();
          setBusy(true);
          try {
            const id = await createProject(new FormData(e.currentTarget));
            router.push(`/projekt/?id=${id}`);
          } catch (err) {
            alert("Speichern fehlgeschlagen: " + (err instanceof Error ? err.message : String(err)));
            setBusy(false);
          }
        }}
      >
        <section className="panel" aria-labelledby="h-k">
          <h2 id="h-k" className="font-display text-[17px] font-extrabold">Kunde und Kontakt</h2>
          <div className="grid gap-4 sm:grid-cols-2">
            <Field name="company" label="Firma" />
            <Field name="person" label="Kontaktperson" />
            <Field name="phone" label="Telefon" type="tel" />
            <Field name="email" label="E-Mail" type="email" />
          </div>
        </section>

        <section className="panel" aria-labelledby="h-o">
          <h2 id="h-o" className="font-display text-[17px] font-extrabold">Objekt und Leistung</h2>
          <div className="grid gap-4 sm:grid-cols-2">
            <Field name="title" label="Objekt" placeholder="z. B. Fitness-Studio Döttingen" required />
            <Field name="location" label="Ort / Adresse" />
          </div>
          <ServiceChips />
          <label className="flex flex-col gap-1.5">
            <span className="label">Beschreibung</span>
            <textarea name="description" rows={4} className="field h-auto py-2.5" placeholder="Was wird benötigt? Pläne vorhanden? Termine?" />
          </label>
          <label className="flex flex-col gap-1.5">
            <span className="label">Eingang über</span>
            <select name="source" className="field sm:w-1/2" defaultValue="Telefon">
              <option>Telefon</option><option>E-Mail</option><option>Website</option><option>Empfehlung</option><option>Ausschreibung</option><option>Begehung</option>
            </select>
          </label>
        </section>

        <section className="panel" aria-labelledby="h-n">
          <h2 id="h-n" className="font-display text-[17px] font-extrabold">Nächste Schritte</h2>
          <div className="grid gap-4 sm:grid-cols-3">
            <OwnerSelect />
            <Field name="visit" label="Begehung" type="date" />
            <Field name="due" label="Rückmeldung bis" type="date" defaultValue={addDays(today(), 1)} />
          </div>
        </section>

        <div className="flex flex-wrap justify-end gap-2.5">
          <Link href="/" className="btn-secondary">Abbrechen</Link>
          <button disabled={busy} className="btn-primary">{busy ? "Wird angelegt …" : "Projekt anlegen"}</button>
        </div>
      </form>
    </div>
  );
}
