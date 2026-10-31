"use client";

import Image from "next/image";
import { useActionState } from "react";
import { login } from "@/app/actions";

export default function LoginPage() {
  const [error, action, pending] = useActionState(login, null);
  return (
    <div className="flex min-h-screen items-center justify-center bg-night px-4">
      <form action={action} className="flex w-full max-w-[380px] flex-col gap-4 rounded-xl bg-white p-7">
        <div className="-mx-7 -mt-7 mb-2 rounded-t-xl bg-night px-7 pb-5 pt-7">
          <Image src="/logo-hell.png" alt="Swiss Brandschutz" width={180} height={40} className="h-10 w-auto" priority />
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
        <button disabled={pending} className="btn-primary">{pending ? "Anmelden …" : "Anmelden"}</button>
      </form>
    </div>
  );
}
