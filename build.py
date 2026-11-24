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
                if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                    v = v[1:-1]
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
    # en las páginas anotadas, el texto oficial ya se indexa en su página de texto oficial
    body = re.sub(r'<div class="oficial">.*?</div>', "", body, flags=re.S)
    body = re.sub(r'<div class="preg".*?</details></div>', "", body, flags=re.S)
    body = re.sub(r'<details class="oficial-final">.*?</details>', "", body, flags=re.S)
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
        if not text and 'class="oficial-h' in h:
            continue
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
    "brain": '<path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 3 3h1V4Z"/><path d="M15 4a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-3 3h-1V4Z"/>',
    "grid": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M3 9h18M3 15h18M9 3v18M15 3v18"/>',
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
NAV_AUX = [
    {"label": "Inicio", "url": "auxiliar/", "icon": "home"},
    {"label": "Temario", "url": "auxiliar/temario/", "icon": "book"},
    {"label": "Constitución", "url": "constitucion/", "icon": "landmark"},
    {"label": "Leyes", "url": "leyes/", "icon": "scale"},
    {"label": "Tests", "url": "auxiliar/tests/", "icon": "check"},
    {"label": "Psicotécnicos", "url": "auxiliar/psicotecnicos/", "icon": "brain"},
    {"label": "Ofimática práctica", "url": "auxiliar/ofimatica/", "icon": "grid"},
    {"label": "Exámenes resueltos", "url": "auxiliar/examenes/", "icon": "file"},
    {"label": "Flashcards", "url": "auxiliar/flashcards/", "icon": "cards"},
    {"label": "YouTube", "url": "auxiliar/youtube/", "icon": "play"},
]
NAV_ADM = [
    {"label": "Inicio", "url": "administrativo/", "icon": "home"},
    {"label": "Temario", "url": "administrativo/temario/", "icon": "book"},
    {"label": "Constitución", "url": "constitucion/", "icon": "landmark"},
    {"label": "Leyes", "url": "leyes/", "icon": "scale"},
    {"label": "Tests", "url": "administrativo/tests/", "icon": "check"},
    {"label": "Ofimática práctica", "url": "administrativo/ofimatica/", "icon": "grid"},
    {"label": "Exámenes resueltos", "url": "administrativo/examenes/", "icon": "file"},
    {"label": "Flashcards", "url": "administrativo/flashcards/", "icon": "cards"},
    {"label": "YouTube", "url": "administrativo/youtube/", "icon": "play"},
]
OPOSITATEST_URL = "https://www.opositatest.com/oposiciones/cuerpo-de-tecnicos-auxiliares-de-informatica-de-la-administracion-del-estado/test"
OPOSITATEST_AUX_URL = "https://www.opositatest.com/oposiciones/auxiliares-administrativos/test"
OPOSITATEST_ADM_URL = "https://www.opositatest.com/oposiciones/administrativos-del-estado-turno-libre/test"

# Rutas compartidas por las dos oposiciones (el menú lateral depende de la elegida).
SHARED_PREFIXES = ("constitucion/", "leyes/")


def icon(name: str, cls: str = "icon") -> str:
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


env.globals.update(base=BASE, nav=NAV, nav_aux=NAV_AUX, nav_adm=NAV_ADM, icon=icon, build_id=BUILD_ID,
                   opositatest_url=OPOSITATEST_URL, opositatest_aux_url=OPOSITATEST_AUX_URL,
                   opositatest_adm_url=OPOSITATEST_ADM_URL, year=TODAY.year)


def opo_of(rel_url: str) -> str:
    if rel_url.startswith("auxiliar/"):
        return "aux"
    if rel_url.startswith("administrativo/"):
        return "adm"
    if rel_url.startswith(SHARED_PREFIXES):
        return "shared"
    return "tai"


def active_in(nav: list[dict], rel_url: str) -> str:
    active = ""
    for item in nav:
        if item["url"] and rel_url.startswith(item["url"]) and len(item["url"]) > len(active):
            active = item["url"]
    return active


def render(template: str, rel_url: str, **ctx) -> None:
    """rel_url: ruta relativa sin base, terminada en / (o '' para la portada)."""
    tpl = env.get_template(template)
    active = "" if rel_url == "" else active_in(NAV, rel_url)
    active_aux = active_in(NAV_AUX, rel_url)
    active_adm = active_in(NAV_ADM, rel_url)
    opo = opo_of(rel_url)
    ctx.setdefault("brand", {"aux": "Auxiliar", "adm": "Administrativo", "shared": "Opo"}.get(opo, "TAI"))
    html_out = tpl.render(rel_url=rel_url, active=active, active_aux=active_aux, active_adm=active_adm, opo=opo, **ctx)
    target = rel_url + "index.html" if rel_url.endswith("/") or rel_url == "" else rel_url
    write(target, html_out)


