/* TAI Estudio · flashcards con repetición espaciada (sistema Leitner). */
(function () {
  "use strict";
  const root = document.getElementById("fc-app");
  if (!root) return;
  const T = window.TAI;
  const NS = root.getAttribute("data-ns") || "";
  const SRC = root.getAttribute("data-src") || "flashcards";
  const INTERVALS = [1, 3, 7, 14, 30, 60]; // días según la caja
  const NEW_PER_DAY = 20;
  const $ = (sel) => root.querySelector(sel);
  const views = {
    decks: $('[data-fc-view="decks"]'),
    study: $('[data-fc-view="study"]'),
    done: $('[data-fc-view="done"]'),
  };

  let DATA = null;
  let state = T.store.get(NS + "fc", {}); // id -> {box, due, seen}
  let queue = [];
  let current = null;
  let sessionStats = { total: 0, ok: 0, mid: 0, ko: 0 };

  const today = () => T.todayStr();
  function addDays(n) { const d = new Date(); d.setDate(d.getDate() + n); return T.todayStr(d); }
  const shuffle = (arr) => { const a = arr.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };

  function allCards() {
    const out = [];
    DATA.mazos.forEach((d) => d.tarjetas.forEach((c) => out.push(Object.assign({ deck: d.id, deckTitle: d.titulo }, c))));
    return out;
  }
  const isDue = (c) => state[c.id] && state[c.id].due <= today();
  const isNew = (c) => !state[c.id];

  function show(name) {
    Object.keys(views).forEach((k) => { views[k].hidden = k !== name; });
  }

  function refreshDecks() {
    const cards = allCards();
    const due = cards.filter(isDue).length;
    const newToday = Math.min(NEW_PER_DAY - newSeenToday(), cards.filter(isNew).length);
    const txt = $("[data-fc-today-text]");
    if (due + Math.max(0, newToday) === 0) txt.textContent = "¡Lo tienes todo al día! Vuelve mañana o estudia un mazo entero.";
    else txt.textContent = due + " tarjetas para repasar y " + Math.max(0, newToday) + " nuevas para hoy.";
    DATA.mazos.forEach((d) => {
      const el = root.querySelector('[data-deck="' + d.id + '"]');
      if (!el) return;
      const known = d.tarjetas.filter((c) => state[c.id] && state[c.id].box >= 3).length;
      el.querySelector("[data-deck-due]").textContent = d.tarjetas.filter((c) => isDue(c) || isNew(c)).length;
      el.querySelector("[data-deck-known]").textContent = known;
      el.querySelector("[data-deck-bar]").style.width = Math.round((known / d.tarjetas.length) * 100) + "%";
    });
  }

  function newSeenToday() {
    const log = T.store.get(NS + "fc-new", {});
    return log[today()] || 0;
  }
  function countNewSeen() {
    const log = T.store.get(NS + "fc-new", {});
    log[today()] = (log[today()] || 0) + 1;
    T.store.set(NS + "fc-new", log);
  }

  function start(deckId, all) {
    let cards = allCards();
    if (deckId === "__due__") {
      const due = shuffle(cards.filter(isDue));
      const fresh = cards.filter(isNew).slice(0, Math.max(0, NEW_PER_DAY - newSeenToday()));
      queue = due.concat(fresh);
    } else {
      cards = cards.filter((c) => c.deck === deckId);
      queue = all ? shuffle(cards) : shuffle(cards.filter((c) => isDue(c) || isNew(c)));
    }
    if (!queue.length) {
      $("[data-fc-done-text]").textContent = "No hay tarjetas pendientes en este mazo. Pulsa «Todas» para repasarlo entero.";
      show("done");
      return;
    }
    sessionStats = { total: queue.length, ok: 0, mid: 0, ko: 0 };
    show("study");
    next();
  }

  function next() {
    current = queue.shift();
    if (!current) { finish(); return; }
    const card = $("[data-fc-card]");
    card.classList.remove("is-flipped");
    $("[data-fc-answer]").hidden = true;
    $("[data-fc-front]").innerHTML = current.f;
    $("[data-fc-back]").innerHTML = current.b;
    const done = sessionStats.ok + sessionStats.mid + sessionStats.ko;
    $("[data-fc-progress]").textContent = current.deckTitle + " · " + (queue.length + 1) + " por repasar";
    card.focus({ preventScroll: true });
  }

  function flip() {
    if (!current) return;
    const card = $("[data-fc-card]");
    card.classList.toggle("is-flipped");
    if (card.classList.contains("is-flipped")) $("[data-fc-answer]").hidden = false;
  }

  function grade(g) {
    if (!current) return;
    const s = state[current.id] || { box: 0, due: today(), seen: 0 };
    if (!state[current.id]) countNewSeen();
    s.seen = (s.seen || 0) + 1;
    if (g === 0) {
      s.box = 0;
      s.due = addDays(1);
      sessionStats.ko++;
      queue.splice(Math.min(3, queue.length), 0, current); // vuelve a salir en esta sesión
    } else if (g === 1) {
      s.box = Math.max(0, Math.min(s.box, 2));
      s.due = addDays(INTERVALS[s.box]);
      sessionStats.mid++;
    } else {
      s.box = Math.min(INTERVALS.length - 1, s.box + 1);
      s.due = addDays(INTERVALS[s.box]);
      sessionStats.ok++;
    }
    state[current.id] = s;
    T.store.set(NS + "fc", state);
    T.markStudyDay();
    next();
  }

  function finish() {
    $("[data-fc-done-text]").textContent = "Has repasado " + sessionStats.total + " tarjetas: " + sessionStats.ok + " sabidas, " +
      sessionStats.mid + " con dudas y " + sessionStats.ko + " fallos (esas volverán mañana).";
    show("done");
    refreshDecks();
  }

  root.addEventListener("click", (e) => {
    const t = e.target.closest("[data-fc-study],[data-fc-back],[data-fc-grade],[data-fc-card],[data-fc-reset]");
    if (!t) return;
    if (t.hasAttribute("data-fc-study")) start(t.getAttribute("data-fc-study"), t.hasAttribute("data-fc-all"));
    else if (t.hasAttribute("data-fc-back")) { show("decks"); refreshDecks(); }
    else if (t.hasAttribute("data-fc-grade")) grade(parseInt(t.getAttribute("data-fc-grade"), 10));
    else if (t.hasAttribute("data-fc-card")) flip();
    else if (t.hasAttribute("data-fc-reset")) {
      if (confirm("¿Seguro que quieres borrar todo tu progreso de flashcards?")) { state = {}; T.store.set(NS + "fc", state); T.store.set(NS + "fc-new", {}); refreshDecks(); }
    }
  });

  document.addEventListener("keydown", (e) => {
    if (views.study.hidden) return;
    if (e.key === " " || e.key === "Enter") { e.preventDefault(); flip(); }
    else if (!$("[data-fc-answer]").hidden && ["1", "2", "3"].includes(e.key)) grade(parseInt(e.key, 10) - 1);
  });

  fetch(T.BASE + "data/" + SRC + ".json").then((r) => r.json()).then((d) => {
    DATA = d;
    // limpiar estados de tarjetas que ya no existen
    const ids = new Set(allCards().map((c) => c.id));
    Object.keys(state).forEach((k) => { if (!ids.has(k)) delete state[k]; });
    refreshDecks();
    const params = new URLSearchParams(location.search);
    if (params.get("mazo")) start(params.get("mazo"), false);
  });
})();
