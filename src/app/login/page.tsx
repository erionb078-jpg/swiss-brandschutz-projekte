"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { sb } from "@/lib/supabase";

export default function LoginPage() {
  const router = useRouter();
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  return (
    <div className="flex min-h-screen items-center justify-center bg-night px-4">
      <form
        onSubmit={async (e) => {
          e.preventDefault();
          setBusy(true);
          setError(null);
          const fd = new FormData(e.currentTarget);
          const { error } = await sb().auth.signInWithPassword({ email: String(fd.get("email")), password: String(fd.get("password")) });
          if (error) {
            setError("E-Mail oder Passwort stimmt nicht.");
            setBusy(false);
          } else router.replace("/");
        }}
        className="flex w-full max-w-[380px] flex-col gap-4 rounded-xl bg-white p-7"
      >
        <div className="-mx-7 -mt-7 mb-2 rounded-t-xl bg-night px-7 pb-5 pt-7">
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src="/logo-hell.png" alt="Swiss Brandschutz" className="h-10 w-auto" />
        </div>
        <h1 className="font-display text-2xl font-extrabold">Projekte</h1>
        <label className="flex flex-col gap-1.5">
          <span className="label">E-Mail</span>
          <input name="email" type="email" autoComplete="email" required className="field" />
        </label>
        <label className="flex flex-col gap-1.5">
          <span className="label">Passwort</span>
          <input name="password" type="password" autoComplete="current-password" required className="field" />
        </label>
        {error && <p role="alert" className="text-sm font-medium text-brand">{error}</p>}
        <button disabled={busy} className="btn-primary">{busy ? "Anmelden …" : "Anmelden"}</button>
      </form>
    </div>
  );
}
