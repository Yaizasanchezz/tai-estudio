#!/usr/bin/env python3
"""Descarga el texto consolidado y vigente de las normas de data/leyes.json
usando la API de datos abiertos del BOE y lo guarda en data/boe/<ID>.json.

Lo ejecuta GitHub Actions cada semana. Solo usa la biblioteca estándar.
API: https://www.boe.es/datosabiertos/api/legislacion-consolidada
"""
from __future__ import annotations

import datetime as dt
import json
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "boe"
API = "https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/"
UA = "tai-estudio/1.0 (web de estudio personal; GitHub Actions)"
TODAY = dt.date.today().strftime("%Y%m%d")


def get(url: str, accept: str, tries: int = 3) -> bytes:
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"Accept": accept, "User-Agent": UA})
            with urllib.request.urlopen(req, timeout=90) as r:
                return r.read()
        except (urllib.error.URLError, TimeoutError) as e:  # reintentos suaves
            last = e
            time.sleep(3 * (i + 1))
    raise RuntimeError(f"No se pudo descargar {url}: {last}")


def find_key(obj, key):
    """Busca la primera aparición de una clave en un JSON anidado."""
    if isinstance(obj, dict):
        if key in obj:
            return obj[key]
        for v in obj.values():
            r = find_key(v, key)
            if r is not None:
                return r
    elif isinstance(obj, list):
        for v in obj:
            r = find_key(v, key)
            if r is not None:
                return r
    return None


def fmt_date(s: str | None) -> str:
    if not s or len(s) < 8:
        return s or ""
    return f"{s[6:8]}/{s[4:6]}/{s[0:4]}"


def element_html(el: ET.Element) -> str:
    el = _copy(el)
    el.tail = None
    for a in el.iter("a"):
        href = a.get("href", "")
        if href.startswith("/"):
            a.set("href", "https://www.boe.es" + href)
        if a.get("href", "").startswith("http"):
            a.set("target", "_blank")
            a.set("rel", "noopener")
    return ET.tostring(el, encoding="unicode", method="html")


def _copy(el: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(el, encoding="unicode"))


def pick_version(versions: list[ET.Element]) -> ET.Element | None:
    """La versión vigente: la más reciente cuya fecha de vigencia ya ha llegado."""
    best = None
    best_key = ""
    for v in versions:
        vig = v.get("fecha_vigencia") or v.get("fecha_publicacion") or ""
        if vig and vig > TODAY:
            continue
        key = (v.get("fecha_publicacion") or "") + vig
        if key >= best_key:
            best, best_key = v, key
    return best if best is not None else (versions[-1] if versions else None)


def parse_text(xml_bytes: bytes) -> list[dict]:
    root = ET.fromstring(xml_bytes)
    code = root.findtext("status/code")
    if code and code != "200":
        raise RuntimeError(f"La API devolvió el estado {code}")
    bloques = []
    for b in root.iter("bloque"):
        cad = b.get("fecha_caducidad")
        if cad and cad <= TODAY:
            continue  # bloque derogado
        v = pick_version(b.findall("version"))
        if v is None:
            continue
        html = "".join(element_html(child) for child in list(v))
        if not html.strip():
            continue
        bloques.append({"id": b.get("id"), "tipo": b.get("tipo"), "titulo": b.get("titulo"), "html": html})
    return bloques


def fetch_one(law: dict) -> str:
    boe_id = law["id"]
    meta_raw = get(API + boe_id + "/metadatos", "application/json")
    meta = json.loads(meta_raw)
    titulo = find_key(meta, "titulo") or law["nombre"]
    fecha_act = find_key(meta, "fecha_actualizacion") or ""
    bloques = parse_text(get(API + boe_id + "/texto", "application/xml"))
    if not bloques:
        raise RuntimeError("Texto vacío")
    data = {
        "id": boe_id,
        "titulo": titulo,
        "fecha_actualizacion": fecha_act,
        "fecha_actualizacion_fmt": fmt_date(str(fecha_act)[:8]),
        "descargado": dt.date.today().strftime("%d/%m/%Y"),
        "bloques": bloques,
    }
    path = OUT / f"{boe_id}.json"
    if path.exists():
        old = json.loads(path.read_text(encoding="utf-8"))
        if old.get("bloques") == bloques and old.get("titulo") == titulo:
            return f"sin cambios ({len(bloques)} bloques)"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=0), encoding="utf-8")
    return f"actualizada: {titulo[:70]} ({len(bloques)} bloques)"


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    leyes = json.loads((ROOT / "data" / "leyes.json").read_text(encoding="utf-8"))["leyes"]
    only = set(sys.argv[1:])
    errors = 0
    for law in leyes:
        if not law.get("id") or (only and law["slug"] not in only):
            continue
        try:
            print(f"{law['id']}: {fetch_one(law)}", flush=True)
        except Exception as e:  # una norma que falle no detiene las demás
            errors += 1
            print(f"{law['id']}: ERROR {e}", flush=True)
        time.sleep(1.5)  # ser amables con el servidor del BOE
    print(f"Terminado con {errors} errores")
    return 0


if __name__ == "__main__":
    sys.exit(main())
