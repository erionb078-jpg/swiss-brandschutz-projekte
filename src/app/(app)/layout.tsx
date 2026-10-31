import Image from "next/image";
import { createClient } from "@/lib/supabase/server";
import { NavLinks } from "@/components/NavLinks";
import { Icon } from "@/components/Icon";
import { logout } from "@/app/actions";
import { initials, today } from "@/lib/format";

export default async function AppLayout({ children }: { children: React.ReactNode }) {
  const supabase = await createClient();
  const [{ data: auth }, { count }] = await Promise.all([
    supabase.auth.getUser(),
    supabase.from("tasks").select("id", { count: "exact", head: true }).eq("done", false).lte("due", today()),
  ]);
  const email = auth.user?.email ?? "";
  const name = (auth.user?.user_metadata?.name as string | undefined) ?? email.split("@")[0];

  return (
    <div className="flex min-h-screen flex-col lg:flex-row">
      <nav aria-label="Hauptnavigation" className="flex shrink-0 flex-col gap-4 bg-night px-4 py-4 text-white lg:sticky lg:top-0 lg:h-screen lg:w-[250px] lg:gap-7 lg:py-6">
        <div className="flex items-center justify-between lg:block">
          <Image src="/logo-hell.png" alt="Swiss Brandschutz" width={160} height={36} className="ml-2 h-9 w-auto" priority />
          <form action={logout} className="lg:hidden">
            <button className="rounded-lg p-2 text-[#C9C6C0] hover:bg-night-2" aria-label="Abmelden"><Icon name="logout" /></button>
          </form>
        </div>
        <NavLinks openTasks={count ?? 0} />
        <div className="mt-auto hidden items-center gap-2.5 p-2 lg:flex">
          <div className="flex h-9 w-9 items-center justify-center rounded-full bg-[#3a3b3f] text-xs font-semibold">{initials(name)}</div>
          <div className="min-w-0 flex-1 text-[13px] leading-tight">
            <div className="truncate">{name}</div>
            <div className="truncate text-[#A8A5A0]">Swiss Brandschutz</div>
          </div>
          <form action={logout}>
            <button className="rounded-lg p-2 text-[#C9C6C0] hover:bg-night-2 hover:text-white" aria-label="Abmelden" title="Abmelden"><Icon name="logout" /></button>
          </form>
        </div>
      </nav>
      <main className="min-w-0 flex-1 px-4 py-6 sm:px-8">{children}</main>
    </div>
  );
}
