"""Перевірка vault: frontmatter, цілісність wiki-посилань, досяжність із MOC."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"Templates", "scripts", ".git"}
LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
TYPES = {"concept", "component", "decision", "glossary", "moc"}


def notes():
    return {p.stem: p for p in ROOT.rglob("*.md")
            if not (set(p.relative_to(ROOT).parts) & SKIP) and p.name != "README.md"}


def main():
    ns = notes()
    errors, graph = [], {}
    for name, p in ns.items():
        text = p.read_text(encoding="utf-8")
        m = re.match(r"---\n(.*?)\n---\n", text, re.S)
        if not m:
            errors.append(f"{name}: немає frontmatter")
            continue
        fm = dict(l.split(": ", 1) for l in m.group(1).splitlines() if ": " in l)
        if fm.get("type") not in TYPES:
            errors.append(f"{name}: невідомий type {fm.get('type')!r}")
        if "created" not in fm or "tags" not in fm:
            errors.append(f"{name}: бракує created/tags")
        targets = {t.strip() for t in LINK.findall(text)}
        graph[name] = targets
        for t in targets:
            if t not in ns:
                errors.append(f"{name}: непрацююче посилання [[{t}]]")
    seen, stack = set(), ["MOC-Застосунок"]
    while stack:
        n = stack.pop()
        if n in seen or n not in graph:
            continue
        seen.add(n)
        stack.extend(graph[n])
    for n in ns:
        if n not in seen:
            errors.append(f"{n}: недосяжна з MOC")
    print(f"нотаток: {len(ns)}, досяжних з MOC: {len(seen & set(ns))}")
    for e in errors:
        print("ПОМИЛКА:", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
