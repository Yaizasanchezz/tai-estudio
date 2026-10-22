#!/usr/bin/env python3
"""Genera la web estática de TAI Estudio en la carpeta dist/.

Uso:
    python build.py            # genera dist/ con la ruta base /tai-estudio/
    SITE_BASE=/ python build.py  # para servirla desde la raíz

Solo necesita: markdown, jinja2 y pygments (pip install -r requirements.txt).
"""
from __future__ import annotations

import datetime as dt
import html
import json
import os
import re
import shutil
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markdown.extensions.toc import slugify_unicode
from pygments.formatters import HtmlFormatter

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
CONTENT = ROOT / "content"
DATA = ROOT / "data"
BASE = os.environ.get("SITE_BASE", "/tai-estudio/")
if not BASE.endswith("/"):
    BASE += "/"
BUILD_ID = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d%H%M%S")
TODAY = dt.date.today()

env = Environment(
    loader=FileSystemLoader(ROOT / "templates"),
    autoescape=select_autoescape(["html"]),
    trim_blocks=True,
    lstrip_blocks=True,
)

# ---------------------------------------------------------------- utilidades


def read_json(path: Path, default=None):
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return default


def write(rel: str, content: str | bytes) -> None:
    out = DIST / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, bytes):
        out.write_bytes(content)
    else:
        out.write_text(content, encoding="utf-8")


def front_matter(text: str) -> tuple[dict, str]:
    meta: dict = {}
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        head = text[4:end]
        text = text[end + 4:].lstrip("\n")
        for line in head.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                v = v.strip()
                if v.isdigit():
                    v = int(v)
                meta[k.strip()] = v
    return meta, text


def new_md() -> markdown.Markdown:
    return markdown.Markdown(
        extensions=[
            "extra",
            "sane_lists",
            "admonition",
            "codehilite",
            "toc",
        ],
        extension_configs={
            "codehilite": {"css_class": "highlight", "guess_lang": False},
            "toc": {"slugify": slugify_unicode, "toc_depth": "2-3"},
        },
        output_format="html5",
    )


def render_md(text: str) -> tuple[str, list]:
    text = text.replace("{{base}}", BASE)
    m = new_md()
    body = m.convert(text)
    body = wrap_tables(body)
    return body, m.toc_tokens


def inline_md(text: str) -> str:
    """Markdown de una frase o bloque corto (tests, flashcards)."""
    text = text.replace("{{base}}", BASE)
    out = markdown.markdown(text, extensions=["extra", "codehilite", "sane_lists"],
                            extension_configs={"codehilite": {"css_class": "highlight", "guess_lang": False}})
    # quitar <p> envolvente si es un único párrafo
    if out.startswith("<p>") and out.endswith("</p>") and out.count("<p>") == 1:
        out = out[3:-4]
    return out


def wrap_tables(body: str) -> str:
    return re.sub(r"(<table>.*?</table>)", r'<div class="table-wrap">\1</div>', body, flags=re.S)


TAG_RE = re.compile(r"<[^>]+>")


def strip_tags(s: str) -> str:
    return html.unescape(TAG_RE.sub(" ", s)).replace("\xa0", " ")


