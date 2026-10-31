-- Startdaten: aktueller Stand der Swiss-Brandschutz-Projekte (31.10.2026)
-- Nach schema.sql einmal ausführen.

insert into projects (id, title, location, client_company, services, description, status, amount_net, offer_ref, offer_date, valid_until, follow_up, source, owner, position) values
('00000000-0000-4000-8000-000000000001','Fitness-Studio Döttingen','5312 Döttingen','Arkoteam GmbH','{Türen}','Wir benötigen in einem Fitness-Studio in Döttingen eine Brandschutztüre. Plan vorhanden.','anfrage',null,null,null,null,null,'Website','Fadil Fazliu',0),
('00000000-0000-4000-8000-000000000002','SBB UW Steinen · Stahlträger','Steinen','SBB AG Infrastruktur Energie','{Verkleidungen}','Brandschutztechnische Verkleidung der Stahlträger im GIS-Gebäude (nach Begehung 22.10. separat zu offerieren).','abklaerung',null,null,null,null,null,'Begehung','Erion',0),
('00000000-0000-4000-8000-000000000003','SBB UW Steinen · Türen','Steinen','SBB AG Infrastruktur Energie','{Türen}','Brandschutztüren GIS-Gebäude Unterwerk Steinen.','abklaerung',null,null,null,null,null,'Anfrage SBB','Erion',1),
('00000000-0000-4000-8000-000000000004','Jungholzstrasse 43','Zürich','HW Architekten','{Türen,Schrankfronten}','Brandschutzpendenzen Innentüren und Schrankfronten EI30, Schulhaus im laufenden Betrieb, Projekt 224289.70.','offerte',73750,'224289.70','2026-10-25',null,null,'Bauleitung','Fadil Fazliu',0),
('00000000-0000-4000-8000-000000000005','Forelhaus Zürich','Schrennengasse 18, 8003 Zürich','Forelhaus Zürich','{Türen}','Austausch von 15 Brandschutztüren EI30, Ausführung 2027.','offerte',56000,null,'2026-10-19','2026-11-30',null,'Direkt','Fadil Fazliu',1),
('00000000-0000-4000-8000-000000000006','SBB UW Steinen · Abschottungen','Steinen','SBB AG Infrastruktur Energie','{Abschottungen}','Brandabschottungen GIS-Gebäude Unterwerk Steinen.','offerte',26450,null,'2026-10-23',null,null,'Anfrage SBB','Fadil Fazliu',2),
('00000000-0000-4000-8000-000000000007','KITA Baden','Baden','Stadt Baden, Kaufm. Gebäudemanagement','{Verkleidungen,Türen}','Massnahmen 1.8 (Verkleidung Schaltgerätekombination EI30-RF1) und 1.9 (Antipanikschloss SN EN 179), zusätzlich Verkleidung Hauptträger.','offerte',17990,null,'2026-10-28',null,null,'Direkt','Fadil Fazliu',3),
('00000000-0000-4000-8000-000000000008','Letzigarten Zürich, 1. Etappe','Zürich','Halter AG','{Abschottungen}','Brandabschottungen BKP 225.4, Produkte Hilti.','versendet',null,'2026-130','2026-10-27',null,'2026-11-03','Ausschreibung','Erion',0)
on conflict (id) do nothing;

insert into contacts (project_id, name, company, role, phone, email, address) values
('00000000-0000-4000-8000-000000000001','Michael Sörensen','Arkoteam GmbH','Anfragender','076 786 44 21','info@arkoteam.gmbh','5312 Döttingen'),
('00000000-0000-4000-8000-000000000002','Janik Sievert','SBB AG Infrastruktur Energie','Auftraggeber',null,null,'Zollikofen'),
('00000000-0000-4000-8000-000000000003','Janik Sievert','SBB AG Infrastruktur Energie','Auftraggeber',null,null,'Zollikofen'),
('00000000-0000-4000-8000-000000000006','Janik Sievert','SBB AG Infrastruktur Energie','Auftraggeber',null,null,'Zollikofen'),
('00000000-0000-4000-8000-000000000004','Eldi Kaba','HW Architekten','Bauleitung',null,null,'Bachstrasse 9, 8038 Zürich'),
('00000000-0000-4000-8000-000000000005','Frau Milincic','Forelhaus Zürich','Hauswirtschaft & Infrastruktur',null,null,'Schrennengasse 18, 8003 Zürich'),
('00000000-0000-4000-8000-000000000007','Reto Aeschbach','Stadt Baden','Kaufm. Gebäudemanagement',null,null,'Rathausgasse 5, 5401 Baden'),
('00000000-0000-4000-8000-000000000008','Benjamin Diener','Halter AG','Bauleitung',null,null,null);