# ---------------------------------------------------------------- colecciones Markdown


def load_collection(folder: Path) -> list[dict]:
    pages = []
    for f in sorted(folder.glob("*.md")):
        meta, text = front_matter(f.read_text(encoding="utf-8"))
        if meta.get("texto"):
            text = compose_annotated(meta, text, f"{folder.name}/{f.stem}")
        body, toc = render_md(text)
        pages.append({"slug": f.stem, "meta": meta, "body": body, "toc": toc,
                      "title": meta.get("title", f.stem), "order": float(meta.get("order", 99))})
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
    data = read_json(DATA / "boe" / f"{boe_id}.json")
    if data:
        # Las imágenes del BOE vienen con rutas relativas a boe.es.
        for b in data.get("bloques", data.get("blocks", [])) if isinstance(data, dict) else []:
            if isinstance(b, dict) and "html" in b:
                b["html"] = b["html"].replace('src="/datos/', 'src="https://www.boe.es/datos/')
    return data


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


# ---------------------------------------------------------------------------
# Páginas anotadas: texto oficial del BOE (en negro) + notas propias (en rojo)
# ---------------------------------------------------------------------------
# Formato del .md (front matter `texto: slug[, slug…]` y opcional `rango: a30-a55`):
#   texto libre al principio            -> nota de introducción
#   <!-- a30 -->                        -> nota después del art. 30 (de la primera norma)
#   <!-- antes a39 -->                  -> nota antes del art. 39 (tras el encabezado anterior)
#   <!-- lopdgdd:a5 -->                 -> nota del art. 5 de otra norma de la página
#   <!-- antes lo-3-1981:inicio -->     -> nota antes del texto de una norma
#   <!-- final -->                      -> nota al final de la página
#   <!-- titulo a30: Defensa de España --> etiqueta propia junto al título del artículo
#   <!-- destacar a31: frase | frase --> frases del texto oficial que se resaltan en negrita
NOTE_RE = re.compile(r"^<!--\s*(antes\s+)?((?:[a-z0-9-]+:)?[a-z0-9-]+)\s*-->\s*$")
META_RE = re.compile(r"^<!--\s*(titulo|destacar)\s+((?:[a-z0-9-]+:)?[a-z0-9-]+)\s*:\s*(.*?)\s*-->\s*$")
LAWS_BY_SLUG: dict[str, dict] = {}


def parse_annotations(text: str, default_law: str) -> tuple[dict, dict, dict]:
    notes: dict[tuple, list[str]] = {}
    titles: dict[tuple, str] = {}
    marks: dict[tuple, list[str]] = {}
    key = (default_law, "intro", False)
    buf: list[str] = []

    def flush():
        body = "\n".join(buf).strip()
        if body:
            notes.setdefault(key, []).append(body)
        buf.clear()

    def k(ref):
        law, _, bid = ref.rpartition(":")
        return law or default_law, bid

    for line in text.splitlines():
        m = META_RE.match(line.strip())
        if m:
            law, bid = k(m.group(2))
            if m.group(1) == "titulo":
                titles[(law, bid)] = m.group(3)
            else:
                marks[(law, bid)] = [x.strip() for x in m.group(3).split("|") if x.strip()]
            continue
        m = NOTE_RE.match(line.strip())
        if m and not line.strip().startswith("<!-- include"):
            flush()
            law, bid = k(m.group(2))
            key = (law, bid, bool(m.group(1)))
            continue
        buf.append(line)
    flush()
    return notes, titles, marks


def note_md(parts: list[str], cls: str = "") -> str:
    body = "\n\n".join(parts)
    # los encabezados de las notas no entran en el índice de la página
    body = re.sub(r"(?m)^#{2,3} ", "#### ", body)
    return f'\n\n<div class="nota{(" " + cls) if cls else ""}" markdown="1">\n\n{body}\n\n</div>\n\n'


def heading_text(html: str) -> str:
    parts = [squash(strip_tags(x)) for x in re.findall(r"<p[^>]*>(.*?)</p>", html, flags=re.S)]
    return " · ".join(p for p in parts if p)


