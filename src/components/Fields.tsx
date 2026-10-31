import { SERVICES, OWNERS } from "@/lib/types";

export function Field({ name, label, type = "text", placeholder, defaultValue, required, className = "" }: {
  name: string; label: string; type?: string; placeholder?: string; defaultValue?: string | number | null; required?: boolean; className?: string;
}) {
  return (
    <label className={`flex min-w-0 flex-col gap-1.5 ${className}`}>
      <span className="label">{label}</span>
      <input name={name} type={type} placeholder={placeholder} required={required} defaultValue={defaultValue ?? undefined} className="field" />
    </label>
  );
}

export function ServiceChips({ selected = [] }: { selected?: string[] }) {
  return (
    <fieldset className="flex flex-col gap-1.5">
      <legend className="label mb-1.5">Leistung</legend>
      <div className="flex flex-wrap gap-2">
        {SERVICES.map((s) => (
          <label key={s} className="inline-flex min-h-10 cursor-pointer items-center gap-2 rounded-full border border-line-2 bg-white px-3.5 text-[13.5px] has-[:checked]:border-night has-[:checked]:font-semibold">
            <input type="checkbox" name="services" value={s} defaultChecked={selected.includes(s)} className="h-4 w-4 accent-brand" />
            {s}
          </label>
        ))}
      </div>
    </fieldset>
  );
}

export function OwnerSelect({ defaultValue }: { defaultValue?: string | null }) {
  return (
    <label className="flex min-w-0 flex-col gap-1.5">
      <span className="label">Zuständig</span>
      <select name="owner" defaultValue={defaultValue ?? OWNERS[0]} className="field">
        {OWNERS.map((o) => <option key={o}>{o}</option>)}
      </select>
    </label>
  );
}
