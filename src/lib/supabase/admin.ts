import { createClient } from "@supabase/supabase-js";

// Nur serverseitig verwenden (Website-Eingang). Umgeht Row Level Security.
export function createAdminClient() {
  return createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!, {
    auth: { persistSession: false },
  });
}