def squash(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


SEARCH: list[dict] = []


def index_html_sections(page_title: str, url: str, body: str, kind: str, limit: int = 700) -> None:
    """Divide el HTML por h2/h3 y añade cada sección al índice de búsqueda."""
    parts = re.split(r'(<h[23][^>]*id="[^"]+"[^>]*>.*?</h[23]>)', body, flags=re.S)
    current = {"s": "", "a": "", "x": ""}
    intro = parts[0]
    if squash(strip_tags(intro)):
        SEARCH.append({"t": page_title, "s": "", "u": url, "k": kind, "x": squash(strip_tags(intro))[:limit]})
    for i in range(1, len(parts), 2):
        h = parts[i]
        m = re.search(r'id="([^"]+)"', h)
        current = {
            "s": squash(strip_tags(h)),
            "a": m.group(1) if m else "",
        }
        text = squash(strip_tags(parts[i + 1] if i + 1 < len(parts) else ""))
        SEARCH.append({"t": page_title, "s": current["s"], "u": f"{url}#{current['a']}", "k": kind, "x": text[:limit]})


# ---------------------------------------------------------------- navegación

ICONS = {
    "home": '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M9.5 21v-6h5v6"/>',
    "book": '<path d="M4 19.5V5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2Z"/><path d="M4 19.5A2 2 0 0 0 6 22h13v-3"/><path d="M8 7h7"/>',
    "landmark": '<path d="M3 21h18"/><path d="M5 21V10"/><path d="M19 21V10"/><path d="M9 21V10"/><path d="M15 21V10"/><path d="M2 10 12 3l10 7Z"/>',
    "scale": '<path d="M12 3v18"/><path d="M7 21h10"/><path d="M5 7h14"/><path d="m5 7-3 7a3.5 3.5 0 0 0 6 0Z"/><path d="m19 7-3 7a3.5 3.5 0 0 0 6 0Z"/>',
    "check": '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="m8 12 3 3 5-6"/>',
    "briefcase": '<rect x="3" y="7" width="18" height="13" rx="3"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M3 13h18"/>',
    "file": '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9Z"/><path d="M14 3v6h6"/><path d="M8 13h8"/><path d="M8 17h5"/>',
    "cards": '<rect x="6" y="3" width="14" height="16" rx="3"/><path d="M4 7v12a2 2 0 0 0 2 2h10"/>',
    "play": '<rect x="2.5" y="5" width="19" height="14" rx="4"/><path d="m10 9 5 3-5 3Z"/>',
    "external": '<path d="M14 4h6v6"/><path d="M20 4 10 14"/><path d="M19 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h5"/>',
}

NAV = [
    {"label": "Inicio", "url": "", "icon": "home"},
    {"label": "Temario", "url": "temario/", "icon": "book"},
    {"label": "Constitución", "url": "constitucion/", "icon": "landmark"},
    {"label": "Leyes", "url": "leyes/", "icon": "scale"},
    {"label": "Tests", "url": "tests/", "icon": "check"},
    {"label": "Supuestos prácticos", "url": "supuestos/", "icon": "briefcase"},
    {"label": "Exámenes resueltos", "url": "examenes/", "icon": "file"},
    {"label": "Flashcards", "url": "flashcards/", "icon": "cards"},
    {"label": "YouTube", "url": "youtube/", "icon": "play"},
]
OPOSITATEST_URL = "https://www.opositatest.com/oposiciones/cuerpo-de-tecnicos-auxiliares-de-informatica-de-la-administracion-del-estado/test"


def icon(name: str, cls: str = "icon") -> str:
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


env.globals.update(base=BASE, nav=NAV, icon=icon, build_id=BUILD_ID,
                   opositatest_url=OPOSITATEST_URL, year=TODAY.year)


def render(template: str, rel_url: str, **ctx) -> None:
    """rel_url: ruta relativa sin base, terminada en / (o '' para la portada)."""
    tpl = env.get_template(template)
    active = ""
    for item in NAV:
        if item["url"] and rel_url.startswith(item["url"]):
            active = item["url"]
    if rel_url == "":
        active = ""
    html_out = tpl.render(rel_url=rel_url, active=active, **ctx)
    target = rel_url + "index.html" if rel_url.endswith("/") or rel_url == "" else rel_url
    write(target, html_out)


# ---------------------------------------------------------------- colecciones Markdown


def load_collection(folder: Path) -> list[dict]:
    pages = []
    for f in sorted(folder.glob("*.md")):
        meta, text = front_matter(f.read_text(encoding="utf-8"))
        body, toc = render_md(text)
        pages.append({"slug": f.stem, "meta": meta, "body": body, "toc": toc,
                      "title": meta.get("title", f.stem), "order": meta.get("order", 99)})
    pages.sort(key=lambda p: (p["order"], p["slug"]))
    return pages


def build_temario() -> list[dict]:
    pages = load_collection(CONTENT / "temario")
    for i, p in enumerate(pages):
        url = "temario/" if p["slug"] == "index" else f"temario/{p['slug']}/"
        p["url"] = url
    for i, p in enumerate(pages):
        prev_p = pages[i - 1] if i > 0 else None
        next_p = pages[i + 1] if i + 1 < len(pages) else None
        render("page.html", p["url"], page=p, section="Temario", section_url="temario/",
               siblings=pages, prev=prev_p, next=next_p, studied_key=f"temario/{p['slug']}")
        index_html_sections(p["title"], BASE + p["url"], p["body"], "Temario")
    return pages


def boe_law(boe_id: str) -> dict | None:
    return read_json(DATA / "boe" / f"{boe_id}.json")


def law_toc(law: dict) -> list[dict]:
    """Índice a partir de los bloques: encabezados (títulos, capítulos) y artículos."""
    toc = []
    for b in law.get("bloques", []):
        if b["tipo"] in ("encabezado", "precepto", "parte_final", "preambulo"):
            toc.append({"id": b["id"], "titulo": b["titulo"], "tipo": b["tipo"]})
    return toc


def render_law_text(law_meta: dict, url: str, explained_url: str | None) -> None:
    data = boe_law(law_meta["id"]) if law_meta.get("id") else None
    if data:
        for b in data.get("bloques", []):
            if b["tipo"] == "precepto":
                SEARCH.append({"t": f"{law_meta['corto']} (texto oficial)", "s": b["titulo"],
                               "u": f"{BASE}{url}#{b['id']}", "k": "Texto oficial",
                               "x": squash(strip_tags(b["html"]))[:260]})
    render("ley_texto.html", url, law=law_meta, data=data, toc=law_toc(data) if data else [],
           explained_url=explained_url,
           boe_url=f"https://www.boe.es/buscar/act.php?id={law_meta['id']}" if law_meta.get("id") else law_meta.get("url"))


def build_constitucion(leyes: list[dict]) -> list[dict]:
    pages = load_collection(CONTENT / "constitucion")
    ce = next(l for l in leyes if l["slug"] == "constitucion")
    for p in pages:
        p["url"] = f"constitucion/explicada/{p['slug']}/"
    for i, p in enumerate(pages):
        render("page.html", p["url"], page=p, section="Constitución explicada", section_url="constitucion/",
               siblings=pages, prev=pages[i - 1] if i else None,
               next=pages[i + 1] if i + 1 < len(pages) else None,
               studied_key=f"ce/{p['slug']}", official_url="constitucion/texto/")
        index_html_sections(f"Constitución explicada · {p['title']}", BASE + p["url"], p["body"], "Constitución")
    render("constitucion.html", "constitucion/", pages=pages, ce=ce, data=boe_law(ce["id"]))
    render_law_text(ce, "constitucion/texto/", "constitucion/")
    return pages


def build_leyes(leyes: list[dict]) -> None:
    explained = {p["slug"]: p for p in load_collection(CONTENT / "leyes")}
    groups: dict[str, list] = {}
    for law in leyes:
        if law["slug"] == "constitucion":
            continue
        groups.setdefault(law.get("grupo", "Otras"), []).append(law)
        exp = explained.get(law.get("explicada", law["slug"]))
        law["has_explained"] = exp is not None
        law["has_text"] = bool(law.get("id")) and boe_law(law["id"]) is not None
        law["exp_url"] = f"leyes/{law.get('explicada', law['slug'])}/" if exp else None
        law["text_url"] = f"leyes/{law['slug']}/texto/" if law.get("id") else None
    # páginas explicadas (una explicación puede cubrir varias normas)
    for slug, p in explained.items():
        related = [l for l in leyes if l.get("explicada", l["slug"]) == slug]
        p["url"] = f"leyes/{slug}/"
        render("page.html", p["url"], page=p, section="Leyes explicadas", section_url="leyes/",
               siblings=None, prev=None, next=None, studied_key=f"leyes/{slug}", related=related)
        index_html_sections(f"{p['title']}", BASE + p["url"], p["body"], "Leyes")
    for law in leyes:
        if law["slug"] == "constitucion" or not law.get("id"):
            continue
        render_law_text(law, law["text_url"], law["exp_url"])
    render("leyes.html", "leyes/", groups=groups)


def build_examenes() -> None:
    folder = DATA / "examenes"
    exams = []
    for f in sorted(folder.glob("*.json")):
        ex = read_json(f)
        for parte in ex.get("partes", []):
            for q in parte.get("preguntas", []):
                q["explicacion_html"] = inline_md(q.get("explicacion", ""))
        exams.append(ex)
    exams.sort(key=lambda e: e.get("orden", 99))
    for ex in exams:
        url = f"examenes/{ex['slug']}/"
        ex["url"] = url
        render("examen.html", url, ex=ex)
        for parte in ex.get("partes", []):
            for q in parte.get("preguntas", []):
                SEARCH.append({"t": ex["titulo"], "s": f"{parte['titulo']} · pregunta {q['n']}: {q.get('tema', '')}",
                               "u": f"{BASE}{url}#{parte['id']}-{q['n']}", "k": "Exámenes",
                               "x": squash(strip_tags(q["explicacion_html"]))[:300]})
    render("examenes.html", "examenes/", exams=exams)


def build_data_pages() -> None:
    tests = read_json(DATA / "tests.json", {"preguntas": []})
    for q in tests["preguntas"]:
        q["pregunta"] = inline_md(q["pregunta"])
        q["opciones"] = [inline_md(o) for o in q["opciones"]]
        q["explicacion"] = inline_md(q["explicacion"])
    write("data/tests.json", json.dumps(tests, ensure_ascii=False))

    sup = read_json(DATA / "supuestos.json", {"supuestos": []})
    for s in sup["supuestos"]:
        s["enunciado"] = render_md(s["enunciado"])[0]
        for q in s["preguntas"]:
            q["pregunta"] = inline_md(q["pregunta"])
            q["opciones"] = [inline_md(o) for o in q["opciones"]]
            q["explicacion"] = inline_md(q["explicacion"])
    write("data/supuestos.json", json.dumps(sup, ensure_ascii=False))

    fc = read_json(DATA / "flashcards.json", {"mazos": []})
    total_cards = 0
    for deck in fc["mazos"]:
        for c in deck["tarjetas"]:
            c["f"] = inline_md(c["f"])
            c["b"] = inline_md(c["b"])
        total_cards += len(deck["tarjetas"])
    write("data/flashcards.json", json.dumps(fc, ensure_ascii=False))

    bloques = {
        "constitucion": "Constitución", "leyes": "Leyes y Admin. electrónica",
        "tecnologia": "Tecnología básica", "desarrollo": "Desarrollo", "sistemas": "Sistemas y redes",
    }
    counts = {k: sum(1 for q in tests["preguntas"] if q["bloque"] == k) for k in bloques}
    render("tests.html", "tests/", bloques=bloques, counts=counts, total=len(tests["preguntas"]))
    render("supuestos.html", "supuestos/", supuestos=sup["supuestos"])
    render("flashcards.html", "flashcards/", mazos=fc["mazos"], total=total_cards)

    yt = read_json(DATA / "youtube.json", {"categorias": []})
    render("youtube.html", "youtube/", categorias=yt["categorias"])
    return len(tests["preguntas"]), total_cards


# ---------------------------------------------------------------- estáticos y PWA


def copy_static() -> None:
    shutil.copytree(ROOT / "static", DIST / "static", dirs_exist_ok=True)
    light = HtmlFormatter(style="friendly").get_style_defs(":root .highlight")
    dark = HtmlFormatter(style="dracula").get_style_defs('[data-theme="dark"] .highlight')
    write("static/css/pygments.css", light + "\n" + dark +
          '\n:root .highlight, [data-theme="dark"] .highlight { background: var(--code-bg) !important; }\n')


def build_pwa() -> None:
    manifest = {
        "name": "TAI Estudio",
        "short_name": "TAI Estudio",
        "description": "Temario, Constitución, leyes, tests, supuestos y flashcards para la oposición TAI.",
        "start_url": BASE,
        "scope": BASE,
        "display": "standalone",
        "background_color": "#fff7fa",
        "theme_color": "#d6457c",
        "lang": "es",
        "icons": [
            {"src": f"{BASE}static/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": f"{BASE}static/img/icon-512.png", "sizes": "512x512", "type": "image/png"},
            {"src": f"{BASE}static/img/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        ],
    }
    write("manifest.webmanifest", json.dumps(manifest, ensure_ascii=False, indent=1))
    sw = (ROOT / "templates" / "sw.js").read_text(encoding="utf-8")
    sw = sw.replace("__BUILD_ID__", BUILD_ID).replace("__BASE__", BASE)
    write("sw.js", sw)


# ---------------------------------------------------------------- main


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    leyes = read_json(DATA / "leyes.json", {"leyes": []})["leyes"]

    temario = build_temario()
    ce_pages = build_constitucion(leyes)
    build_leyes(leyes)
    build_examenes()
    n_tests, n_cards = build_data_pages()

    render("home.html", "", temario=temario, ce_pages=ce_pages, n_tests=n_tests, n_cards=n_cards)
    render("404.html", "404.html")
    copy_static()
    build_pwa()
    write("search.json", json.dumps(SEARCH, ensure_ascii=False))
    write(".nojekyll", "")
    n_pages = len(list(DIST.rglob("*.html")))
    print(f"OK · {n_pages} páginas · {len(SEARCH)} entradas de búsqueda · base {BASE}")


if __name__ == "__main__":
    main()
