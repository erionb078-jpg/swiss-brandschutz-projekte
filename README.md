# Swiss Brandschutz · Projekte

Projekt-App für Anfragen, Offerten, Begehungen und Kontakte von Swiss Brandschutz.
Läuft unter **projekte.swiss-brandschutz.ch**.

Technik: Next.js 15 · TypeScript · Tailwind CSS 4 · Supabase (Datenbank + Login) · Vercel (Hosting)

---

## Einrichtung (einmalig, ca. 20 Minuten)

### 1. Supabase – Datenbank

1. Auf [supabase.com](https://supabase.com) ein neues Projekt anlegen, Region **Central EU (Zurich)** oder Frankfurt.
2. Links **SQL Editor → New query**, Inhalt von `supabase/schema.sql` einfügen → **Run**.
3. Nochmals **New query**, Inhalt von `supabase/seed.sql` einfügen → **Run**. Damit sind alle aktuellen Projekte drin.
4. **Authentication → Sign In / Providers:** „Allow new users to sign up“ **ausschalten**. So kann sich niemand selbst registrieren.
5. **Authentication → Users → Add user → Create new user:** für dich und Fadil je E-Mail und Passwort setzen, „Auto Confirm User“ anhaken.
6. **Project Settings → API:** Diese drei Werte brauchst du gleich für Vercel:
   - Project URL
   - `anon` `public` Key
   - `service_role` Key (geheim halten)

### 2. Vercel – Hosting

1. Auf [vercel.com](https://vercel.com) mit GitHub anmelden → **Add New → Project** → dieses Repo importieren.
2. Unter **Environment Variables** eintragen:

   | Name | Wert |
   |---|---|
   | `NEXT_PUBLIC_SUPABASE_URL` | Project URL aus Supabase |
   | `NEXT_PUBLIC_SUPABASE_ANON_KEY` | `anon` Key |
   | `SUPABASE_SERVICE_ROLE_KEY` | `service_role` Key |
   | `ANFRAGE_SECRET` | ein langes Zufallswort, z. B. 40 Zeichen |

3. **Deploy.** Nach 1–2 Minuten läuft die App unter einer `….vercel.app`-Adresse.

### 3. Domain projekte.swiss-brandschutz.ch

1. In Vercel: Projekt → **Settings → Domains** → `projekte.swiss-brandschutz.ch` eingeben → **Add**.
2. Vercel zeigt einen **CNAME-Eintrag** an (Ziel meist `cname.vercel-dns.com`).
3. Beim Anbieter, wo `swiss-brandschutz.ch` verwaltet wird (z. B. Hostpoint, Infomaniak, Cyon): DNS-Verwaltung öffnen und neuen Eintrag anlegen:
   - Typ: `CNAME`
   - Name/Host: `projekte`
   - Ziel/Wert: der Wert, den Vercel anzeigt
4. Nach wenigen Minuten (selten bis 24 h) zeigt Vercel „Valid Configuration“, das SSL-Zertifikat kommt automatisch.
5. In Supabase **Authentication → URL Configuration → Site URL** auf `https://projekte.swiss-brandschutz.ch` setzen.

Die bestehende Website auf swiss-brandschutz.ch wird dadurch nicht verändert.

---

## Arbeiten mit der App

- **Board:** Karten per Ziehen in die nächste Spalte schieben. Beim Verschieben nach „Versendet“ wird automatisch ein Nachfass-Termin 7 Tage später gesetzt.
- **Heute:** Oben stehen überfällige und bald fällige Aufgaben und Nachfass-Termine.
- **Projektseite:** Status per Klick setzen, Offerte, Begehungen mit Notizen, Kontakte, Aufgaben, Links zu Dokumenten und ein Verlauf.
- **Neue Anfrage:** Formular erfasst Projekt, Kontakt und eine erste Aufgabe „Kunde kontaktieren“.

## Anfragen von der Website automatisch übernehmen

Das Kontaktformular auf swiss-brandschutz.ch kann jede Anfrage zusätzlich an die App schicken:

```
POST https://projekte.swiss-brandschutz.ch/api/anfrage
Header:  Content-Type: application/json
         x-anfrage-secret: <ANFRAGE_SECRET>
Body:    { "name": "Michael Sörensen", "firma": "Arkoteam GmbH", "telefon": "076 786 44 21",
           "email": "info@arkoteam.gmbh", "ort": "5312 Döttingen",
           "nachricht": "Wir benötigen … eine Brandschutztüre." }
```

Die Anfrage erscheint dann als neue Karte in „Neue Anfrage“, mit Kontakt und Aufgabe „kontaktieren“ (fällig am nächsten Tag). Der Aufruf muss vom Server der Website kommen, nicht aus dem Browser, damit das Geheimwort nicht sichtbar ist.

## Lokal entwickeln

```bash
cp .env.example .env.local   # Werte aus Supabase eintragen
npm install
npm run dev                  # http://localhost:3000
```

## Weitere Benutzer

In Supabase unter **Authentication → Users → Add user** anlegen. Alle angemeldeten Benutzer sehen und bearbeiten alle Projekte. Die Auswahl „Zuständig“ steht in `src/lib/types.ts` (`OWNERS`).