insert into visits (project_id, date, title, participants, notes) values
('00000000-0000-4000-8000-000000000004','2026-08-13','Besprechung vor Ort',null,'Grundlage der Offerte, zusammen mit dem Prüfprotokoll Brandschutz EBP vom 24.06.2026.'),
('00000000-0000-4000-8000-000000000004','2026-10-26','Begehung vor Ort','Eldi Kaba, Fadil Fazliu','Befunde noch erfassen.'),
('00000000-0000-4000-8000-000000000002','2026-10-22','Begehung vor Ort','Erion, Swiss Brandschutz','Stahlträger aus Sicht Swiss Brandschutz brandschutztechnisch nicht korrekt, Verkleidung separat offerieren.'),
('00000000-0000-4000-8000-000000000006','2026-10-22','Begehung vor Ort','Erion, Swiss Brandschutz','Grundlage der Offerte Brandabschottungen.'),
('00000000-0000-4000-8000-000000000007',null,'Aufmass','Swiss Brandschutz','Aufmass Schaltgerätekombination erfolgt; Hauptträger ca. 25–30 m².');

insert into tasks (project_id, title, due, done) values
('00000000-0000-4000-8000-000000000001','Herrn Sörensen kontaktieren, Plan anfordern, Türtyp und Masse klären','2026-10-30',false),
('00000000-0000-4000-8000-000000000002','Offerte Stahlträger-Verkleidung erstellen',null,false),
('00000000-0000-4000-8000-000000000003','Offerte Brandschutztüren erstellen',null,false),
('00000000-0000-4000-8000-000000000004','Befunde der Begehung in Offerte einarbeiten',null,false),
('00000000-0000-4000-8000-000000000004','Offerte an E. Kaba senden',null,false),
('00000000-0000-4000-8000-000000000004','Begehung 26.10. durchführen','2026-10-26',true),
('00000000-0000-4000-8000-000000000005','Zahlungsplan auf 100 % ergänzen (30/20/20/10 ergibt 80 %)','2026-11-05',false),
('00000000-0000-4000-8000-000000000008','Offerte 2026-130 als Dokument ablegen',null,false);

insert into documents (project_id, name, url, date) values
('00000000-0000-4000-8000-000000000004','Offerte Jungholzstrasse 43','https://claude.ai/code/artifact/d714ca1d-1915-4239-ae1b-833cdd9721ca','2026-10-25'),
('00000000-0000-4000-8000-000000000005','Offerte Brandschutztüren Forelhaus','https://claude.ai/code/artifact/224f518d-6674-44d1-900b-0ce43e0a06a1','2026-10-19'),
('00000000-0000-4000-8000-000000000006','Offerte UW Steinen','https://claude.ai/code/artifact/6148a060-e025-4a46-8d5f-aa10326aa007','2026-10-23'),
('00000000-0000-4000-8000-000000000006','Offerte Brandabschottungen UW Steinen','https://claude.ai/code/artifact/443e78af-9ee2-425c-90d1-777348700f79','2026-10-21'),
('00000000-0000-4000-8000-000000000002','Besichtigung UW Steinen – Checkliste','https://claude.ai/code/artifact/6378c424-dcac-473d-a6c9-4c3e94be8652','2026-10-21'),
('00000000-0000-4000-8000-000000000007','Offerte Brandschutz KITA Baden','https://claude.ai/code/artifact/8c63ad5f-7106-4ced-9cfb-a6a9bb4c4692','2026-10-28');

insert into events (project_id, date, text) values
('00000000-0000-4000-8000-000000000001','2026-10-29','Anfrage über Website eingegangen'),
('00000000-0000-4000-8000-000000000002','2026-10-22','Begehung, Stahlträger als separate Offerte festgehalten'),
('00000000-0000-4000-8000-000000000003','2026-10-22','Anfrage SBB, Türen separat'),
('00000000-0000-4000-8000-000000000004','2026-06-24','Prüfprotokoll EBP erhalten, Projekt angelegt'),
('00000000-0000-4000-8000-000000000004','2026-08-13','Besprechung vor Ort'),
('00000000-0000-4000-8000-000000000004','2026-10-25','Offerte erstellt, CHF 73''750 netto'),
('00000000-0000-4000-8000-000000000004','2026-10-26','Begehung mit E. Kaba durchgeführt'),
('00000000-0000-4000-8000-000000000005','2026-10-19','Offerte erstellt, CHF 56''000 netto, gültig bis 30.11.2026'),
('00000000-0000-4000-8000-000000000006','2026-10-23','Offerte erstellt, CHF 26''450 netto'),
('00000000-0000-4000-8000-000000000007','2026-10-28','Offerte erstellt, CHF 17''990 netto'),
('00000000-0000-4000-8000-000000000008','2026-10-27','Offerte 2026-130 eingereicht');
