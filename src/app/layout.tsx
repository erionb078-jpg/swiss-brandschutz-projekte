import type { Metadata } from "next";
import "@fontsource/archivo/600.css";
import "@fontsource/archivo/800.css";
import "@fontsource/public-sans/400.css";
import "@fontsource/public-sans/500.css";
import "@fontsource/public-sans/600.css";
import "./globals.css";

export const metadata: Metadata = {
  title: "Swiss Brandschutz · Projekte",
  robots: { index: false, follow: false },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="de-CH">
      <body className="font-sans antialiased">{children}</body>
    </html>
  );
}
