export function Loading() {
  return <div className="py-16 text-center text-sm text-muted">Wird geladen …</div>;
}
export function ErrorBox({ error }: { error: string }) {
  return <div role="alert" className="rounded-lg bg-brand-soft px-4 py-3 text-sm text-brand-dark">Fehler beim Laden: {error}</div>;
}

/** Formular, das eine asynchrone Funktion aufruft, danach leert und neu lädt. */
export function AsyncForm({ run, after, className, children, reset = true }: {
  run: (fd: FormData) => Promise<unknown>;
  after?: () => unknown;
  className?: string;
  children: React.ReactNode;
  reset?: boolean;
}) {
  return (
    <form
      className={className}
      onSubmit={async (e) => {
        e.preventDefault();
        const form = e.currentTarget;
        const btn = form.querySelector("button[type=submit],button:not([type])") as HTMLButtonElement | null;
        if (btn) btn.disabled = true;
        try {
          await run(new FormData(form));
          if (reset) form.reset();
          form.closest("details")?.removeAttribute("open");
          await after?.();
        } catch (err) {
          alert("Speichern fehlgeschlagen: " + (err instanceof Error ? err.message : String(err)));
        } finally {
          if (btn) btn.disabled = false;
        }
      }}
    >
      {children}
    </form>
  );
}
