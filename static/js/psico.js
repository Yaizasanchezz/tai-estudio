/* Auxiliar Estudio · generador de psicotécnicos (ejercicios aleatorios con explicación). */
(function () {
  "use strict";
  const app = document.getElementById("psy-app");
  if (!app) return;
  const T = window.TAI;
  const $ = (s) => app.querySelector(s);
  const views = { setup: $('[data-psy-view="setup"]'), run: $('[data-psy-view="run"]'), result: $('[data-psy-view="result"]') };
  const L = ["a", "b", "c", "d"];

  // ------------------------------------------------------------ utilidades
  const rnd = (a, b) => a + Math.floor(Math.random() * (b - a + 1));
  const pick = (arr) => arr[Math.floor(Math.random() * arr.length)];
  const shuffle = (arr) => { const a = arr.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const nf = (n, d) => Number(n).toLocaleString("es-ES", { minimumFractionDigits: d || 0, maximumFractionDigits: d === undefined ? 2 : d });
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  /** Monta 4 opciones distintas con la correcta y devuelve {opts, key}. */
  function options(correct, candidates, fmt) {
    fmt = fmt || ((x) => String(x));
    const seen = new Set([fmt(correct)]);
    const wrong = [];
    for (const c of shuffle(candidates)) {
      const f = fmt(c);
      if (!seen.has(f)) { seen.add(f); wrong.push(c); }
      if (wrong.length === 3) break;
    }
    let k = 1;
    while (wrong.length < 3 && typeof correct === "number") { // relleno numérico
      const c = correct + (k % 2 ? k : -k) * (Math.abs(correct) > 50 ? 5 : 1); k++;
      if (!seen.has(fmt(c))) { seen.add(fmt(c)); wrong.push(c); }
    }
    const all = shuffle([correct].concat(wrong));
    return { opts: all.map(fmt), key: all.indexOf(correct) };
  }

  // ------------------------------------------------------------ series numéricas
  function genNumSeries() {
    const type = pick(["arit", "geom", "alt", "dif2", "muladd", "fib", "sq"]);
    let seq = [], ans, exp, show = 6;
    if (type === "arit") {
      const a = rnd(-10, 40), d = pick([-9, -7, -6, -4, -3, 3, 4, 5, 6, 7, 8, 9, 11, 12]);
      for (let i = 0; i < 7; i++) seq.push(a + i * d);
      exp = "Cada término " + (d > 0 ? "suma " + d : "resta " + -d) + " al anterior (serie aritmética).";
    } else if (type === "geom") {
      const a = rnd(1, 6), r = pick([2, 3]);
      for (let i = 0; i < 6; i++) seq.push(a * Math.pow(r, i));
      show = 5;
      exp = "Cada término se multiplica por " + r + " (serie geométrica).";
    } else if (type === "alt") {
      const a1 = rnd(1, 20), d1 = pick([2, 3, 4, 5]), a2 = rnd(20, 60), d2 = pick([-3, -2, 2, 6, 10]);
      for (let i = 0; i < 9; i++) seq.push(i % 2 === 0 ? a1 + (i / 2) * d1 : a2 + ((i - 1) / 2) * d2);
      show = 8;
      exp = "Son dos series intercaladas: en las posiciones impares se suma " + d1 + " (" + a1 + ", " + (a1 + d1) + ", " + (a1 + 2 * d1) + "…) y en las pares " + (d2 > 0 ? "se suma " + d2 : "se resta " + -d2) + ". El siguiente término toca a la serie de las posiciones impares.";
    } else if (type === "dif2") {
      const a = rnd(1, 15), d0 = rnd(1, 4), k = pick([1, 2, 3]);
      let x = a, d = d0;
      for (let i = 0; i < 7; i++) { seq.push(x); x += d; d += k; }
      exp = "Las diferencias entre términos aumentan de " + k + " en " + k + ": +" + d0 + ", +" + (d0 + k) + ", +" + (d0 + 2 * k) + "… La siguiente diferencia es +" + (d0 + 5 * k) + ".";
    } else if (type === "muladd") {
      const a = rnd(1, 5), m = 2, c = pick([-1, 1, 2, 3]);
      let x = a;
      for (let i = 0; i < 6; i++) { seq.push(x); x = x * m + c; }
      show = 5;
      exp = "Cada término es el anterior × " + m + (c > 0 ? " + " + c : " − " + -c) + ".";
    } else if (type === "fib") {
      const a = rnd(1, 6), b = rnd(2, 9);
      seq = [a, b];
      for (let i = 2; i < 8; i++) seq.push(seq[i - 1] + seq[i - 2]);
      show = 7;
      exp = "Cada término es la suma de los dos anteriores (tipo Fibonacci).";
    } else {
      const s = rnd(1, 6), c = pick([0, 1, -1, 2]);
      for (let i = 0; i < 7; i++) seq.push((s + i) * (s + i) + c);
      exp = "Son los cuadrados de " + s + ", " + (s + 1) + ", " + (s + 2) + "…" + (c ? (c > 0 ? " más " + c : " menos " + -c) : "") + ". El siguiente es " + (s + show) + "²" + (c ? (c > 0 ? " + " + c : " − " + -c) : "") + ".";
    }
    ans = seq[show];
    const shown = seq.slice(0, show);
    const last = shown[show - 1], prevD = last - shown[show - 2];
    const o = options(ans, [ans + 1, ans - 1, ans + 2, ans - 2, last + prevD, ans + prevD, ans * 2, ans + 10, ans - 10].filter((x) => x !== ans));
    return { kind: "Series numéricas", q: "¿Qué número continúa la serie?<p class=\"psy-seq\">" + shown.join(", ") + ", <strong>?</strong></p>", opts: o.opts, key: o.key, exp: exp + " Respuesta: <strong>" + ans + "</strong>." };
  }

  // ------------------------------------------------------------ series de letras (abecedario de 27 letras)
  const ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ".split("");
  function genLetterSeries() {
    const type = pick(["salto", "alterno", "creciente"]);
    let idx = [], exp;
    if (type === "salto") {
      const k = pick([2, 3, 4]);
      const start = rnd(0, 26 - 5 * k);
      for (let i = 0; i < 6; i++) idx.push(start + i * k);
      exp = "Se avanza siempre " + k + " posiciones en el abecedario (se salta " + (k - 1) + (k - 1 === 1 ? " letra" : " letras") + ").";
    } else if (type === "alterno") {
      const a = pick([1, 2]), b = pick([3, 4]);
      const start = rnd(0, 26 - 3 * (a + b) - a);
      let x = start;
      for (let i = 0; i < 6; i++) { idx.push(x); x += i % 2 === 0 ? a : b; }
      exp = "Los saltos se alternan: +" + a + ", +" + b + ", +" + a + ", +" + b + "… El siguiente salto es +" + a + ".";
    } else {
      const start = rnd(0, 6);
      let x = start;
      for (let i = 0; i < 6; i++) { idx.push(x); x += i + 1; }
      exp = "Los saltos crecen de uno en uno: +1, +2, +3, +4… El siguiente salto es +5.";
    }
    const ans = ABC[idx[5]];
    const shown = idx.slice(0, 5).map((i) => ABC[i]);
    const near = [idx[5] - 1, idx[5] + 1, idx[5] - 2, idx[5] + 2, idx[4] + 1, idx[5] - 3, idx[5] + 3, idx[4] - 1].filter((i) => i >= 0 && i < 27 && i !== idx[5]).map((i) => ABC[i]);
    const o = options(ans, near);
    return { kind: "Series de letras", q: "¿Qué letra continúa la serie? <small class=\"muted\">(abecedario de 27 letras, con Ñ)</small><p class=\"psy-seq\">" + shown.join(" ") + " <strong>?</strong></p>", opts: o.opts, key: o.key, exp: exp + " Posiciones: " + shown.map((l) => l + "=" + (ABC.indexOf(l) + 1)).join(", ") + " → <strong>" + ans + "=" + (idx[5] + 1) + "</strong>." };
  }

  // ------------------------------------------------------------ cálculo y problemas
  function genCalc() {
    const type = pick(["pct", "desc", "r3d", "r3i", "frac", "media", "iva"]);
    let q, ans, exp, cands, fmt = (x) => nf(x);
    if (type === "pct") {
      const p = pick([5, 12, 15, 20, 25, 30, 35, 40, 60, 75]), base = pick([80, 120, 240, 360, 450, 600, 840, 1200, 2500]);
      ans = (p * base) / 100;
      q = "¿Cuánto es el " + p + " % de " + nf(base) + "?";
      exp = p + " % de " + nf(base) + " = " + nf(base) + " × " + p + " / 100 = <strong>" + nf(ans) + "</strong>.";
      cands = [ans * 2, ans / 2, ans + base / 10, ans - base / 20, (p + 5) * base / 100, (p - 5) * base / 100];
    } else if (type === "desc") {
      const price = pick([40, 60, 80, 120, 150, 200, 250, 320]), d = pick([10, 15, 20, 25, 30, 40]);
      ans = price * (100 - d) / 100;
      q = "Un artículo cuesta " + nf(price) + " € y tiene un descuento del " + d + " %. ¿Cuánto se paga?";
      exp = "Se paga el " + (100 - d) + " %: " + nf(price) + " × " + nf((100 - d) / 100) + " = <strong>" + nf(ans) + " €</strong>.";
      cands = [price * d / 100, price - d, ans - 5, ans + 5, price * (100 - d - 5) / 100];
      fmt = (x) => nf(x) + " €";
    } else if (type === "r3d") {
      const n1 = pick([3, 4, 5, 6]), unit = pick([1.5, 2, 2.5, 3, 4, 1.2]), n2 = pick([7, 8, 9, 10, 12, 15]);
      const p1 = n1 * unit; ans = n2 * unit;
      q = "Si " + n1 + " carpetas cuestan " + nf(p1) + " €, ¿cuánto cuestan " + n2 + " carpetas?";
      exp = "Regla de tres directa: cada carpeta cuesta " + nf(p1) + " / " + n1 + " = " + nf(unit) + " €, así que " + n2 + " × " + nf(unit) + " = <strong>" + nf(ans) + " €</strong>.";
      cands = [ans + unit, ans - unit, p1 + n2, ans * 1.5, (n2 - 1) * unit];
      fmt = (x) => nf(x) + " €";
    } else if (type === "r3i") {
      const w1 = pick([2, 3, 4, 6]), days = pick([6, 8, 10, 12, 15]), w2 = pick([2, 3, 4, 5, 6, 8, 10, 12]).valueOf();
      const total = w1 * days;
      const w = total % w2 === 0 && w2 !== w1 ? w2 : (w1 * 2);
      ans = total / w;
      q = w1 + " personas tramitan un lote de expedientes en " + days + " días. Trabajando al mismo ritmo, ¿cuántos días tardarían " + w + " personas?";
      exp = "Regla de tres inversa (más personas, menos días): el trabajo total es " + w1 + " × " + days + " = " + total + " días-persona; " + total + " / " + w + " = <strong>" + nf(ans) + " días</strong>.";
      cands = [days * w / w1, ans + 1, ans - 1, ans + 2, days - (w - w1)];
      fmt = (x) => nf(x) + " días";
    } else if (type === "frac") {
      const den = pick([3, 4, 5, 6, 8]), num = rnd(1, den - 1), mult = pick([12, 15, 20, 24, 30, 40]);
      const base = den * mult; ans = num * mult;
      q = "¿Cuánto son los " + num + "/" + den + " de " + nf(base) + "?";
      exp = nf(base) + " / " + den + " = " + mult + ", y " + mult + " × " + num + " = <strong>" + nf(ans) + "</strong>.";
      cands = [ans + mult, ans - mult, base - ans, mult, ans * 2];
    } else if (type === "media") {
      const vals = [rnd(10, 40), rnd(10, 40), rnd(10, 40)];
      const target = rnd(15, 35); vals.push(target * 4 - vals[0] - vals[1] - vals[2]);
      if (vals[3] < 1) vals[3] += 20;
      const sum = vals.reduce((a, b) => a + b, 0); ans = sum / 4;
      q = "Una oficina registra " + vals.join(", ") + " solicitudes en cuatro días. ¿Cuál es la media diaria?";
      exp = "Suma: " + vals.join(" + ") + " = " + sum + "; entre 4 días = <strong>" + nf(ans) + "</strong>.";
      cands = [ans + 1, ans - 1, ans + 2.5, sum / 3, ans + 5];
    } else {
      const net = pick([100, 200, 250, 400, 500, 800]);
      ans = net * 1.21;
      q = "Una factura tiene una base imponible de " + nf(net) + " €. ¿Cuál es el total con un IVA del 21 %?";
      exp = nf(net) + " × 1,21 = <strong>" + nf(ans) + " €</strong> (el IVA son " + nf(net * 0.21) + " €).";
      cands = [net * 0.21, net * 1.12, net + 21, ans + 10, net * 1.2];
      fmt = (x) => nf(x) + " €";
    }
    const o = options(ans, cands.filter((x) => x > 0 && x !== ans), fmt);
    return { kind: "Cálculo y problemas", q: q, opts: o.opts, key: o.key, exp: exp };
  }

  // ------------------------------------------------------------ interpretación de tablas
  const UNITS = ["Registro General", "Atención al Ciudadano", "Recursos Humanos", "Gestión Económica", "Archivo"];
  const MONTHS = ["Enero", "Febrero", "Marzo"];
  function genTable() {
    const rows = UNITS.map((u) => ({ u: u, v: MONTHS.map(() => rnd(12, 95)) }));
    const type = pick(["rowsum", "max", "diff", "colsum", "pct"]);
    let q, ans, exp, cands, fmt = (x) => nf(x);
    if (type === "rowsum") {
      const r = pick(rows); ans = r.v.reduce((a, b) => a + b, 0);
      q = "¿Cuántos expedientes tramitó <strong>" + r.u + "</strong> en el trimestre?";
      exp = r.v.join(" + ") + " = <strong>" + ans + "</strong>.";
      cands = [ans + 10, ans - 10, ans + 1, ans - 9, ans + 20];
    } else if (type === "max") {
      const m = rnd(0, 2);
      const sorted = rows.slice().sort((a, b) => b.v[m] - a.v[m]);
      if (sorted[0].v[m] === sorted[1].v[m]) sorted[0].v[m] += 3; // sin empates
      ans = sorted[0].u;
      q = "¿Qué unidad tramitó <strong>más</strong> expedientes en " + MONTHS[m].toLowerCase() + "?";
      exp = "En " + MONTHS[m].toLowerCase() + " el máximo es " + sorted[0].v[m] + ", de <strong>" + ans + "</strong> (le sigue " + sorted[1].u + " con " + sorted[1].v[m] + ").";
      cands = rows.map((r) => r.u).filter((u) => u !== ans);
      fmt = (x) => String(x);
    } else if (type === "diff") {
      const r = pick(rows); const a = rnd(0, 2); let b = rnd(0, 2); if (b === a) b = (a + 1) % 3;
      ans = Math.abs(r.v[a] - r.v[b]);
      q = "¿Cuál es la diferencia entre " + MONTHS[a].toLowerCase() + " y " + MONTHS[b].toLowerCase() + " en <strong>" + r.u + "</strong>?";
      exp = "|" + r.v[a] + " − " + r.v[b] + "| = <strong>" + ans + "</strong>.";
      cands = [ans + 1, ans - 1, ans + 10, r.v[a] + r.v[b], ans + 5];
    } else if (type === "colsum") {
      const m = rnd(0, 2); ans = rows.reduce((s, r) => s + r.v[m], 0);
      q = "¿Cuántos expedientes se tramitaron en total en <strong>" + MONTHS[m].toLowerCase() + "</strong>?";
      exp = rows.map((r) => r.v[m]).join(" + ") + " = <strong>" + ans + "</strong>.";
      cands = [ans + 10, ans - 10, ans + 12, ans - 7, ans + 1];
    } else {
      // porcentaje exacto: se ajusta la fila para que el total sea redondo
      const r = pick(rows); const total = pick([100, 200, 250, 400]); const p = pick([10, 20, 25, 30, 40, 50]);
      r.v = [Math.round(total * p / 100), 0, 0];
      const rest = total - r.v[0]; r.v[1] = Math.floor(rest / 2); r.v[2] = rest - r.v[1];
      ans = p;
      q = "¿Qué porcentaje de los expedientes del trimestre de <strong>" + r.u + "</strong> corresponde a enero?";
      exp = "Total del trimestre: " + r.v.join(" + ") + " = " + total + ". Enero: " + r.v[0] + " / " + total + " × 100 = <strong>" + p + " %</strong>.";
      cands = [p + 5, p - 5, p + 10, Math.round(r.v[1] / total * 100), 100 - p];
      fmt = (x) => nf(x) + " %";
    }
    let html = '<div class="table-wrap"><table><thead><tr><th>Unidad</th>' + MONTHS.map((m) => "<th>" + m + "</th>").join("") + "</tr></thead><tbody>";
    rows.forEach((r) => { html += "<tr><td>" + r.u + "</td>" + r.v.map((v) => "<td>" + v + "</td>").join("") + "</tr>"; });
    html += "</tbody></table></div>";
    const o = options(ans, cands.filter((x) => (typeof x !== "number" || x >= 0) && x !== ans), fmt);
    return { kind: "Interpretación de tablas", q: "Observa la tabla de expedientes tramitados:" + html + "<p>" + q + "</p>", opts: o.opts, key: o.key, exp: exp };
  }

  // ------------------------------------------------------------ ordenación alfabética
  const AP = ["García", "Garrido", "Gallardo", "Gómez", "González", "Martín", "Martínez", "Marín", "Morales", "Moreno", "Muñoz", "Navarro", "Núñez", "Nieto", "Ortega", "Ortiz", "Pérez", "Peña", "Pastor", "Sánchez", "Santos", "Sanz", "Serrano", "Romero", "Rodríguez", "Rubio", "Ruiz", "Castro", "Castillo", "Cano", "Calvo"];
  const NOM = ["Ana", "Andrés", "Carmen", "Carlos", "Elena", "Eduardo", "Lucía", "Luis", "María", "Mario", "Pilar", "Pablo", "Rosa", "Raúl", "Sara", "Sergio"];
  const cmp = (a, b) => a.localeCompare(b, "es", { sensitivity: "base" });
  function genAlpha() {
    const letter = pick(["Ga", "Go", "Ma", "Mo", "N", "Or", "P", "S", "R", "Ca"]);
    let pool = AP.filter((x) => x.startsWith(letter));
    if (pool.length < 2) pool = AP;
    const people = [];
    const used = new Set();
    while (people.length < 4) {
      const p = { a1: pick(Math.random() < 0.7 ? pool : AP), a2: pick(AP), n: pick(NOM) };
      if (p.a2 === p.a1) continue;
      const k = p.a1 + p.a2 + p.n;
      if (!used.has(k)) { used.add(k); people.push(p); }
    }
    // a veces, dos con el mismo primer apellido para obligar a mirar el segundo
    if (Math.random() < 0.5) { people[1].a1 = people[0].a1; if (people[1].a2 === people[0].a2) people[1].a2 = pick(AP.filter((x) => x !== people[0].a2)); }
    const label = (p) => p.a1 + " " + p.a2 + ", " + p.n;
    if (new Set(people.map(label)).size < 4) return genAlpha();
    const sorted = people.slice().sort((x, y) => cmp(x.a1, y.a1) || cmp(x.a2, y.a2) || cmp(x.n, y.n));
    const pos = rnd(1, 4);
    const ans = label(sorted[pos - 1]);
    const o = options(ans, people.map(label).filter((x) => x !== ans));
    const ord = ["primer", "segundo", "tercer", "cuarto"][pos - 1];
    return { kind: "Ordenación alfabética", q: "Si ordenas alfabéticamente estos nombres por <strong>primer apellido, segundo apellido y nombre</strong>, ¿cuál queda en <strong>" + ord + " lugar</strong>?", opts: o.opts, key: o.key, exp: "Orden correcto: " + sorted.map((p, i) => (i + 1) + ". " + label(p)).join(" · ") + ". Se compara letra a letra; si el primer apellido coincide, decide el segundo, y después el nombre. La Ñ va después de la N." };
  }

  // ------------------------------------------------------------ comprobación de datos
  function code() { const ch = "ABCDEFGHJKLMNPRSTVXZ"; return pick(ch.split("")) + pick(ch.split("")) + "-" + rnd(1000, 9999) + "-" + pick(ch.split("")); }
  function mutate(c) {
    const kind = rnd(0, 2);
    if (kind === 0) { const d = c.slice(3, 7).split(""); const i = rnd(0, 2); [d[i], d[i + 1]] = [d[i + 1], d[i]]; const s = c.slice(0, 3) + d.join("") + c.slice(7); return s === c ? c.slice(0, 3) + String((parseInt(c.slice(3, 7), 10) + 1) % 10000).padStart(4, "1") + c.slice(7) : s; }
    if (kind === 1) { const n = parseInt(c.slice(3, 7), 10); return c.slice(0, 3) + String(n + pick([1, 10, 100]) > 9999 ? n - 1 : n + pick([1, 10, 100])) + c.slice(7); }
    const ch = "ABCDEFGHJKLMNPRSTVXZ".split("").filter((x) => x !== c[c.length - 1]); return c.slice(0, -1) + pick(ch);
  }
  function genCompare() {
    const n = 6, eq = rnd(1, 5);
    const rows = [];
    for (let i = 0; i < n; i++) { const c = code(); let d = i < eq ? c : mutate(c); if (i >= eq && d === c) d = c.slice(0, -1) + (c.slice(-1) === "A" ? "B" : "A"); rows.push([c, d]); }
    const mixed = shuffle(rows);
    const same = mixed.filter((r) => r[0] === r[1]).length;
    let html = '<div class="table-wrap"><table class="psy-codes"><thead><tr><th>Columna A</th><th>Columna B</th></tr></thead><tbody>';
    mixed.forEach((r) => { html += "<tr><td>" + r[0] + "</td><td>" + r[1] + "</td></tr>"; });
    html += "</tbody></table></div>";
    const o = options(same, [0, 1, 2, 3, 4, 5, 6].filter((x) => x !== same && Math.abs(x - same) <= 3));
    return { kind: "Comprobación de datos", q: "¿Cuántas filas tienen el código <strong>exactamente igual</strong> en las dos columnas?" + html, opts: o.opts, key: o.key, exp: "Son iguales <strong>" + same + "</strong>. Las distintas: " + (mixed.filter((r) => r[0] !== r[1]).map((r) => r[0] + " / " + r[1]).join(" · ") || "ninguna") + ". Compara por bloques (letras, número, letra final) y fíjate en las cifras cambiadas de orden." };
  }

  // ------------------------------------------------------------ ortografía
  const SPELL = [["absorber", "absorver"], ["hervir", "herbir"], ["exhausto", "exausto"], ["desahucio", "desaucio"], ["vagabundo", "bagabundo"], ["absolver", "absolber"], ["prohibir", "proibir"], ["adhesivo", "adesivo"], ["exhibir", "exibir"], ["enhebrar", "enebrar"], ["zanahoria", "zanaoria"], ["ahorro", "aorro"], ["hinchar", "inchar"], ["bóveda", "bóbeda"], ["cerveza", "cerbeza"], ["víbora", "bíbora"], ["beneficio", "veneficio"], ["envidia", "embidia"], ["invierno", "imbierno"], ["convertir", "combertir"], ["objeción", "obgeción"], ["cónyuge", "cónyugue"], ["extravagante", "estravagante"], ["excepcional", "escepcional"], ["expectativa", "espectativa"], ["espontáneo", "expontáneo"], ["esplendor", "explendor"], ["exuberante", "exhuberante"], ["adolescente", "adolecente"], ["dieciséis", "diesiséis"], ["jirafa", "girafa"], ["proteger", "protejer"], ["recoger", "recojer"], ["mujer", "muger"], ["extranjero", "extrangero"], ["viajero", "viagero"], ["crujir", "crugir"], ["elegir", "elejir"], ["ingenuo", "injenuo"], ["objetivo", "objetibo"], ["yegua", "llegua"], ["subrayar", "subrallar"], ["ahuyentar", "ahullentar"], ["hallar", "hayar"], ["absceso", "abceso"], ["excavar", "escavar"], ["exhortar", "exortar"], ["deshielo", "desielo"], ["inhóspito", "inóspito"], ["veintitrés", "veintitres"], ["garaje", "garage"], ["bienvenido", "bienbenido"], ["obvio", "obbio"], ["subvención", "suvención"], ["boicot", "voicot"], ["vehículo", "veículo"], ["ahínco", "aínco"], ["exhaustivo", "exaustivo"], ["prevención", "prebención"], ["observar", "obserbar"]];
  function genSpelling() {
    const items = shuffle(SPELL).slice(0, 4);
    const good = items[0][0];
    const o = options(good, items.slice(1).map((x) => x[1]));
    return { kind: "Ortografía", q: "¿Qué palabra está <strong>bien escrita</strong>?", opts: o.opts, key: o.key, exp: "Correcta: <strong>" + good + "</strong>. Las otras están mal: " + items.slice(1).map((x) => "<s>" + x[1] + "</s> → <em>" + x[0] + "</em>").join(", ") + "." };
  }

  // ------------------------------------------------------------ sinónimos y antónimos
  const SYN = [["efímero", "pasajero", ["eterno", "sólido", "ajeno"]], ["diáfano", "claro", ["oscuro", "húmedo", "lejano"]], ["perspicaz", "sagaz", ["torpe", "lento", "ingenuo"]], ["exiguo", "escaso", ["abundante", "extenso", "ancho"]], ["acérrimo", "tenaz", ["tibio", "débil", "indiferente"]], ["locuaz", "hablador", ["callado", "tímido", "serio"]], ["ecuánime", "imparcial", ["parcial", "colérico", "injusto"]], ["inocuo", "inofensivo", ["dañino", "tóxico", "letal"]], ["mendaz", "mentiroso", ["sincero", "veraz", "honesto"]], ["obsoleto", "anticuado", ["moderno", "actual", "novedoso"]], ["nimio", "insignificante", ["enorme", "crucial", "vital"]], ["ufano", "orgulloso", ["humilde", "triste", "avergonzado"]], ["vetusto", "antiguo", ["nuevo", "reciente", "joven"]], ["sosegado", "tranquilo", ["inquieto", "nervioso", "agitado"]], ["pusilánime", "cobarde", ["valiente", "audaz", "osado"]], ["fehaciente", "fidedigno", ["dudoso", "falso", "incierto"]], ["dirimir", "resolver", ["complicar", "enredar", "aplazar"]], ["soslayar", "eludir", ["afrontar", "encarar", "enfrentar"]], ["ínclito", "ilustre", ["desconocido", "vulgar", "anónimo"]], ["prolijo", "extenso", ["breve", "conciso", "escueto"]]];
  const ANT = [["efímero", "duradero", ["breve", "fugaz", "pasajero"]], ["exiguo", "abundante", ["escaso", "mínimo", "reducido"]], ["locuaz", "callado", ["hablador", "parlanchín", "charlatán"]], ["diáfano", "turbio", ["claro", "transparente", "nítido"]], ["inocuo", "nocivo", ["inofensivo", "inerte", "suave"]], ["sosegado", "inquieto", ["tranquilo", "calmado", "sereno"]], ["pródigo", "tacaño", ["generoso", "desprendido", "dadivoso"]], ["obsoleto", "actual", ["anticuado", "viejo", "caduco"]], ["afable", "arisco", ["amable", "cordial", "simpático"]], ["verosímil", "increíble", ["creíble", "posible", "probable"]], ["ensalzar", "denigrar", ["alabar", "elogiar", "exaltar"]], ["esporádico", "frecuente", ["ocasional", "raro", "aislado"]], ["benévolo", "malévolo", ["bondadoso", "indulgente", "clemente"]], ["perenne", "caduco", ["perpetuo", "continuo", "constante"]], ["superfluo", "necesario", ["innecesario", "sobrante", "inútil"]], ["acatar", "desobedecer", ["obedecer", "cumplir", "respetar"]]];
  function genVerbal() {
    const syn = Math.random() < 0.5;
    const it = pick(syn ? SYN : ANT);
    const o = options(it[1], it[2]);
    return { kind: syn ? "Sinónimos" : "Antónimos", q: "¿Cuál es " + (syn ? "un <strong>sinónimo</strong>" : "un <strong>antónimo</strong>") + " de <strong>«" + it[0] + "»</strong>?", opts: o.opts, key: o.key, exp: "«" + it[0] + "» " + (syn ? "significa lo mismo que" : "es lo contrario de") + " <strong>«" + it[1] + "»</strong>." + (syn ? " Las demás opciones significan otra cosa o lo contrario." : " Las demás son sinónimos o se parecen.") };
  }

  const GEN = { numseries: genNumSeries, letterseries: genLetterSeries, calc: genCalc, table: genTable, alpha: genAlpha, compare: genCompare, spelling: genSpelling, verbal: genVerbal };
  window.PSY_GEN = GEN; // para pruebas automáticas

  // ------------------------------------------------------------ motor
  let S = null, timer = null;
  function show(name) { Object.keys(views).forEach((k) => { views[k].hidden = k !== name; }); window.scrollTo({ top: app.offsetTop - 90, behavior: "smooth" }); }

  function start() {
    const types = Array.from(app.querySelectorAll("[data-psy-types] input:checked")).map((i) => i.value);
    if (!types.length) { $("[data-psy-msg]").textContent = "Elige al menos un tipo de ejercicio."; return; }
    $("[data-psy-msg]").textContent = "";
    const n = parseInt(app.querySelector('input[name="psy-count"]:checked').value, 10);
    const mode = app.querySelector('input[name="psy-mode"]:checked').value;
    const qs = [];
    for (let i = 0; i < n; i++) qs.push(GEN[types[i % types.length]]());
    S = { qs: shuffle(qs), i: 0, ans: [], mode: mode, t0: Date.now() };
    const tEl = $("[data-psy-timer]");
    clearInterval(timer);
    if (mode === "examen") {
      // en el examen real: 110 preguntas en 90 min (≈ 49 s por pregunta)
      S.limit = Math.round(n * 49);
      tEl.hidden = false;
      timer = setInterval(() => {
        const left = S.limit - Math.round((Date.now() - S.t0) / 1000);
        tEl.textContent = "⏱ " + Math.floor(Math.max(left, 0) / 60) + ":" + String(Math.max(left, 0) % 60).padStart(2, "0");
        if (left <= 0) finish();
      }, 500);
    } else tEl.hidden = true;
    show("run");
    renderQ();
  }

  function renderQ() {
    const q = S.qs[S.i];
    $("[data-psy-progress]").textContent = "Ejercicio " + (S.i + 1) + " de " + S.qs.length;
    $("[data-psy-kind]").textContent = q.kind;
    $("[data-psy-q]").innerHTML = q.q;
    $("[data-psy-opts]").innerHTML = q.opts.map((o, j) => '<li><button type="button" class="xq-opt" data-l="' + j + '"><span class="xq-l">' + L[j] + '</span><span class="xq-o">' + esc(o) + "</span></button></li>").join("");
    $("[data-psy-feedback]").hidden = true;
    $("[data-psy-next]").hidden = true;
    $("[data-psy-skip]").hidden = false;
  }

  function answer(j) {
    if (S.ans[S.i] !== undefined) return;
    const q = S.qs[S.i];
    S.ans[S.i] = j;
    if (S.mode === "practica") {
      app.querySelectorAll("[data-psy-opts] .xq-opt").forEach((b) => {
        const l = parseInt(b.getAttribute("data-l"), 10);
        if (l === q.key) b.classList.add("is-key"); else if (l === j) b.classList.add("is-wrong");
      });
      const fb = $("[data-psy-feedback]");
      fb.hidden = false;
      fb.className = "psy-feedback " + (j === q.key ? "is-ok" : j === null ? "" : "is-ko");
      fb.innerHTML = "<strong>" + (j === q.key ? "¡Correcto!" : j === null ? "En blanco." : "No es esa.") + "</strong> " + q.exp;
      $("[data-psy-next]").hidden = false;
      $("[data-psy-skip]").hidden = true;
    } else next();
  }

  function next() {
    if (S.i + 1 >= S.qs.length) return finish();
    S.i++;
    renderQ();
  }

  function finish() {
    clearInterval(timer);
    let ok = 0, ko = 0, bl = 0;
    S.qs.forEach((q, i) => { const a = S.ans[i]; if (a === undefined || a === null) bl++; else if (a === q.key) ok++; else ko++; });
    const net = ok - ko / 3, n10 = Math.max(0, net / S.qs.length * 10);
    $("[data-psy-score]").innerHTML = "<strong>" + ok + "</strong> aciertos · <strong>" + ko + "</strong> errores · " + bl + " en blanco → neta " + nf(net) + " de " + S.qs.length + " (<strong>" + nf(n10, 1) + "/10</strong>) · " + Math.round((Date.now() - S.t0) / 1000) + " s";
    $("[data-psy-review]").innerHTML = S.qs.map((q, i) => {
      const a = S.ans[i]; const st = a === undefined || a === null ? "En blanco" : a === q.key ? "Bien" : "Mal (marcaste " + L[a] + ")";
      return '<details class="psy-rev ' + (a === q.key ? "is-ok" : a === undefined || a === null ? "" : "is-ko") + '"' + (a !== q.key ? " open" : "") + "><summary>" + (i + 1) + ". " + q.kind + " · " + st + "</summary><div class=\"psy-q\">" + q.q + "</div><p>Respuesta: <strong>" + L[q.key] + ") " + esc(q.opts[q.key]) + "</strong></p><p class=\"muted\">" + q.exp + "</p></details>";
    }).join("");
    if (ok + ko > 0) {
      T.markStudyDay();
      T.store.set("aux-last-test", { d: new Date().toISOString(), n10: n10, title: "Psicotécnicos", n: S.qs.length });
    }
    show("result");
  }

  $("[data-psy-start]").addEventListener("click", start);
  $("[data-psy-again]").addEventListener("click", () => show("setup"));
  $("[data-psy-next]").addEventListener("click", next);
  $("[data-psy-skip]").addEventListener("click", () => { if (S.mode === "practica") answer(null); else { S.ans[S.i] = null; next(); } });
  $("[data-psy-quit]").addEventListener("click", finish);
  $("[data-psy-opts]").addEventListener("click", (e) => { const b = e.target.closest(".xq-opt"); if (b) answer(parseInt(b.getAttribute("data-l"), 10)); });
})();
