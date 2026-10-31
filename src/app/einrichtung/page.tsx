export const dynamic = "force-dynamic";

const VARS = ["NEXT_PUBLIC_SUPABASE_URL", "NEXT_PUBLIC_SUPABASE_ANON_KEY", "SUPABASE_SERVICE_ROLE_KEY", "ANFRAGE_SECRET"];

export default function SetupPage() {
  const status = VARS.map((v) => ({ v, ok: !!process.env[v] && (v !== "NEXT_PUBLIC_SUPABASE_URL" || process.env[v]!.startsWith("https://")) }));
  return (
    <div className="mx-auto flex min-h-screen max-w-[640px] flex-col justify-center gap-5 px-5 py-10">
      <h1 className="font-display text-3xl font-extrabold">Einrichtung fehlt noch</h1>
      <p className="text-[15px] leading-relaxed">
        Die App ist online, aber die Verbindung zur Datenbank ist noch nicht eingetragen. In Vercel unter
        <b> Settings → Environment Variables</b> diese Werte setzen und danach unter <b>Deployments → … → Redeploy</b> neu bereitstellen.
      </p>
      <ul className="flex flex-col gap-2">
        {status.map(({ v, ok }) => (
          <li key={v} className="flex items-center justify-between rounded-lg border border-line bg-white px-4 py-3 text-sm">
            <code>{v}</code>
            <span className={ok ? "font-semibold text-[#2E5E3A]" : "font-semibold text-brand"}>{ok ? "vorhanden" : "fehlt"}</span>
          </li>
        ))}
      </ul>
      <p className="text-sm text-muted">Die Werte findest du in Supabase unter Project Settings → API. Die URL beginnt mit https:// und endet auf .supabase.co.</p>
    </div>
  );
}
