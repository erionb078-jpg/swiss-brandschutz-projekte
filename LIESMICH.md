# Abrar – Quelldateien

Hilfsdateien, mit denen die Abrar-Website gebaut wurde. Die fertige Website liegt im Zweig `abrar-website`.

- `generatoren/` – Übungsblätter (`sheets.py`), Downloads (`printables.py`), Startseite (`build_landing.py`), PDF-Ausgabe mit Playwright (`pdf.js`, `pdfall.js`), Strichführung (`strokes.py`)
- `gebet/` – Vorlage und Skript der Seite „Gebet lernen“ (`gebet_tpl.html` + `gebet.js` ergeben `gebet/index.html`)
- `suren/` – Generator der Seite „Kurze Suren“
- `buch-deutsch/` – Übersetzung des Buchs: `tr.py` (deutsche Texte), `apply.py` (setzt sie mit PyMuPDF ins PDF)
- `lehrer/` – Skripte, die den Bereich „Lernen mit Lehrer“ in die Startseite eingefügt haben

Die Skripte enthalten noch Pfade aus der alten Arbeitsumgebung. Vor dem Ausführen anpassen.

## Englische Version (Zweig `abrar-website-en`)

- `uebersetzung-en/` – Übersetzungslisten (Deutsch → Englisch) je Seite; `apply.py <datei> <liste>` wendet sie an
- `generatoren-en/` – englische Übungsblätter und Downloads (`printables.py`, `sheets.py`, Ausgabe mit `render.py`), Arbeitsordner `/tmp/sp` mit Schriften, Logo, Qalam/Fuffl-SVG und `glyphs.json`/`strokes.json` aus dem Spiel
- `generatoren-en/header_desk.py` – Header-Szene: Schreibtisch mit Monitor, iPad und Handy, die das Buch zeigen (`header_scene.py` = alte Lehrer-Szene, nicht mehr verwendet)
- Buchseiten `buch/pages/` aus `Abrar_Quran_Reading_2026.pdf` mit `pdftoppm -r 110` und WebP (Qualität 80) erzeugt
