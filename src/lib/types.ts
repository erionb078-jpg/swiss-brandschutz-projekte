export const STATUSES = [
  { key: "anfrage", label: "Neue Anfrage" },
  { key: "abklaerung", label: "Abklärung · Begehung" },
  { key: "offerte", label: "Offerte bereit" },
  { key: "versendet", label: "Versendet · Nachfassen" },
  { key: "auftrag", label: "Auftrag" },
  { key: "absage", label: "Absage" },
] as const;

export type StatusKey = (typeof STATUSES)[number]["key"];

export const STEPS: { key: StatusKey; label: string }[] = [
  { key: "anfrage", label: "Anfrage" },
  { key: "abklaerung", label: "Begehung" },
  { key: "offerte", label: "Offerte" },
  { key: "versendet", label: "Versendet" },
  { key: "auftrag", label: "Auftrag" },
];

export const SERVICES = ["Türen", "Abschottungen", "Verkleidungen", "Schrankfronten", "Sonstiges"];

export const OWNERS = ["Fadil Fazliu", "Erion"];

export type Project = {
  id: string;
  title: string;
  location: string | null;
  client_company: string | null;
  services: string[];
  description: string | null;
  status: StatusKey;
  amount_net: number | null;
  offer_ref: string | null;
  offer_date: string | null;
  valid_until: string | null;
  follow_up: string | null;
  source: string | null;
  owner: string | null;
  position: number;
  created_at: string;
};

export type Contact = {
  id: string;
  project_id: string | null;
  name: string;
  company: string | null;
  role: string | null;
  phone: string | null;
  email: string | null;
  address: string | null;
};

export type Visit = {
  id: string;
  project_id: string;
  date: string | null;
  title: string;
  participants: string | null;
  notes: string | null;
};

export type Task = { id: string; project_id: string; title: string; due: string | null; done: boolean };
export type Doc = { id: string; project_id: string; name: string; url: string; date: string | null };
export type Event = { id: string; project_id: string; date: string; text: string };
