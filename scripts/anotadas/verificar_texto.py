"""Comprueba que el texto oficial que muestran las páginas anotadas es idéntico al del BOE.
Compara, artículo por artículo, el texto visible (sin etiquetas) con el bloque del BOE."""
import json, re, sys, glob, html
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
leyes = {l["slug"]: l for l in json.load(open(ROOT / "data/leyes.json"))["leyes"]}
def norm(h):
    h = re.sub(r"</?(strong|em|b|i|span|a|sup|sub)\b[^>]*>", "", h)
    h = re.sub(r"<[^>]+>", " ", h)
    return re.sub(r"\s+", " ", html.unescape(h)).strip()
def front(p):
    s = p.read_text(); m = re.match(r"^---\n(.*?)\n---\n", s, re.S)
    return dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), re.M)) if m else {}
bad = total = 0
for md in sorted(list((ROOT / "content/constitucion").glob("*.md")) + list((ROOT / "content/leyes").glob("*.md"))):
    meta = front(md)
    if "texto" not in meta: continue
    url = ("constitucion/explicada/" if md.parent.name == "constitucion" else "leyes/") + md.stem + "/index.html"
    page = (ROOT / "dist" / url).read_text()
    slugs = [s.strip() for s in meta["texto"].split(",")]
    for slug in slugs:
        law = leyes[slug]
        if not law.get("id"): continue
        data = json.load(open(ROOT / f"data/boe/{law['id']}.json"))
        for b in data["bloques"]:
            if b["tipo"] not in ("precepto", "preambulo"): continue
            if b["tipo"] == "preambulo" and not meta.get("rango", "").startswith("preambulo"): continue
            hid = b["id"] if len(slugs) == 1 else f"{slug}-{b['id']}"
            m = re.search(r'id="%s"[^>]*>.*?</h3>\s*<div class="oficial">(.*?)</div>\s*(?=<div class="nota|<h[23]|<details|</details|$)' % re.escape(hid), page, re.S)
            if not m:
                if meta.get("rango"): continue   # fuera del rango de esta página
                print(f"FALTA  {md.stem}: {slug} {b['id']}"); bad += 1; continue
            total += 1
            want = norm(re.sub(r'^\s*<p class="articulo">.*?</p>', "", b["html"], count=1, flags=re.S))
            got = norm(m.group(1))
            if want != got:
                bad += 1; print(f"DISTINTO {md.stem}: {slug} {b['id']}\n  BOE: {want[:200]}\n  WEB: {got[:200]}")
print(f"{total} preceptos comprobados, {bad} con diferencias o ausentes")
sys.exit(1 if bad else 0)
