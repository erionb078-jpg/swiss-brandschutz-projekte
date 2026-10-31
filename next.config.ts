import type { NextConfig } from "next";

// Statische Seite: "npm run build" erzeugt den Ordner "out", der auf vercel.com/drop gezogen wird.
const nextConfig: NextConfig = {
  output: "export",
  trailingSlash: true,
  images: { unoptimized: true },
};

export default nextConfig;