def emphasize(html: str, phrases: list[str]) -> str:
    for ph in phrases:
        i = html.find(ph)
        if i >= 0:
            html = html[:i] + "<strong>" + ph + "</strong>" + html[i + len(ph):]
    return html


EXAM_NAMES = {"tai-libre": "TAI", "aux-libre": "Auxiliar", "adm-libre": "Administrativo"}
_EXAMS: dict = {}


def exam_question(ref: dict) -> dict:
    """Busca una pregunta real (examen, parte, n) en data/**/examenes."""
    if not _EXAMS:
        for f in list((DATA / "examenes").glob("*.json")) + list(DATA.glob("*/examenes/*.json")):
            d = json.loads(f.read_text(encoding="utf-8"))
            _EXAMS[d["slug"]] = d
    d = _EXAMS[ref["examen"]]
    parte = next(p for p in d["partes"] if p["id"] == ref["parte"])
    q = next(x for x in parte["preguntas"] if str(x["n"]) == str(ref["n"]))
    m = re.match(r"([a-z]+-libre)-(\d{4})(-extraordinario)?", d["slug"])
    name = f'{EXAM_NAMES.get(m.group(1), m.group(1))} {m.group(2)}{" (extraordinario)" if m.group(3) else ""}'
    where = parte["titulo"].lower()
    origen = f"Cayó en el examen de {name} · {where}, pregunta {q['n']}"
    return {"pregunta": q["pregunta"], "opciones": q["opciones"], "respuesta": q["respuesta"],
            "explicacion": q.get("explicacion", ""), "origen": origen,
            "url": f'{BASE}{ {"aux-libre": "auxiliar/", "adm-libre": "administrativo/"}.get(m.group(1), "") }examenes/{d["slug"]}/'}


def load_preguntas(page: str, default_slug: str) -> dict:
    f = DATA / "preguntas" / f"{page}.json"
    if not f.exists():
        return {}
    raw = json.loads(f.read_text(encoding="utf-8"))
    out: dict = {}
    for key, lst in raw.items():
        slug, bid = key.split(":", 1) if ":" in key else (default_slug, key)
        out[(slug, bid)] = [exam_question(q) if "examen" in q else q for q in lst]
    return out


def _md_inline(t: str) -> str:
    h = inline_md(t).strip()
    return re.sub(r"^<p>(.*)</p>$", r"\1", h, flags=re.S)


def preg_html(qs: list[dict]) -> str:
    out = []
    for q in qs:
        ok = "abcd".index(q["respuesta"])
        if q.get("origen"):
            tag = f'<p class="preg-tag preg-real"><a href="{q["url"]}">{html.escape(q["origen"])}</a></p>' if q.get("url") else f'<p class="preg-tag preg-real">{html.escape(q["origen"])}</p>'
        else:
            tag = '<p class="preg-tag">Pregunta tipo examen</p>'
        ops = "".join(f'<li><button type="button" class="preg-op" data-k="{i}"><span class="preg-l">{"abcd"[i]})</span> {_md_inline(o)}</button></li>' for i, o in enumerate(q["opciones"]))
        out.append(f'\n\n<div class="preg" data-ok="{ok}">{tag}<div class="preg-q">{_md_inline(q["pregunta"])}</div>'
                   f'<ol class="preg-ops">{ops}</ol><details class="preg-sol"><summary>Ver respuesta</summary>'
                   f'<p><strong>Correcta: {q["respuesta"]})</strong></p>{inline_md(q.get("explicacion", ""))}</details></div>\n\n')
    return "".join(out)


