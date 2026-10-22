# TAI Estudio

Web de estudio para la oposición **TAI** (Cuerpo de Técnicos Auxiliares de Informática de la Administración del Estado).

**Web:** https://yaizasanchezz.github.io/tai-estudio/

## Apartados

- **Temario**: los 33 temas explicados por bloques, con ejemplos resueltos.
- **Constitución**: explicada artículo por artículo y texto oficial consolidado del BOE.
- **Leyes**: las normas del temario explicadas y su texto oficial (se actualiza solo cada semana).
- **Tests**: preguntas con explicación, por bloques o en modo examen (aciertos − errores/3).
- **Supuestos prácticos**: casos de desarrollo y de sistemas con corrección.
- **Exámenes resueltos**: exámenes oficiales del INAP con todas las respuestas explicadas y corrector.
- **Flashcards**: tarjetas con repetición espaciada.
- **YouTube**: vídeos y canales recomendados.
- **OpositaTest**: acceso directo a su sección de TAI.

El progreso (tests, flashcards, temas estudiados, racha) se guarda en el navegador de cada dispositivo.

## Cómo añadir contenido

| Quiero añadir… | Edita… |
| --- | --- |
| Preguntas de test | `data/tests.json` (bloque: `constitucion`, `leyes`, `tecnologia`, `desarrollo` o `sistemas`) |
| Flashcards | `data/flashcards.json` (cada tarjeta necesita un `id` único) |
| Un supuesto práctico | `data/supuestos.json` |
| Un examen resuelto | un nuevo fichero en `data/examenes/` |
| Vídeos de YouTube | `data/youtube.json` |
| Una ley | `data/leyes.json` (con su identificador BOE-A-…) y, si quieres explicarla, `content/leyes/<slug>.md` |
| Texto del temario | los ficheros Markdown de `content/` |

Al subir los cambios a `main`, GitHub Actions genera y publica la web sola en un par de minutos.

## Cómo funciona por dentro

- `build.py` convierte el Markdown y los JSON en una web estática (HTML, CSS y JavaScript sin dependencias) dentro de `dist/`.
- `scripts/fetch_boe.py` descarga el texto consolidado de cada ley desde la [API de datos abiertos del BOE](https://www.boe.es/datosabiertos/).
- `.github/workflows/deploy.yml` publica en GitHub Pages en cada cambio y, cada lunes, actualiza los textos del BOE.

Para generarla en local:

```bash
pip install -r requirements.txt
python build.py
cd dist && python -m http.server   # (la web espera estar en /tai-estudio/; usa SITE_BASE=/ python build.py para la raíz)
```
