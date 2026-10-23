/* TAI Estudio · motor de tests y supuestos prácticos. */
(function () {
  "use strict";
  const app = document.getElementById("quiz-app");
  if (!app) return;
  const T = window.TAI;
  const SOURCE = app.getAttribute("data-source"); // "tests" | "supuestos" | "aux-tests"
  const NS = app.getAttribute("data-ns") || ""; // prefijo de almacenamiento por oposición
  const LETTERS = ["a", "b", "c", "d"];
  const views = {
    setup: app.querySelector('[data-view="setup"]'),
    run: app.querySelector('[data-view="run"]'),
    result: app.querySelector('[data-view="result"]'),
    history: app.querySelector('[data-view="history"]'),
  };

  let DATA = null;
  let S = null; // estado del test en curso
  let timerId = null;

  const shuffle = (arr) => {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
    return a;
  };
  const fmtTime = (s) => {
    s = Math.max(0, Math.round(s));
    const m = Math.floor(s / 60), ss = s % 60;
    return (m >= 60 ? Math.floor(m / 60) + ":" + String(m % 60).padStart(2, "0") : m) + ":" + String(ss).padStart(2, "0");
  };
  const fmtNum = (n) => (Math.round(n * 100) / 100).toLocaleString("es-ES");

  function show(name) {
    ["setup", "run", "result"].forEach((k) => { if (views[k]) views[k].hidden = k !== name; });
    if (views.history) views.history.hidden = name === "run";
    window.scrollTo({ top: app.offsetTop - 90, behavior: "smooth" });
  }

  async function load() {
    const r = await fetch(T.BASE + "data/" + SOURCE + ".json");
    DATA = await r.json();
  }

  // ---------------------------------------------------------- arranque
  function startTests() {
    const blocks = Array.from(app.querySelectorAll("[data-blocks] input:checked")).map((i) => i.value);
    const count = parseInt((app.querySelector('input[name="count"]:checked') || {}).value || "20", 10);
    const mode = (app.querySelector('input[name="mode"]:checked') || {}).value || "practica";
    const msg = app.querySelector("[data-setup-msg]");
    let pool = DATA.preguntas.filter((q) => blocks.includes(q.bloque));
    if (mode === "falladas") {
      const failed = T.store.get(NS + "failed", {});
      pool = DATA.preguntas.filter((q) => failed[q.id]);
      if (!pool.length) { msg.textContent = "No tienes preguntas falladas guardadas. ¡Bien!"; return; }
    }
    if (!pool.length) { msg.textContent = "Elige al menos un bloque."; return; }
    msg.textContent = "";
    let qs = shuffle(pool);
    if (count > 0) qs = qs.slice(0, count);
    begin({
      title: mode === "falladas" ? "Repaso de falladas" : "Test",
      questions: qs,
      mode: mode === "examen" ? "examen" : "practica",
      seconds: mode === "examen" ? Math.round(qs.length * 72) : 0,
      enunciado: null,
      kind: "test",
    });
  }

  function startSupuesto(id, mode) {
    const s = DATA.supuestos.find((x) => x.id === id);
    if (!s) return;
    begin({
      title: s.titulo,
      questions: s.preguntas,
      mode: mode,
      seconds: mode === "examen" ? Math.round(s.preguntas.length * 105) : 0,
      enunciado: s.enunciado,
      kind: "supuesto",
    });
  }

  function begin(cfg) {
    S = Object.assign(cfg, { i: 0, answers: {}, locked: {}, start: Date.now(), finished: false });
    if (S.seconds) startTimer();
    show("run");
    renderQuestion();
  }

  // ---------------------------------------------------------- temporizador
  function startTimer() {
    clearInterval(timerId);
    S.deadline = Date.now() + S.seconds * 1000;
    timerId = setInterval(() => {
      const el = views.run.querySelector("[data-timer]");
      const left = (S.deadline - Date.now()) / 1000;
      if (el) {
        el.textContent = "⏱ " + fmtTime(left);
        el.classList.toggle("is-low", left < 120);
      }
      if (left <= 0) { clearInterval(timerId); finish(true); }
    }, 1000);
  }

  // ---------------------------------------------------------- pintar pregunta
  function renderQuestion() {
    const q = S.questions[S.i];
    const n = S.questions.length;
    const answered = Object.keys(S.answers).length;
    const chosen = S.answers[q.id];
    const locked = S.mode === "practica" && S.locked[q.id];

    let html = '<div class="quiz-top">' +
      '<strong>' + escapeHtml(S.title) + "</strong>" +
      '<div class="bar" aria-hidden="true"><span style="width:' + Math.round((answered / n) * 100) + '%"></span></div>' +
      '<span class="muted small">' + answered + " / " + n + " respondidas</span>" +
      (S.seconds ? '<span class="timer" data-timer>⏱ ' + fmtTime((S.deadline - Date.now()) / 1000) + "</span>" : "") +
      "</div>";

    if (S.enunciado) {
      html += '<details class="card sup-enunciado"' + (S.i === 0 ? " open" : "") + "><summary>Enunciado del supuesto</summary>" + S.enunciado + "</details>";
    }

    html += '<div class="q-card">' +
      '<p class="q-meta">Pregunta ' + (S.i + 1) + " de " + n + (q.bloque ? " · " + blockLabel(q.bloque) : "") + "</p>" +
      '<div class="q-text">' + q.pregunta + "</div>" +
      '<div class="options">' +
      q.opciones.map((o, k) => {
        let cls = "opt";
        if (chosen === k) cls += " is-selected";
        if (locked) {
          if (k === q.correcta) cls += " is-correct";
          else if (chosen === k) cls += " is-wrong";
        }
        return '<button class="' + cls + '" data-opt="' + k + '"' + (locked ? " disabled" : "") + '><span class="letter">' + LETTERS[k] + '</span><span class="otext">' + o + "</span></button>";
      }).join("") +
      "</div>";
    if (locked) {
      const ok = chosen === q.correcta;
      html += '<div class="explain"><strong>' + (ok ? "¡Correcto! " : "Respuesta correcta: " + LETTERS[q.correcta] + ") ") + "</strong>" + q.explicacion + "</div>";
    }
    html += "</div>";

    html += '<div class="quiz-nav">' +
      '<button class="btn" data-prev' + (S.i === 0 ? " disabled" : "") + ">← Anterior</button>" +
      (S.mode === "examen" && chosen !== undefined ? '<button class="btn" data-clear>Dejar en blanco</button>' : "") +
      (S.i < n - 1 ? '<button class="btn btn-primary" data-next>Siguiente →</button>' : '<button class="btn btn-primary" data-finish>' + (S.mode === "examen" ? "Entregar y corregir" : "Ver resultado") + "</button>") +
      "</div>";

    html += '<div class="qdots" aria-label="Ir a pregunta">' + S.questions.map((qq, k) => {
      let c = "qdot";
      if (S.answers[qq.id] !== undefined) c += " is-answered";
      if (S.mode === "practica" && S.locked[qq.id]) c += S.answers[qq.id] === qq.correcta ? " is-ok" : " is-ko";
      if (k === S.i) c += " is-current";
      return '<button class="' + c + '" data-goto="' + k + '" aria-label="Pregunta ' + (k + 1) + '">' + (k + 1) + "</button>";
    }).join("") + "</div>";

    if (S.mode === "examen") html += '<p class="muted small center" style="margin-top:14px">Puedes cambiar tus respuestas hasta entregar. Recuerda: cada error resta 1/3; en blanco no resta.</p>';
    views.run.innerHTML = html;
  }

  function blockLabel(b) {
    return ({ constitucion: "Constitución", leyes: "Leyes y Admin. electrónica", tecnologia: "Tecnología básica", desarrollo: "Desarrollo", sistemas: "Sistemas y redes" })[b] || b;
  }
  function escapeHtml(s) { return String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c])); }

  // ---------------------------------------------------------- interacción
  app.addEventListener("click", (e) => {
    const t = e.target.closest("button");
    if (!t) return;
    if (t.hasAttribute("data-start")) { ensure().then(startTests); return; }
    if (t.hasAttribute("data-start-sup")) { ensure().then(() => startSupuesto(t.getAttribute("data-start-sup"), t.getAttribute("data-mode"))); return; }
    if (!S) return;
    if (t.hasAttribute("data-opt")) {
      const q = S.questions[S.i];
      if (S.mode === "practica" && S.locked[q.id]) return;
      S.answers[q.id] = parseInt(t.getAttribute("data-opt"), 10);
      if (S.mode === "practica") S.locked[q.id] = true;
      renderQuestion();
      return;
    }
    if (t.hasAttribute("data-clear")) { delete S.answers[S.questions[S.i].id]; renderQuestion(); return; }
    if (t.hasAttribute("data-prev")) { S.i = Math.max(0, S.i - 1); renderQuestion(); return; }
    if (t.hasAttribute("data-next")) { S.i = Math.min(S.questions.length - 1, S.i + 1); renderQuestion(); return; }
    if (t.hasAttribute("data-goto")) { S.i = parseInt(t.getAttribute("data-goto"), 10); renderQuestion(); return; }
    if (t.hasAttribute("data-finish")) {
      const blanks = S.questions.length - Object.keys(S.answers).length;
      if (S.mode === "examen" && blanks > 0 && !confirm("Te quedan " + blanks + " preguntas en blanco. ¿Entregar igualmente?")) return;
      finish(false);
      return;
    }
    if (t.hasAttribute("data-again")) { show("setup"); return; }
    if (t.hasAttribute("data-only-wrong")) {
      views.result.querySelectorAll(".review-item.is-ok").forEach((el) => { el.hidden = !el.hidden; });
      t.textContent = t.textContent.includes("Solo") ? "Ver todas" : "Solo falladas y en blanco";
    }
  });

  document.addEventListener("keydown", (e) => {
    if (!S || S.finished || views.run.hidden) return;
    const tag = (e.target.tagName || "").toLowerCase();
    if (tag === "input" || tag === "textarea") return;
    const k = e.key.toLowerCase();
    const idx = LETTERS.indexOf(k);
    if (idx !== -1 || ["1", "2", "3", "4"].includes(k)) {
      const opt = idx !== -1 ? idx : parseInt(k, 10) - 1;
      const btn = views.run.querySelector('[data-opt="' + opt + '"]');
      if (btn && !btn.disabled) btn.click();
    } else if (e.key === "ArrowRight") { const b = views.run.querySelector("[data-next]"); if (b) b.click(); }
    else if (e.key === "ArrowLeft") { const b = views.run.querySelector("[data-prev]"); if (b && !b.disabled) b.click(); }
  });

  let loading = null;
  function ensure() { if (!loading) loading = load(); return loading; }

  // ---------------------------------------------------------- corrección
  function finish(byTimeout) {
    clearInterval(timerId);
    S.finished = true;
    const n = S.questions.length;
    let ok = 0, ko = 0;
    const failed = T.store.get(NS + "failed", {});
    S.questions.forEach((q) => {
      const a = S.answers[q.id];
      if (a === undefined) return;
      if (a === q.correcta) { ok++; delete failed[q.id]; }
      else { ko++; failed[q.id] = T.todayStr(); }
    });
    if (S.kind === "test") T.store.set(NS + "failed", failed);
    const blank = n - ok - ko;
    const net = ok - ko / 3;
    const nota10 = Math.max(0, (net / n) * 10);
    const secs = Math.round((Date.now() - S.start) / 1000);

    const hist = T.store.get("history-" + SOURCE, []);
    hist.unshift({ d: new Date().toISOString(), title: S.title, n: n, ok: ok, ko: ko, bl: blank, net: net, n10: nota10, secs: secs, mode: S.mode });
    T.store.set("history-" + SOURCE, hist.slice(0, 30));
    T.store.set(NS + "last-test", { d: new Date().toISOString(), n10: nota10, title: S.title, n: n });
    T.markStudyDay();

    const verdict = nota10 >= 5 ? "¡Aprobado! Sigue así." : nota10 >= 3.5 ? "Cerca: repasa las falladas y vuelve a intentarlo." : "Toca repasar este bloque con calma. ¡Tú puedes!";
    let html = '<div class="card result-hero">' +
      (byTimeout ? '<p class="notice">Se acabó el tiempo y el test se ha entregado automáticamente.</p>' : "") +
      '<p class="eyebrow">' + escapeHtml(S.title) + "</p>" +
      '<p class="score">' + fmtNum(nota10) + '<small style="font-size:.4em"> / 10</small></p>' +
      "<p>" + verdict + "</p>" +
      '<div class="score-grid">' +
      "<div><b>" + ok + "</b><span>Aciertos</span></div>" +
      "<div><b>" + ko + "</b><span>Errores</span></div>" +
      "<div><b>" + blank + "</b><span>En blanco</span></div>" +
      "<div><b>" + fmtNum(net) + "</b><span>Puntuación neta</span></div>" +
      "</div>" +
      '<p class="muted small">Puntuación neta = aciertos − errores/3. Tiempo: ' + fmtTime(secs) + ".</p>" +
      '<div class="setup-actions" style="justify-content:center"><button class="btn btn-primary" data-again>Hacer otro</button>' +
      '<button class="btn" data-only-wrong>Solo falladas y en blanco</button></div>' +
      "</div>";

    html += '<div class="card"><h2>Revisión</h2>' + S.questions.map((q, k) => {
      const a = S.answers[q.id];
      const st = a === undefined ? "En blanco" : a === q.correcta ? "Correcta" : "Fallada";
      const cls = a === q.correcta ? "is-ok" : "is-ko";
      return '<div class="review-item ' + cls + '">' +
        '<p class="q-meta">Pregunta ' + (k + 1) + " · " + st + "</p>" +
        '<div class="q-text">' + q.pregunta + "</div>" +
        '<div class="options">' + q.opciones.map((o, j) => {
          let c = "opt";
          if (j === q.correcta) c += " is-correct";
          else if (j === a) c += " is-wrong";
          return '<button class="' + c + '" disabled><span class="letter">' + LETTERS[j] + '</span><span class="otext">' + o + "</span></button>";
        }).join("") + "</div>" +
        '<div class="explain"><strong>Explicación: </strong>' + q.explicacion + "</div></div>";
    }).join("") + "</div>";

    views.result.innerHTML = html;
    show("result");
    renderHistory();
  }

  // ---------------------------------------------------------- historial
  function renderHistory() {
    const box = app.querySelector("[data-history]");
    if (!box) return;
    const hist = T.store.get("history-" + SOURCE, []);
    if (!hist.length) return;
    box.innerHTML = '<ul class="history-list">' + hist.slice(0, 10).map((h) => {
      const d = new Date(h.d);
      return "<li><span><strong>" + escapeHtml(h.title) + "</strong> · " + h.n + " preguntas" + (h.mode === "examen" ? " · examen" : "") + "</span>" +
        "<span>" + d.toLocaleDateString("es-ES") + " · <strong>" + fmtNum(h.n10) + "/10</strong> (" + h.ok + " ✓ · " + h.ko + " ✗ · " + h.bl + " –)</span></li>";
    }).join("") + "</ul>";
  }

  renderHistory();
  window.addEventListener("beforeunload", (e) => {
    if (S && !S.finished && S.mode === "examen" && Object.keys(S.answers).length) { e.preventDefault(); e.returnValue = ""; }
  });
})();
