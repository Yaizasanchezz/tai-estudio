/* TAI Estudio · funciones comunes: tema, menú, buscador, progreso y racha. */
(function () {
  "use strict";
  const BASE = window.TAI_BASE || "/";

  // ------------------------------------------------------------ almacenamiento seguro
  const store = {
    get(key, fallback) {
      try {
        const v = localStorage.getItem("tai-" + key);
        return v === null ? fallback : JSON.parse(v);
      } catch (e) { return fallback; }
    },
    set(key, value) {
      try { localStorage.setItem("tai-" + key, JSON.stringify(value)); } catch (e) { /* sin almacenamiento */ }
    },
  };

  function todayStr(d) {
    d = d || new Date();
    return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
  }

  // ------------------------------------------------------------ racha de estudio
  function markStudyDay() {
    const days = store.get("days", []);
    const t = todayStr();
    if (days[days.length - 1] !== t) {
      days.push(t);
      store.set("days", days.slice(-400));
    }
    renderStreakMini();
  }

  function streak() {
    const days = new Set(store.get("days", []));
    let n = 0;
    const d = new Date();
    if (!days.has(todayStr(d))) d.setDate(d.getDate() - 1); // la racha sigue viva si estudiaste ayer
    while (days.has(todayStr(d))) { n++; d.setDate(d.getDate() - 1); }
    return { n: n, today: days.has(todayStr()) };
  }

  function renderStreakMini() {
    const el = document.querySelector("[data-streak-mini]");
    if (!el) return;
    const s = streak();
    if (s.n > 0) {
      el.hidden = false;
      el.textContent = "Racha: " + s.n + (s.n === 1 ? " día" : " días") + (s.today ? " ✿" : "");
    }
  }

  // ------------------------------------------------------------ tema claro / oscuro
  function setupTheme() {
    const btn = document.querySelector("[data-theme-toggle]");
    if (!btn) return;
    btn.addEventListener("click", () => {
      const cur = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", cur);
      try { localStorage.setItem("tai-theme", cur); } catch (e) { /* nada */ }
    });
  }

  // ------------------------------------------------------------ menú lateral (móvil)
  function setupSidebar() {
    const sb = document.getElementById("sidebar");
    const bd = document.querySelector(".sidebar-backdrop");
    const open = () => { sb.classList.add("is-open"); bd.classList.add("is-open"); };
    const close = () => { sb.classList.remove("is-open"); bd.classList.remove("is-open"); };
    document.querySelectorAll("[data-open-sidebar]").forEach((b) => b.addEventListener("click", open));
    document.querySelectorAll("[data-close-sidebar]").forEach((b) => b.addEventListener("click", close));
    document.addEventListener("keydown", (e) => { if (e.key === "Escape") close(); });
  }

  // ------------------------------------------------------------ "estudiado"
  function setupStudied() {
    const studied = store.get("studied", {});
    document.querySelectorAll("[data-studied-toggle]").forEach((btn) => {
      const key = btn.getAttribute("data-studied-toggle");
      btn.setAttribute("aria-pressed", studied[key] ? "true" : "false");
      btn.addEventListener("click", () => {
        const s = store.get("studied", {});
        if (s[key]) delete s[key]; else { s[key] = todayStr(); markStudyDay(); }
        store.set("studied", s);
        btn.setAttribute("aria-pressed", s[key] ? "true" : "false");
      });
    });
    document.querySelectorAll("[data-studied-item]").forEach((li) => {
      if (studied[li.getAttribute("data-studied-item")]) li.classList.add("is-studied");
    });
  }

  // ------------------------------------------------------------ índice lateral activo
  function setupToc() {
    const links = Array.from(document.querySelectorAll(".toc a"));
    if (!links.length || !("IntersectionObserver" in window)) return;
    const map = new Map();
    links.forEach((a) => {
      const el = document.getElementById(decodeURIComponent(a.getAttribute("href").slice(1)));
      if (el) map.set(el, a);
    });
    const obs = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) {
          links.forEach((l) => l.classList.remove("is-current"));
          const a = map.get(en.target);
          if (a) a.classList.add("is-current");
        }
      });
    }, { rootMargin: "-80px 0px -70% 0px" });
    map.forEach((_, el) => obs.observe(el));
  }

  // ------------------------------------------------------------ buscador
  let index = null;
  const norm = (s) => (s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  function highlight(text, terms) {
    let out = esc(text);
    terms.forEach((t) => {
      if (t.length < 2) return;
      const n = norm(out);
      let res = "", i = 0, idx;
      // resaltado tolerante a tildes
      while ((idx = n.indexOf(t, i)) !== -1) {
        res += out.slice(i, idx) + "<mark>" + out.slice(idx, idx + t.length) + "</mark>";
        i = idx + t.length;
      }
      out = res + out.slice(i);
    });
    return out;
  }

  function snippet(text, terms) {
    const n = norm(text);
    let pos = -1;
    for (const t of terms) { pos = n.indexOf(t); if (pos !== -1) break; }
    if (pos === -1) return text.slice(0, 160) + (text.length > 160 ? "…" : "");
    const start = Math.max(0, pos - 60);
    return (start > 0 ? "…" : "") + text.slice(start, start + 180) + (start + 180 < text.length ? "…" : "");
  }

  function search(q) {
    const terms = norm(q).split(/\s+/).filter(Boolean);
    if (!terms.length) return [];
    const scored = [];
    for (const e of index) {
      if (!e._n) e._n = { t: norm(e.t), s: norm(e.s), x: norm(e.x) };
      let score = 0, ok = true;
      for (const t of terms) {
        let hit = 0;
        if (e._n.s.includes(t)) hit += 6;
        if (e._n.t.includes(t)) hit += 3;
        if (e._n.x.includes(t)) hit += 1;
        if (!hit) { ok = false; break; }
        score += hit;
      }
      if (!ok) continue;
      // bonus a artículos exactos: "articulo 14", "art 14"
      if (/^art(iculo|\.)?\s*\d+/.test(norm(q)) && e._n.s.startsWith("articulo " + norm(q).replace(/\D+/g, "") + ".")) score += 20;
      if (e.k === "Texto oficial") score -= 1;
      scored.push([score, e]);
    }
    scored.sort((a, b) => b[0] - a[0]);
    return scored.slice(0, 40).map((x) => x[1]).map((e) => ({ e: e, terms: terms }));
  }

  function setupSearch() {
    const modal = document.getElementById("search-modal");
    const input = document.getElementById("search-input");
    const results = document.getElementById("search-results");
    if (!modal) return;
    let active = -1;

    async function load() {
      if (index) return;
      results.innerHTML = '<p class="sr-empty">Cargando índice…</p>';
      try {
        const r = await fetch(BASE + "search.json");
        index = await r.json();
      } catch (e) {
        results.innerHTML = '<p class="sr-empty">No se ha podido cargar el buscador.</p>';
      }
    }
    function open() {
      modal.hidden = false;
      document.body.style.overflow = "hidden";
      input.focus();
      input.select();
      load().then(() => run());
    }
    function close() {
      modal.hidden = true;
      document.body.style.overflow = "";
    }
    function run() {
      if (!index) return;
      const q = input.value.trim();
      if (q.length < 2) {
        results.innerHTML = '<p class="sr-empty">Escribe al menos 2 letras. Prueba «moción de censura», «artículo 23», «RAID 5» o «silencio administrativo».</p>';
        return;
      }
      const res = search(q);
      active = -1;
      if (!res.length) { results.innerHTML = '<p class="sr-empty">Sin resultados para «' + esc(q) + '».</p>'; return; }
      results.innerHTML = res.map(({ e, terms }) =>
        '<a class="sr-item" role="option" href="' + esc(e.u) + '">' +
        '<span class="sr-kind">' + esc(e.k) + " · " + esc(e.t) + "</span>" +
        '<span class="sr-title">' + highlight(e.s || e.t, terms) + "</span>" +
        '<span class="sr-snip">' + highlight(snippet(e.x, terms), terms) + "</span></a>"
      ).join("");
    }
    function move(d) {
      const items = results.querySelectorAll(".sr-item");
      if (!items.length) return;
      active = (active + d + items.length) % items.length;
      items.forEach((it, i) => it.classList.toggle("is-active", i === active));
      items[active].scrollIntoView({ block: "nearest" });
    }

    document.querySelectorAll("[data-open-search]").forEach((b) => b.addEventListener("click", open));
    document.querySelectorAll("[data-close-search]").forEach((b) => b.addEventListener("click", close));
    modal.addEventListener("click", (e) => { if (e.target === modal) close(); });
    let t;
    input.addEventListener("input", () => { clearTimeout(t); t = setTimeout(run, 120); });
    input.addEventListener("keydown", (e) => {
      if (e.key === "ArrowDown") { e.preventDefault(); move(1); }
      else if (e.key === "ArrowUp") { e.preventDefault(); move(-1); }
      else if (e.key === "Enter") {
        const items = results.querySelectorAll(".sr-item");
        const target = items[active >= 0 ? active : 0];
        if (target) { window.location.href = target.href; close(); }
      }
    });
    results.addEventListener("click", (e) => { if (e.target.closest(".sr-item")) close(); });
    document.addEventListener("keydown", (e) => {
      const tag = (e.target.tagName || "").toLowerCase();
      const typing = tag === "input" || tag === "textarea" || e.target.isContentEditable;
      if ((e.key === "/" && !typing) || ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k")) {
        e.preventDefault();
        open();
      } else if (e.key === "Escape" && !modal.hidden) {
        close();
      }
    });
  }

  // ------------------------------------------------------------ service worker (uso sin conexión)
  function setupSW() {
    if ("serviceWorker" in navigator && location.protocol === "https:") {
      window.addEventListener("load", () => navigator.serviceWorker.register(BASE + "sw.js").catch(() => null));
    }
  }

  window.TAI = { store: store, markStudyDay: markStudyDay, streak: streak, todayStr: todayStr, BASE: BASE };

  document.addEventListener("DOMContentLoaded", () => {
    setupTheme();
    setupSidebar();
    setupStudied();
    setupToc();
    setupSearch();
    renderStreakMini();
    setupSW();
  });
})();
