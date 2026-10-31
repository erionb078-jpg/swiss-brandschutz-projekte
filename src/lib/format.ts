export function chf(n: number | null | undefined) {
  if (n == null) return null;
  return "CHF " + new Intl.NumberFormat("de-CH", { maximumFractionDigits: 0 }).format(Number(n));
}

export function chf2(n: number) {
  return "CHF " + new Intl.NumberFormat("de-CH", { minimumFractionDigits: 2, maximumFractionDigits: 2 }).format(n);
}

/** "2026-10-29" → "29.10." (oder mit Jahr) */
export function dmy(s: string | null | undefined, year = false) {
  if (!s) return "";
  const [y, m, d] = s.slice(0, 10).split("-");
  return year ? `${d}.${m}.${y}` : `${d}.${m}.`;
}

export function today() {
  return new Date().toLocaleDateString("sv-SE", { timeZone: "Europe/Zurich" });
}

export function addDays(iso: string, n: number) {
  const d = new Date(iso + "T12:00:00Z");
  d.setUTCDate(d.getUTCDate() + n);
  return d.toISOString().slice(0, 10);
}

export function initials(name: string | null | undefined) {
  if (!name) return "–";
  const parts = name.replace(/^(Herr|Frau)\s+/i, "").split(/\s+/).filter(Boolean);
  return ((parts[0]?.[0] ?? "") + (parts.length > 1 ? parts[parts.length - 1][0] : "")).toUpperCase();
}

export function shortName(name: string | null | undefined) {
  if (!name) return "";
  const parts = name.split(/\s+/);
  if (parts.length < 2 || /^(Herr|Frau)$/i.test(parts[0])) return name;
  return `${parts[0][0]}. ${parts.slice(1).join(" ")}`;
}
