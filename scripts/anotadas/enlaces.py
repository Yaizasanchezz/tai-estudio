"""Comprueba enlaces internos y anclas (#id) de todo dist/."""
import re, sys
from pathlib import Path
D = Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
ids = {}
pages = list(D.rglob("*.html"))
for p in pages:
    ids[p] = set(re.findall(r'\sid="([^"]+)"', p.read_text(errors="ignore")))
bad = []
for p in pages:
    for href in re.findall(r'href="(/[^"]*)"', p.read_text(errors="ignore")):
        path, _, frag = href.partition("#"); path = path.split("?")[0]
        t = D / path.lstrip("/")
        if t.is_dir() or path.endswith("/"): t = t / "index.html"
        if not t.exists(): bad.append(f"{p.relative_to(D)} -> {href} (no existe)"); continue
        if frag and t.suffix == ".html" and frag not in ids.get(t, set()): bad.append(f"{p.relative_to(D)} -> {href} (ancla)")
for b in sorted(set(bad))[:40]: print(b)
print(len(set(bad)), "enlaces rotos")
