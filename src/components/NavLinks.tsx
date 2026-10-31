"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { Icon } from "./Icon";

const items = [
  { href: "/", label: "Projekte", icon: "board" },
  { href: "/aufgaben", label: "Aufgaben", icon: "tasks" },
  { href: "/kontakte", label: "Kontakte", icon: "people" },
  { href: "/begehungen", label: "Begehungen", icon: "calendar" },
];

export function NavLinks({ openTasks }: { openTasks: number }) {
  const path = usePathname();
  return (
    <div className="flex gap-0.5 overflow-x-auto lg:flex-col">
      {items.map((it) => {
        const active = it.href === "/" ? path === "/" || path.startsWith("/projekte") : path.startsWith(it.href);
        return (
          <Link
            key={it.href}
            href={it.href}
            aria-current={active ? "page" : undefined}
            className={`flex shrink-0 items-center gap-3 rounded-lg px-3 py-2.5 text-sm ${active ? "bg-night-2 text-white" : "text-[#C9C6C0] hover:bg-night-2 hover:text-white"}`}
          >
            <Icon name={it.icon} />
            {it.label}
            {it.icon === "tasks" && openTasks > 0 && (
              <span className="ml-auto rounded-full bg-brand px-2 text-[11px] font-semibold text-white">{openTasks}</span>
            )}
          </Link>
        );
      })}
    </div>
  );
}
