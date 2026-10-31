# Swiss Brandschutz · Projekte

Projekt-App für Anfragen, Offerten, Begehungen und Kontakte von Swiss Brandschutz.
Läuft unter **projekte.swiss-brandschutz.ch**.

Technik: Next.js 15 (statischer Export) · TypeScript · Tailwind CSS 4 · Supabase (Datenbank + Login) · Vercel (Hosting)

---

## Einrichtung (einmalig, ca. 20 Minuten)

### 1. Supabase – Datenbank

1. Auf [supabase.com](https://supabase.com) ein neues Projekt anlegen, Region **Central EU (Zurich)** oder Frankfurt.
2. Links **SQL Editor → New query**, Inhalt von `supabase/schema.sql` einfügen → **Run**.
3. Nochmals **New query**, Inhalt von `supabase/seed.sql` einfügen → **Run**. Damit sind alle aktuellen Projekte drin.
4. **Authentication → Sign In / Providers:** „Allow new users to sign up“ **ausschalten**. So kann sich niemand selbst registrieren.
5. **Authentication → Users → Add user → Create new user:** für dich und Fadil je E-Mail und Passwort setzen, „Auto Confirm User“ anhaken.
6. **Project Settings → API:** Project URL und `anon` `public` Key notieren.

### 2. Ordner bauen

```bash
cp .env.example .env.local   # Project URL und anon Key eintragen
npm install
npm run build                # erzeugt den Ordner "out"
```

### 3. Auf Vercel hochladen (ohne GitHub)

1. [vercel.com/drop](https://vercel.com/drop) öffnen.
2. Den Ordner **out** ins Browserfenster ziehen. Nach wenigen Sekunden ist die App online.
3. Die Seite einem Vercel-Konto zuordnen („Claim“), damit sie dauerhaft bleibt und eine eigene Domain bekommt.

Alternativ mit GitHub: Repo in Vercel importieren und unter Environment Variables `NEXT_PUBLIC_SUPABASE_URL` und `NEXT_PUBLIC_SUPABASE_ANON_KEY` setzen. Vercel baut dann bei jeder Änderung neu.

### 4. Domain projekte.swiss-brandschutz.ch

1. In Vercel: Projekt → **Settings → Domains** → `projekte.swiss-brandschutz.ch` → **Add**.
2. Beim Anbieter von `swiss-brandschutz.ch` einen DNS-Eintrag anlegen: Typ `CNAME`, Name `projekte`, Ziel der Wert, den Vercel anzeigt.
3. In Supabase **Authentication → URL Configuration → Site URL** auf `https://projekte.swiss-brandschutz.ch` setzen.

---

## Arbeiten mit der App

- **Board:** Karten per Ziehen in die nächste Spalte schieben. Beim Verschieben nach „Versendet“ wird automatisch ein Nachfass-Termin 7 Tage später gesetzt.
- **Heute:** Oben stehen überfällige und bald fällige Aufgaben und Nachfass-Termine.
- **Projektseite:** Status per Klick setzen, Offerte, Begehungen mit Notizen, Kontakte, Aufgaben, Links zu Dokumenten und ein Verlauf.
- **Neue Anfrage:** Formular erfasst Projekt, Kontakt und eine erste Aufgabe „Kunde kontaktieren“.

Die App ist eine reine statische Seite. Alle Daten liegen in Supabase und sind nur nach Login sichtbar (Row Level Security).

## Lokal entwickeln

```bash
cp .env.example .env.local   # Werte aus Supabase eintragen
npm install
npm run dev                  # http://localhost:3000
```

## Weitere Benutzer

In Supabase unter **Authentication → Users → Add user** anlegen. Alle angemeldeten Benutzer sehen und bearbeiten alle Projekte. Die Auswahl „Zuständig“ steht in `src/lib/types.ts` (`OWNERS`).
