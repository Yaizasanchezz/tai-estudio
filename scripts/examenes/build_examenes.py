"""Genera data/examenes/*.json.

Fuentes:
- scripts/examenes/fuentes/<id>.json: enunciados, opciones y plantilla oficial de cada examen
  (transcripción de los cuadernillos del INAP contrastada con el proyecto libre OpoTAI).
- scripts/examenes/tai_*.py: datos del examen (META), id de la fuente (FUENTE) y, para cada
  pregunta, el tema y una explicación propia (PARTES con tuplas (n, tema, _, respuesta, explicación)).

Uso: python3 scripts/examenes/build_examenes.py
"""
import importlib.util
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent.parent / "data" / "examenes"
OUT_AUX = HERE.parent.parent / "data" / "aux" / "examenes"
FUENTES = HERE / "fuentes"

# id de parte del módulo -> (sección de la fuente, lista)
MAP = {"p1": ("p1", "questions"), "r1": ("p1", "reserve"),
       "s1": ("p2-s1", "questions"), "rs1": ("p2-s1", "reserve"),
       "s2": ("p2-s2", "questions"), "rs2": ("p2-s2", "reserve"),
       # Auxiliar Administrativo: dos partes sin supuestos
       "p2": ("p2", "questions"), "r2": ("p2", "reserve")}


def load(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def clean_statement(text: str, fid: str) -> str:
    """Quita las figuras redibujadas por terceros y adapta las rutas de las imágenes originales."""
    if not text:
        return ""
    out = []
    for line in text.splitlines():
        if "redibujo" in line or "Reconstrucción de OpoTAI" in line:
            continue
        if line.strip() in ("*Original del cuadernillo:*",):
            continue
        out.append(line)
    text = "\n".join(out)
    text = re.sub(r"\]\(assets/" + re.escape(fid) + r"/", "]({{base}}static/img/examenes/" + fid + "/", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    OUT_AUX.mkdir(parents=True, exist_ok=True)
    for path in sorted(HERE.glob("tai_*.py")) + sorted(HERE.glob("aux_*.py")):
        mod = load(path)
        src = json.loads((FUENTES / f"{mod.FUENTE}.json").read_text(encoding="utf-8"))
        secs = {s["id"]: s for s in src["sections"]}
        ex = dict(mod.META)
        ex["partes"] = []
        total = 0
        for parte in mod.PARTES:
            sid, kind = MAP[parte["id"]]
            sec = secs[sid]
            exp = {str(t[0]): t for t in parte["preguntas"]}
            qs = []
            for q in sec[kind]:
                n = str(q["number"]) if kind == "questions" else f"R{q['number']}"
                if n not in exp:
                    raise SystemExit(f"{path.name}: falta la explicación de {parte['id']} {n}")
                _, tema, _, resp_mod, explicacion = exp[n]
                resp = "anulada" if q.get("annulled") else q["answer"].lower()
                if resp_mod != resp:
                    raise SystemExit(f"{path.name}: {parte['id']} {n} respuesta {resp_mod} != plantilla {resp}")
                qs.append({"n": n, "tema": tema, "pregunta": q["text"], "opciones": q["options"],
                           "respuesta": resp, "explicacion": explicacion})
            extra = set(exp) - {x["n"] for x in qs}
            if extra:
                raise SystemExit(f"{path.name}: explicaciones sobrantes en {parte['id']}: {sorted(extra)}")
            total += len(qs)
            desc = parte.get("descripcion")
            if desc is None:
                desc = clean_statement(sec.get("statement") or "", mod.FUENTE) if kind == "questions" else ""
            ex["partes"].append({"id": parte["id"], "titulo": parte["titulo"], "descripcion": desc, "preguntas": qs})
        (OUT_AUX if path.name.startswith("aux_") else OUT).joinpath(f"{ex['slug']}.json").write_text(json.dumps(ex, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{ex['slug']}: {total} preguntas")


if __name__ == "__main__":
    main()
