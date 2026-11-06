# Abrar – Quelldateien

Hilfsdateien, mit denen die Abrar-Website gebaut wurde. Die fertige Website liegt im Zweig `abrar-website`.

- `generatoren/` – Übungsblätter (`sheets.py`), Downloads (`printables.py`), Startseite (`build_landing.py`), PDF-Ausgabe mit Playwright (`pdf.js`, `pdfall.js`), Strichführung (`strokes.py`)
- `gebet/` – Vorlage und Skript der Seite „Gebet lernen“ (`gebet_tpl.html` + `gebet.js` ergeben `gebet/index.html`)
- `suren/` – Generator der Seite „Kurze Suren“
- `buch-deutsch/` – Übersetzung des Buchs: `tr.py` (deutsche Texte), `apply.py` (setzt sie mit PyMuPDF ins PDF)
- `lehrer/` – Skripte, die den Bereich „Lernen mit Lehrer“ in die Startseite eingefügt haben

Die Skripte enthalten noch Pfade aus der alten Arbeitsumgebung. Vor dem Ausführen anpassen.