def compose_annotated(meta: dict, text: str, page: str = "") -> str:
    """Devuelve el markdown completo de una página anotada."""
    slugs = [x.strip() for x in str(meta["texto"]).split(",") if x.strip()]
    notes, titles, marks = parse_annotations(text, slugs[0])
    used = set()
    pregs = load_preguntas(page, slugs[0])
    pused = set()

    def quiz(law, bid):
        if (law, bid) in pregs:
            pused.add((law, bid))
            return preg_html(pregs[(law, bid)])
        return ""

    def take(law, bid, before):
        key = (law, bid, before)
        used.add(key)
        return notes.get(key, [])

    out = []
    intro = take(slugs[0], "intro", False)
    if intro:
        out.append(note_md(intro, "nota-intro"))
    rng = str(meta.get("rango", "")).split("-", 1) if meta.get("rango") else None
    for slug in slugs:
        law = LAWS_BY_SLUG[slug]
        data = boe_law(law["id"]) if law.get("id") else None
        if len(slugs) > 1:
            out.append(f'\n\n## {law["nombre"]} {{#{slug}}}\n\n')
        if take(slug, "inicio", True):
            out.append(note_md(notes[(slug, "inicio", True)]))
        if not data:
            out.append(f'\n\n<p class="oficial-falta">Esta norma no se publica en el BOE (es europea): su texto oficial está en <a href="{law.get("url", "")}" target="_blank" rel="noopener">EUR-Lex ↗</a>. Abajo, las explicaciones.</p>\n\n')
            rest = [k for k in notes if k[0] == slug and k not in used]
            for i, key in enumerate(rest):
                last = not any(k[:2] == key[:2] for k in rest[i + 1:])
                out.append(note_md(take(*key)) + (quiz(key[0], key[1]) if last else ""))
            continue
        blocks = [b for b in data["bloques"] if b["tipo"] in ("encabezado", "precepto", "preambulo")]
        if not rng or rng[0] != "preambulo":
            blocks = [b for b in blocks if b["tipo"] != "preambulo"]
        if rng:
            ids = [b["id"] for b in blocks]
            a, z = ids.index(rng[0]), ids.index(rng[1])
            blocks = blocks[a:z + 1]
        finals: list[str] = []
        in_final = False
        for b in blocks:
            bid = b["id"]
            is_art = b["tipo"] == "precepto"
            noted = any((slug, bid, x) in notes for x in (True, False)) or (slug, bid) in pregs
            if is_art and not bid.startswith("a") and not rng and not noted:
                in_final = True
            pre = take(slug, bid, True)
            if b["tipo"] == "encabezado":
                level = "##" if re.match(r"(TÍTULO|LIBRO|PARTE)", b.get("titulo") or "") or len(slugs) == 1 else "###"
                if len(slugs) > 1:
                    level = "###"
                hid = bid if len(slugs) == 1 else f"{slug}-{bid}"
                chunk = f'\n\n{level} {heading_text(b["html"])} {{#{hid} .oficial-h}}\n\n'
                chunk += note_md(pre) if pre else ""
                chunk += note_md(take(slug, bid, False)) if (slug, bid, False) in notes else ""
                chunk += quiz(slug, bid)
                out.append(chunk)
                continue
            body = re.sub(r'^\s*<p class="articulo">.*?</p>', "", b["html"], count=1, flags=re.S)
            body = emphasize(body, marks.get((slug, bid), []))
            label = titles.get((slug, bid))
            head_txt = squash(strip_tags(re.search(r'<p class="articulo">(.*?)</p>', b["html"], flags=re.S).group(1))) if '<p class="articulo">' in b["html"] else (b["titulo"] or ("Preámbulo" if b["tipo"] == "preambulo" else ""))
            lab = f' <span class="nota-label">{label}</span>' if label else ""
            hid = bid if len(slugs) == 1 else f"{slug}-{bid}"
            chunk = ""
            if pre:
                chunk += note_md(pre)
            chunk += f'\n\n### {head_txt}{lab} {{#{hid} .oficial-h}}\n\n<div class="oficial">\n{body}\n</div>\n\n'
            after = take(slug, bid, False)
            if after:
                chunk += note_md(after)
            chunk += quiz(slug, bid)
            (finals if in_final and not noted else out).append(chunk)
        if finals:
            out.append('\n\n<details class="oficial-final" markdown="1">\n<summary>Disposiciones adicionales, transitorias, derogatorias y finales (texto oficial)</summary>\n\n' + "".join(finals) + "\n\n</details>\n\n")
    final = take(slugs[0], "final", False)
    if final:
        out.append(note_md(final, "nota-final"))
    left = [k for k in notes if k not in used]
    if left:
        raise SystemExit(f"Notas sin destino en {meta.get('title')}: {left[:5]}")
    pleft = [k for k in pregs if k not in pused]
    if pleft:
        raise SystemExit(f"Preguntas sin destino en {meta.get('title')}: {pleft[:5]}")
    return "".join(out)


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
        exp = explained.get(law.get("explicada", law["slug"])) if law.get("explicada", law["slug"]) else None
        law["has_explained"] = exp is not None
        law["has_text"] = bool(law.get("id")) and boe_law(law["id"]) is not None
        law["exp_url"] = f"leyes/{law.get('explicada', law['slug'])}/" if exp else None
        if law.get("explicada_url"):  # explicada en el temario de Auxiliar
            law["has_explained"] = True
            law["exp_url"] = law["explicada_url"]
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
        ex["notas_html"] = inline_md(ex.get("notas", "")) if ex.get("notas") else ""
        for parte in ex.get("partes", []):
            parte["descripcion_html"] = wrap_tables(inline_md(parte.get("descripcion", ""))) if parte.get("descripcion") else ""
            for q in parte.get("preguntas", []):
                q["explicacion_html"] = wrap_tables(inline_md(q.get("explicacion", "")))
                q["pregunta_html"] = wrap_tables(inline_md(q.get("pregunta", "")))
                q["opciones"] = [inline_md(o) for o in q.get("opciones", [])]
        exams.append(ex)
    exams.sort(key=lambda e: e.get("orden", 99))
    for ex in exams:
        url = f"examenes/{ex['slug']}/"
        ex["url"] = url
        render("examen.html", url, ex=ex)
        for parte in ex.get("partes", []):
            for q in parte.get("preguntas", []):
                SEARCH.append({"t": ex["titulo"], "s": f"{parte['titulo']} · pregunta {q['n']}: {q.get('tema', '')} · {q.get('pregunta', '')}",
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


# ---------------------------------------------------------------- Auxiliar Administrativo del Estado

AUX = DATA / "aux"
AUX_HOME = "auxiliar/"


def prep_quiz(data: dict) -> dict:
    for q in data["preguntas"]:
        q["pregunta"] = inline_md(q["pregunta"])
        q["opciones"] = [inline_md(o) for o in q["opciones"]]
        q["explicacion"] = inline_md(q["explicacion"])
    return data


def build_aux() -> dict:
    ctx = {"home_url": AUX_HOME}
    # temario
    pages = load_collection(CONTENT / "auxiliar" / "temario")
    for p in pages:
        p["url"] = f"{AUX_HOME}temario/" if p["slug"] == "index" else f"{AUX_HOME}temario/{p['slug']}/"
    for i, p in enumerate(pages):
        render("page.html", p["url"], page=p, section="Temario de Auxiliar", section_url=f"{AUX_HOME}temario/",
               siblings=pages, prev=pages[i - 1] if i else None, next=pages[i + 1] if i + 1 < len(pages) else None,
               studied_key=f"aux/temario/{p['slug']}", **ctx)
        index_html_sections(f"Auxiliar · {p['title']}", BASE + p["url"], p["body"], "Temario Auxiliar")

    # tests y ofimática (mismo motor que TAI)
    n_tests = 0
    for src, url, h1, lead_tpl, labels in (
        ("tests", "tests/", "Tests", "{n} preguntas con explicación de los dos bloques. La nota se calcula como en el examen: aciertos − errores/3.",
         {"b1": "Bloque I · Organización pública", "b2": "Bloque II · Actividad administrativa", "info": "Informática básica e Internet"}),
        ("ofimatica", "ofimatica/", "Ofimática práctica", "{n} preguntas de Windows 11, Word, Excel, Access y Outlook 365, tal y como las preguntan en la segunda parte del examen.",
         {"windows": "Windows 11", "word": "Word 365", "excel": "Excel 365", "access": "Access 365", "outlook": "Outlook 365"}),
    ):
        data = read_json(AUX / f"{src}.json", {"preguntas": []})
        prep_quiz(data)
        write(f"data/aux-{src}.json", json.dumps(data, ensure_ascii=False))
        counts = {k: sum(1 for q in data["preguntas"] if q["bloque"] == k) for k in labels}
        render("tests.html", AUX_HOME + url, bloques=labels, counts=counts, total=len(data["preguntas"]),
               source=f"aux-{src}", ns="aux-", h1=h1, lead=lead_tpl.format(n=len(data["preguntas"])),
               extra=read_json(AUX / f"{src}-extra.json"), **ctx)
        if src == "tests":
            n_tests = len(data["preguntas"])
        else:
            n_ofi = len(data["preguntas"])

    # flashcards
    fc = read_json(AUX / "flashcards.json", {"mazos": []})
    n_cards = 0
    for deck in fc["mazos"]:
        for c in deck["tarjetas"]:
            c["f"] = inline_md(c["f"])
            c["b"] = inline_md(c["b"])
        n_cards += len(deck["tarjetas"])
    write("data/aux-flashcards.json", json.dumps(fc, ensure_ascii=False))
    render("flashcards.html", AUX_HOME + "flashcards/", mazos=fc["mazos"], total=n_cards, src="aux-flashcards", ns="aux-", **ctx)

    # psicotécnicos
    render("psicotecnicos.html", AUX_HOME + "psicotecnicos/", **ctx)

    # exámenes
    exams = []
    for f in sorted((AUX / "examenes").glob("*.json")):
        ex = read_json(f)
        ex["notas_html"] = inline_md(ex.get("notas", "")) if ex.get("notas") else ""
        for parte in ex.get("partes", []):
            parte["descripcion_html"] = wrap_tables(inline_md(parte.get("descripcion", ""))) if parte.get("descripcion") else ""
            for q in parte.get("preguntas", []):
                q["explicacion_html"] = wrap_tables(inline_md(q.get("explicacion", "")))
                q["pregunta_html"] = wrap_tables(inline_md(q.get("pregunta", "")))
                q["opciones"] = [inline_md(o) for o in q.get("opciones", [])]
        exams.append(ex)
    exams.sort(key=lambda e: e.get("orden", 99))
    for ex in exams:
        ex["url"] = f"{AUX_HOME}examenes/{ex['slug']}/"
        render("examen.html", ex["url"], ex=ex, **ctx)
        for parte in ex.get("partes", []):
            for q in parte.get("preguntas", []):
                SEARCH.append({"t": ex["titulo"], "s": f"{parte['titulo']} · pregunta {q['n']}: {q.get('tema', '')} · {q.get('pregunta', '')}",
                               "u": f"{BASE}{ex['url']}#{parte['id']}-{q['n']}", "k": "Exámenes Auxiliar",
                               "x": squash(strip_tags(q["explicacion_html"]))[:300]})
    render("examenes.html", AUX_HOME + "examenes/", exams=exams, opo_name="Auxiliar Administrativo del Estado",
           tip1="Ponte un temporizador de 90 minutos y haz las dos partes seguidas, como en el examen real.", **ctx)

    # YouTube
    yt = read_json(AUX / "youtube.json", {"categorias": []})
    render("youtube.html", AUX_HOME + "youtube/", categorias=yt["categorias"],
           lead="Canales y vídeos para Auxiliar: Constitución y leyes, ofimática (Word, Excel, Access, Outlook) y psicotécnicos.", **ctx)

    render("aux_home.html", AUX_HOME, temario=pages, n_tests=n_tests, n_ofi=n_ofi, n_cards=n_cards,
           n_exams=len(exams), **ctx)
    return {"pages": pages}


# ---------------------------------------------------------------- Administrativo del Estado (C1)

ADM = DATA / "adm"
ADM_HOME = "administrativo/"


def strip_first_admonition(text: str) -> str:
    """Quita el primer bloque «!!! tip» (el «Qué pide el programa» del tema reutilizado)."""
    lines = text.lstrip("\n").splitlines()
    if not lines or not lines[0].startswith("!!! "):
        return text
    i = 1
    while i < len(lines) and (lines[i].startswith("    ") or not lines[i].strip()):
        i += 1
    return "\n".join(lines[i:])


def md_sections(text: str) -> tuple[str, list[tuple[str, str]]]:
    """Divide un Markdown en (preámbulo, [(título ##, bloque completo)])."""
    parts = re.split(r"(?m)^(?=## )", text)
    pre, secs = parts[0], []
    for part in parts[1:]:
        secs.append((part.splitlines()[0][3:].strip(), part.rstrip() + "\n"))
    return pre, secs


def sec_number(title: str) -> str | None:
    m = re.match(r"(\d+)\.", title)
    return m.group(1) if m else None


def table_rows(block: str) -> list[str]:
    rows = [l for l in block.splitlines() if l.startswith("|")]
    return rows[2:]  # sin cabecera ni separador


ADM_INCLUDE = re.compile(r"<!--\s*include\s+(\S+?)(?:\.md)?(?:\s+sections=([\w,]+))?\s*-->")


def load_adm_temario() -> list[dict]:
    """Temas de content/administrativo/temario.

    Para no duplicar texto, un tema del C1 se compone con partes de los temas de Auxiliar:
    - front matter «reuse: auxiliar/temario/b2-08-word»: todo el tema (sin su recuadro inicial),
      insertado donde esté «<!-- reuse -->» (o al final del texto propio);
    - «<!-- include auxiliar/temario/b1-02-tc-reforma-corona sections=1,2 -->»: solo esas secciones
      («sections=all»: todas las numeradas). Sus tablas «Resumen» se juntan en «<!-- resumen -->».
    Después se renumeran los «## N.», y los enlaces a temas de Auxiliar incluidos apuntan al tema C1."""
    folder = CONTENT / "administrativo" / "temario"
    raw = []
    for f in sorted(folder.glob("*.md")):
        meta, text = front_matter(f.read_text(encoding="utf-8"))
        raw.append((f.stem, meta, text))
    # 1.ª pasada: qué tema de Auxiliar queda cubierto por qué tema del C1
    link_map: dict[str, str] = {}
    for slug, meta, text in raw:
        srcs = [meta["reuse"]] if meta.get("reuse") else []
        srcs += [m.group(1) for m in ADM_INCLUDE.finditer(text) if (m.group(2) or "all") == "all"]
        srcs += [m.group(1) for m in ADM_INCLUDE.finditer(text)]
        for src in srcs:
            link_map.setdefault(src.rstrip("/") + "/", f"{ADM_HOME}temario/{slug}/")
    pages = []
    for slug, meta, text in raw:
        resumen: list[str] = []

        def source(path: str) -> str:
            t = front_matter((CONTENT / f"{path}.md").read_text(encoding="utf-8"))[1]
            # referencias pensadas para Auxiliar (solo en el texto reutilizado)
            t = re.sub(r'!!! example "Tu caso"\n(?:    .*\n|\n(?=    ))*', "", t)
            t = t.replace("Así lo preguntaron en 2026", "Así lo preguntaron en Auxiliar 2026")
            t = re.sub(r" \((?:ver )?tema (?:II-)?\d+\)", "", t)
            return re.sub(r"\[(el |este )?tema (?:II-)?\d+\]", lambda mm: f"[{mm.group(1) or ''}tema correspondiente]", t)

        if meta.get("reuse"):
            other = strip_first_admonition(source(meta["reuse"])).strip()
            text = text.replace("<!-- reuse -->", other) if "<!-- reuse -->" in text else text.rstrip() + "\n\n" + other + "\n"

        def do_include(m: re.Match) -> str:
            _, secs = md_sections(source(m.group(1)))
            want = (m.group(2) or "all").split(",")
            out = []
            for title, block in secs:
                if title.lower().startswith("resumen"):
                    if want == ["all"]:
                        resumen.extend(table_rows(block))
                    continue
                n = sec_number(title)
                if want == ["all"] or (n and n in want):
                    out.append(block)
            return "\n".join(out)

        text = ADM_INCLUDE.sub(do_include, text)
        if "<!-- resumen -->" in text:
            table = "## Resumen\n\n| Dato | Respuesta |\n| --- | --- |\n" + "\n".join(resumen)
            text = text.replace("<!-- resumen -->", table.rstrip())
        # renumerar secciones
        counter = iter(range(1, 1000))
        text = re.sub(r"(?m)^## \d+\. ", lambda _m: f"## {next(counter)}. ", text)
        for a, b in sorted(link_map.items(), key=lambda kv: -len(kv[0])):
            text = text.replace("{{base}}" + a, "{{base}}" + b)
        body, toc = render_md(text)
        pages.append({"slug": slug, "meta": meta, "body": body, "toc": toc,
                      "title": meta.get("title", slug), "order": float(meta.get("order", 99))})
    pages.sort(key=lambda p: (p["order"], p["slug"]))
    return pages


def load_exams(folder: Path) -> list[dict]:
    exams = []
    for f in sorted(folder.glob("*.json")):
        ex = read_json(f)
        ex["notas_html"] = inline_md(ex.get("notas", "")) if ex.get("notas") else ""
        for parte in ex.get("partes", []):
            parte["descripcion_html"] = wrap_tables(inline_md(parte.get("descripcion", ""))) if parte.get("descripcion") else ""
            for q in parte.get("preguntas", []):
                q["explicacion_html"] = wrap_tables(inline_md(q.get("explicacion", "")))
                q["pregunta_html"] = wrap_tables(inline_md(q.get("pregunta", "")))
                q["opciones"] = [inline_md(o) for o in q.get("opciones", [])]
        exams.append(ex)
    exams.sort(key=lambda e: e.get("orden", 99))
    return exams


def build_adm() -> dict:
    ctx = {"home_url": ADM_HOME}
    pages = load_adm_temario()
    for p in pages:
        p["url"] = f"{ADM_HOME}temario/" if p["slug"] == "index" else f"{ADM_HOME}temario/{p['slug']}/"
    for i, p in enumerate(pages):
        render("page.html", p["url"], page=p, section="Temario de Administrativo", section_url=f"{ADM_HOME}temario/",
               siblings=pages, prev=pages[i - 1] if i else None, next=pages[i + 1] if i + 1 < len(pages) else None,
               studied_key=f"adm/temario/{p['slug']}", **ctx)
        index_html_sections(f"Administrativo · {p['title']}", BASE + p["url"], p["body"], "Temario Administrativo")

    counts_out = {}
    for src, url, h1, lead_tpl, labels, data_dir in (
        ("tests", "tests/", "Tests", "{n} preguntas con explicación de los bloques I a V. La nota se calcula como en el examen: aciertos − errores/3.",
         {"b1": "I · Organización del Estado", "b2": "II · Oficinas públicas", "b3": "III · Derecho administrativo",
          "b4": "IV · Gestión de personal", "b5": "V · Gestión financiera"}, ADM),
        # El bloque VI (ofimática) es el mismo programa que en Auxiliar: se reutilizan sus preguntas.
        ("ofimatica", "ofimatica/", "Ofimática práctica", "{n} preguntas de Windows 11, Word, Excel, Access y Outlook 365 (bloque VI).",
         {"windows": "Windows 11", "word": "Word 365", "excel": "Excel 365", "access": "Access 365", "outlook": "Outlook 365"}, AUX),
    ):
        data = read_json(data_dir / f"{src}.json", {"preguntas": []})
        prep_quiz(data)
        write(f"data/adm-{src}.json", json.dumps(data, ensure_ascii=False))
        counts = {k: sum(1 for q in data["preguntas"] if q["bloque"] == k) for k in labels}
        render("tests.html", ADM_HOME + url, bloques=labels, counts=counts, total=len(data["preguntas"]),
               source=f"adm-{src}", ns="adm-", h1=h1, lead=lead_tpl.format(n=len(data["preguntas"])),
               extra=read_json(data_dir / f"{src}-extra.json"), **ctx)
        counts_out[src] = len(data["preguntas"])

    fc = read_json(ADM / "flashcards.json", {"mazos": []})
    n_cards = 0
    for deck in fc["mazos"]:
        for c in deck["tarjetas"]:
            c["f"] = inline_md(c["f"])
            c["b"] = inline_md(c["b"])
        n_cards += len(deck["tarjetas"])
    write("data/adm-flashcards.json", json.dumps(fc, ensure_ascii=False))
    render("flashcards.html", ADM_HOME + "flashcards/", mazos=fc["mazos"], total=n_cards, src="adm-flashcards", ns="adm-", **ctx)

    exams = load_exams(ADM / "examenes")
    for ex in exams:
        ex["url"] = f"{ADM_HOME}examenes/{ex['slug']}/"
        render("examen.html", ex["url"], ex=ex, **ctx)
        for parte in ex.get("partes", []):
            for q in parte.get("preguntas", []):
                SEARCH.append({"t": ex["titulo"], "s": f"{parte['titulo']} · pregunta {q['n']}: {q.get('tema', '')} · {q.get('pregunta', '')}",
                               "u": f"{BASE}{ex['url']}#{parte['id']}-{q['n']}", "k": "Exámenes Administrativo",
                               "x": squash(strip_tags(q["explicacion_html"]))[:300]})
    render("examenes.html", ADM_HOME + "examenes/", exams=exams, opo_name="Administrativo del Estado",
           tip1="Ponte un temporizador con la duración del examen real y haz las dos partes seguidas.", **ctx)

    yt = read_json(ADM / "youtube.json", {"categorias": []})
    render("youtube.html", ADM_HOME + "youtube/", categorias=yt["categorias"],
           lead="Vídeos para Administrativo: el examen de 2026, Constitución y leyes, contratos, gestión financiera y ofimática.", **ctx)

    render("adm_home.html", ADM_HOME, temario=pages, n_tests=counts_out["tests"], n_ofi=counts_out["ofimatica"],
           n_cards=n_cards, n_exams=len(exams), n_temas=sum(1 for p in pages if p["slug"] != "index"), **ctx)
    return {"pages": pages}


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
    LAWS_BY_SLUG.update({l["slug"]: l for l in leyes})

    temario = build_temario()
    ce_pages = build_constitucion(leyes)
    build_leyes(leyes)
    build_examenes()
    n_tests, n_cards = build_data_pages()
    build_aux()
    build_adm()

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
