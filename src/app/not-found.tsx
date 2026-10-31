import Link from "next/link";
export default function NotFound() {
  return (
    <div className="flex min-h-[60vh] flex-col items-center justify-center gap-3">
      <h1 className="font-display text-2xl font-extrabold">Nicht gefunden</h1>
      <Link href="/" className="btn-secondary">Zu den Projekten</Link>
    </div>
  );
}
