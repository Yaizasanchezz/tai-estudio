/* TAI Estudio · corrector de exámenes oficiales. */
(function () {
  "use strict";
  const T = window.TAI;
  document.querySelectorAll("[data-exam-part]").forEach((part) => {
    const key = "exam-" + part.getAttribute("data-exam-part");
    const penalty = parseFloat(part.getAttribute("data-penalty")) || 1 / 3;
    const rows = Array.from(part.querySelectorAll(".g-row"));
    const out = part.querySelector("[data-grade-out]");
    let saved = T.store.get(key, {});

    function paint() {
      rows.forEach((r) => {
        const n = r.getAttribute("data-n");
        r.querySelectorAll(".g-opt").forEach((b) => b.classList.toggle("is-on", saved[n] === b.getAttribute("data-l")));
      });
    }
    paint();

    part.addEventListener("click", (e) => {
      const opt = e.target.closest(".g-opt");
      if (opt) {
        const n = opt.closest(".g-row").getAttribute("data-n");
        const l = opt.getAttribute("data-l");
        if (saved[n] === l) delete saved[n]; else saved[n] = l;
        T.store.set(key, saved);
        rows.forEach((r) => r.classList.remove("is-ok", "is-ko", "show-key"));
        paint();
        return;
      }
      if (e.target.closest("[data-grade]")) {
        let ok = 0, ko = 0, bl = 0, valid = 0;
        rows.forEach((r) => {
          const n = r.getAttribute("data-n");
          const k = r.getAttribute("data-key");
          r.classList.remove("is-ok", "is-ko");
          r.classList.add("show-key");
          r.querySelectorAll(".g-opt").forEach((b) => b.classList.toggle("is-key", b.getAttribute("data-l") === k));
          if (k === "anulada") return;
          valid++;
          if (!saved[n]) { bl++; return; }
          if (saved[n] === k) { ok++; r.classList.add("is-ok"); } else { ko++; r.classList.add("is-ko"); }
        });
        const net = ok - ko * penalty;
        const n10 = Math.max(0, (net / valid) * 10);
        out.textContent = ok + " aciertos · " + ko + " errores · " + bl + " en blanco → neta " +
          (Math.round(net * 100) / 100).toLocaleString("es-ES") + " de " + valid + " (" + (Math.round(n10 * 10) / 10).toLocaleString("es-ES") + "/10)";
        if (ok + ko > 0) T.markStudyDay();
      }
      if (e.target.closest("[data-grade-clear]")) {
        if (!confirm("¿Borrar tus respuestas de esta parte?")) return;
        saved = {};
        T.store.set(key, saved);
        rows.forEach((r) => r.classList.remove("is-ok", "is-ko", "show-key"));
        out.textContent = "";
        paint();
      }
    });
  });
})();
