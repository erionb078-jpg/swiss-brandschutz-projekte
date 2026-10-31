"use client";

import { createClient, type SupabaseClient } from "@supabase/supabase-js";

// Diese beiden Werte sind öffentlich (für den Browser gedacht). Geschützt wird alles durch Login + Row Level Security.
export const SUPABASE_URL = process.env.NEXT_PUBLIC_SUPABASE_URL ?? "";
export const SUPABASE_ANON_KEY = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY ?? "";

let client: SupabaseClient | null = null;
export function sb() {
  if (!client) client = createClient(SUPABASE_URL || "https://invalid.supabase.co", SUPABASE_ANON_KEY || "missing", { auth: { persistSession: true } });
  return client;
}
