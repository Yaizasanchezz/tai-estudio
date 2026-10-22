/* Service worker de TAI Estudio: permite usar la web sin conexión. */
const VERSION = "tai-__BUILD_ID__";
const BASE = "__BASE__";
const CORE = [
  BASE,
  BASE + "static/css/style.css",
  BASE + "static/css/pygments.css",
  BASE + "static/js/app.js",
  BASE + "search.json",
  BASE + "data/tests.json",
  BASE + "data/flashcards.json",
  BASE + "data/supuestos.json",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(VERSION).then((cache) => cache.addAll(CORE).catch(() => null)).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== VERSION).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;

  // Páginas y datos: primero la red (para tener lo último) y, si no hay conexión, la copia guardada.
  const isPage = req.mode === "navigate" || req.headers.get("accept")?.includes("text/html");
  const isData = url.pathname.endsWith(".json");
  if (isPage || isData) {
    event.respondWith(
      fetch(req).then((res) => {
        const copy = res.clone();
        caches.open(VERSION).then((c) => c.put(req, copy));
        return res;
      }).catch(() => caches.match(req, { ignoreSearch: true }).then((r) => r || caches.match(BASE)))
    );
    return;
  }
  // Estilos, scripts e imágenes: primero la caché.
  event.respondWith(
    caches.match(req, { ignoreSearch: true }).then((cached) => cached || fetch(req).then((res) => {
      const copy = res.clone();
      caches.open(VERSION).then((c) => c.put(req, copy));
      return res;
    }))
  );
});
