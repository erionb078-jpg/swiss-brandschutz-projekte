-- Swiss Brandschutz Projekte – Datenbank
-- In Supabase: SQL Editor → New query → diesen Inhalt einfügen → Run

create extension if not exists pgcrypto;

create table if not exists projects (
  id uuid primary key default gen_random_uuid(),
  title text not null,
  location text,
  client_company text,
  services text[] not null default '{}',
  description text,
  status text not null default 'anfrage'
    check (status in ('anfrage','abklaerung','offerte','versendet','auftrag','absage')),
  amount_net numeric(12,2),
  offer_ref text,
  offer_date date,
  valid_until date,
  follow_up date,
  source text,
  owner text,
  position integer not null default 0,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists contacts (
  id uuid primary key default gen_random_uuid(),
  project_id uuid references projects(id) on delete cascade,
  name text not null,
  company text,
  role text,
  phone text,
  email text,
  address text,
  created_at timestamptz not null default now()
);

create table if not exists visits (
  id uuid primary key default gen_random_uuid(),
  project_id uuid not null references projects(id) on delete cascade,
  date date,
  title text not null default 'Begehung vor Ort',
  participants text,
  notes text,
  created_at timestamptz not null default now()
);

create table if not exists tasks (
  id uuid primary key default gen_random_uuid(),
  project_id uuid not null references projects(id) on delete cascade,
  title text not null,
  due date,
  done boolean not null default false,
  created_at timestamptz not null default now()
);

create table if not exists documents (
  id uuid primary key default gen_random_uuid(),
  project_id uuid not null references projects(id) on delete cascade,
  name text not null,
  url text not null,
  date date,
  created_at timestamptz not null default now()
);

create table if not exists events (
  id uuid primary key default gen_random_uuid(),
  project_id uuid not null references projects(id) on delete cascade,
  date date not null default current_date,
  text text not null,
  created_at timestamptz not null default now()
);

create index if not exists contacts_project_idx on contacts(project_id);
create index if not exists visits_project_idx on visits(project_id);
create index if not exists tasks_project_idx on tasks(project_id);
create index if not exists documents_project_idx on documents(project_id);
create index if not exists events_project_idx on events(project_id);

create or replace function set_updated_at() returns trigger language plpgsql as $$
begin new.updated_at = now(); return new; end $$;

drop trigger if exists projects_updated_at on projects;
create trigger projects_updated_at before update on projects
  for each row execute function set_updated_at();

-- Zugriff: nur angemeldete Benutzer (Erion, Fadil, …) sehen und bearbeiten alles.
alter table projects enable row level security;
alter table contacts enable row level security;
alter table visits enable row level security;
alter table tasks enable row level security;
alter table documents enable row level security;
alter table events enable row level security;

do $$
declare t text;
begin
  foreach t in array array['projects','contacts','visits','tasks','documents','events'] loop
    execute format('drop policy if exists "team_all" on %I', t);
    execute format('create policy "team_all" on %I for all to authenticated using (true) with check (true)', t);
  end loop;
end $$;
