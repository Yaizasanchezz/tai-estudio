/* TAI Estudio · exámenes oficiales interactivos.
   Cada parte guarda en este dispositivo las letras elegidas y corrige con la penalización real. */
(function () {
  "use strict";
  const T = window.TAI;
  document.querySelectorAll("[data-exam-part]").forEach((part) => {
    const key = "exam-" + part.getAttribute("data-exam-part");
    const penalty = parseFloat(part.getAttribute("data-penalty")) || 1 / 3;
    const items = Array.from(part.querySelectorAll(".xq"));
    const out = part.querySelector("[data-grade-out]");
    const progress = part.querySelector("[data-progress]");
    let saved = T.store.get(key, {});

    function paint() {
      let answered = 0;
      items.forEach((q) => {
        const n = q.getAttribute("data-n");
        if (saved[n]) answered++;
        q.querySelectorAll(".xq-opt").forEach((b) => {
          const on = saved[n] === b.getAttribute("data-l");
          b.classList.toggle("is-on", on);
          b.setAttribute("aria-pressed", on ? "true" : "false");
        });
      });
      if (progress) progress.textContent = answered + " / " + items.length + " contestadas";
    }

    function clearMarks() {
      part.classList.remove("is-graded");
      items.forEach((q) => {
        q.classList.remove("is-ok", "is-ko", "is-blank");
        q.querySelectorAll(".xq-opt").forEach((b) => b.classList.remove("is-key", "is-wrong"));
      });
    }

    paint();

    part.addEventListener("click", (e) => {
      const opt = e.target.closest(".xq-opt");
      if (opt) {
        const q = opt.closest(".xq");
        const n = q.getAttribute("data-n");
        const l = opt.getAttribute("data-l");
        if (saved[n] === l) delete saved[n]; else saved[n] = l;
        T.store.set(key, saved);
        if (part.classList.contains("is-graded")) { clearMarks(); out.textContent = ""; }
        paint();
        return;
      }
      if (e.target.closest("[data-grade]")) {
        let ok = 0, ko = 0, bl = 0, valid = 0;
        clearMarks();
        part.classList.add("is-graded");
        items.forEach((q) => {
          const n = q.getAttribute("data-n");
          const k = q.getAttribute("data-key");
          if (k === "anulada") return;
          valid++;
          q.querySelectorAll(".xq-opt").forEach((b) => {
            const l = b.getAttribute("data-l");
            if (l === k) b.classList.add("is-key");
            else if (saved[n] === l) b.classList.add("is-wrong");
          });
          if (!saved[n]) { bl++; q.classList.add("is-blank"); return; }
          if (saved[n] === k) { ok++; q.classList.add("is-ok"); }
          else { ko++; q.classList.add("is-ko"); const d = q.querySelector(".xq-sol"); if (d) d.open = true; }
        });
        const net = ok - ko * penalty;
        const n10 = Math.max(0, (net / Math.max(valid, 1)) * 10);
        out.textContent = ok + " aciertos · " + ko + " errores · " + bl + " en blanco → neta " +
          (Math.round(net * 100) / 100).toLocaleString("es-ES") + " de " + valid + " (" +
          (Math.round(n10 * 10) / 10).toLocaleString("es-ES") + "/10). Las falladas tienen la explicación abierta.";
        if (ok + ko > 0) T.markStudyDay();
        out.scrollIntoView({ behavior: "smooth", block: "nearest" });
      }
      if (e.target.closest("[data-grade-clear]")) {
        if (!confirm("¿Borrar tus respuestas de esta parte?")) return;
        saved = {};
        T.store.set(key, saved);
        clearMarks();
        items.forEach((q) => { const d = q.querySelector(".xq-sol"); if (d) d.open = false; });
        out.textContent = "";
        paint();
      }
    });
  });
})();
