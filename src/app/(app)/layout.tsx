"use client";

import { useEffect, useState } from "react";
import { useRouter, usePathname } from "next/navigation";
import { sb, SUPABASE_URL } from "@/lib/supabase";
import { openTaskCount } from "@/lib/db";
import { NavLinks } from "@/components/NavLinks";
import { Icon } from "@/components/Icon";
import { initials } from "@/lib/format";

export default function AppLayout({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const path = usePathname();
  const [email, setEmail] = useState<string | null>(null);
  const [count, setCount] = useState(0);

  useEffect(() => {
    if (!SUPABASE_URL) return;
    sb().auth.getSession().then(({ data }) => {
      if (!data.session) router.replace("/login/");
      else setEmail(data.session.user.email ?? "");
    });
    const { data: sub } = sb().auth.onAuthStateChange((_e, session) => {
      if (!session) router.replace("/login/");
    });
    return () => sub.subscription.unsubscribe();
  }, [router]);

  useEffect(() => {
    if (email !== null) openTaskCount().then(setCount).catch(() => {});
  }, [email, path]);

  if (!SUPABASE_URL) {
    return <div className="p-10 text-lg">Supabase-Verbindung fehlt in dieser Version. Bitte neu erstellen lassen.</div>;
  }
  if (email === null) {
    return <div className="flex min-h-screen items-center justify-center bg-night"><span className="sr-only">Wird geladen</span></div>;
  }

  const name = email.split("@")[0];
  const logout = async () => {
    await sb().auth.signOut();
    router.replace("/login/");
  };

  return (
    <div className="flex min-h-screen flex-col lg:flex-row">
      <nav aria-label="Hauptnavigation" className="flex shrink-0 flex-col gap-4 bg-night px-4 py-4 text-white lg:sticky lg:top-0 lg:h-screen lg:w-[250px] lg:gap-7 lg:py-6">
        <div className="flex items-center justify-between lg:block">
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src="/logo-hell.png" alt="Swiss Brandschutz" className="ml-2 h-9 w-auto" />
          <button onClick={logout} className="rounded-lg p-2 text-[#C9C6C0] hover:bg-night-2 lg:hidden" aria-label="Abmelden"><Icon name="logout" /></button>
        </div>
        <NavLinks openTasks={count} />
        <div className="mt-auto hidden items-center gap-2.5 p-2 lg:flex">
          <div className="flex h-9 w-9 items-center justify-center rounded-full bg-[#3a3b3f] text-xs font-semibold">{initials(name)}</div>
          <div className="min-w-0 flex-1 text-[13px] leading-tight">
            <div className="truncate">{name}</div>
            <div className="truncate text-[#A8A5A0]">Swiss Brandschutz</div>
          </div>
          <button onClick={logout} className="rounded-lg p-2 text-[#C9C6C0] hover:bg-night-2 hover:text-white" aria-label="Abmelden" title="Abmelden"><Icon name="logout" /></button>
        </div>
      </nav>
      <main className="min-w-0 flex-1 px-4 py-6 sm:px-8">{children}</main>
    </div>
  );
}
