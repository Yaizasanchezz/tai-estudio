"""Sustituye las notas de una página anotada conservando front matter, títulos y destacados.
Uso: python3 setnotes.py content/constitucion/00-preliminar.md notas.md [--rango X-Y]"""
import re, sys
page, notes = sys.argv[1], open(sys.argv[2]).read().strip()
s = open(page).read()
fm, body = re.match(r"^(---\n.*?\n---\n)(.*)$", s, re.S).groups()
if "--rango" in sys.argv:
    fm = re.sub(r"(?m)^rango: .*$", "rango: " + sys.argv[sys.argv.index("--rango") + 1], fm)
keep = [l for l in body.splitlines() if re.match(r"^<!--\s*(titulo|destacar)\s", l)]
# las líneas titulo/destacar del archivo de notas mandan sobre las antiguas
newkeys = {re.match(r"<!--\s*(\w+)\s+([\w:-]+)", l).groups() for l in notes.splitlines() if re.match(r"^<!--\s*(titulo|destacar)\s", l)}
keep = [l for l in keep if re.match(r"<!--\s*(\w+)\s+([\w:-]+)", l).groups() not in newkeys]
open(page, "w").write(fm + "\n" + "\n".join(keep) + "\n\n" + notes + "\n")
