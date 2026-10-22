/* TAI Estudio · panel de la portada. */
(function () {
  "use strict";
  const T = window.TAI;
  const set = (k, v) => { const el = document.querySelector('[data-stat="' + k + '"]'); if (el) el.textContent = v; };

  const QUOTES = [
    "Cada tema que cierras es una plaza un poco más cerca.",
    "No hace falta estudiarlo todo hoy: hace falta estudiar algo hoy.",
    "Constancia mata talento. Y mata temario.",
    "Un test al día y la penalización deja de dar miedo.",
    "Lo difícil ya lo has hecho: empezar.",
    "Hoy toca sumar, aunque sea un poquito.",
    "Tu yo funcionaria con teletrabajo te lo va a agradecer.",
    "Repasar también es avanzar.",
  ];
  const h = new Date().getHours();
  const greet = h < 6 ? "Buenas noches" : h < 14 ? "Buenos días" : h < 21 ? "Buenas tardes" : "Buenas noches";
  const g = document.querySelector("[data-greeting]");
  if (g) g.textContent = greet + ", Yaiza";
  const q = document.querySelector("[data-quote]");
  if (q) q.textContent = QUOTES[(new Date().getDate() + new Date().getMonth()) % QUOTES.length];

  // racha
  const s = T.streak();
  set("streak", s.n + (s.n === 1 ? " día" : " días"));
  set("streak-sub", s.n === 0 ? "Haz un test o repasa flashcards para empezarla" : s.today ? "Hoy ya has estudiado ✿" : "¡Estudia hoy para no perderla!");

  // último test
  const last = T.store.get("last-test", null);
  if (last) {
    set("last-test", (Math.round(last.n10 * 10) / 10).toLocaleString("es-ES") + " / 10");
    set("last-test-sub", last.title + " · " + last.n + " preguntas · " + new Date(last.d).toLocaleDateString("es-ES"));
  }

  // temario estudiado
  const items = document.querySelectorAll("[data-studied-item]");
  const studied = T.store.get("studied", {});
  let done = 0;
  items.forEach((li) => { if (studied[li.getAttribute("data-studied-item")]) done++; });
  const pct = items.length ? Math.round((done / items.length) * 100) : 0;
  set("studied", pct + " %");
  const bar = document.querySelector('[data-stat="studied-bar"]');
  if (bar) bar.style.width = pct + "%";

  // flashcards pendientes
  fetch(T.BASE + "data/flashcards.json").then((r) => r.json()).then((d) => {
    const st = T.store.get("fc", {});
    const today = T.todayStr();
    let due = 0, fresh = 0;
    d.mazos.forEach((m) => m.tarjetas.forEach((c) => {
      if (!st[c.id]) fresh++;
      else if (st[c.id].due <= today) due++;
    }));
    const log = T.store.get("fc-new", {});
    const newLeft = Math.max(0, Math.min(20 - (log[today] || 0), fresh));
    set("due", String(due + newLeft));
  }).catch(() => null);
})();
