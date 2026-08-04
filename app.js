// Nächstes Webinar (Platzhalter-Datum — später anpassbar)
const webinar = {
  title: "Platzhalter: Webinar-Titel",
  startsAt: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000), // in 7 Tagen
};

const references = [
  {
    name: "Referenz 1",
    role: "Rolle / Unternehmen",
    quote: "Platzhalter-Zitat zur Zusammenarbeit.",
  },
  {
    name: "Referenz 2",
    role: "Rolle / Unternehmen",
    quote: "Weiteres Platzhalter-Zitat.",
  },
  {
    name: "Referenz 3",
    role: "Rolle / Unternehmen",
    quote: "Noch ein Platzhalter-Zitat.",
  },
];

let refIndex = 0;

function pad(n) {
  return String(n).padStart(2, "0");
}

function formatDate(d) {
  return d.toLocaleString("de-DE", {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}

function updateCountdown() {
  const el = document.getElementById("countdown");
  if (!el) return;

  const diff = webinar.startsAt.getTime() - Date.now();
  if (diff <= 0) {
    el.textContent = "Gestartet / vorbei";
    return;
  }

  const s = Math.floor(diff / 1000);
  const days = Math.floor(s / 86400);
  const hours = Math.floor((s % 86400) / 3600);
  const mins = Math.floor((s % 3600) / 60);
  const secs = s % 60;
  el.textContent = `${days}d ${pad(hours)}h ${pad(mins)}m ${pad(secs)}s`;
}

function renderReference() {
  const r = references[refIndex];
  document.getElementById("ref-name").textContent = r.name;
  document.getElementById("ref-role").textContent = r.role;
  document.getElementById("ref-quote").textContent = r.quote;
  document.getElementById("ref-counter").textContent =
    `${refIndex + 1} / ${references.length}`;
}

document.getElementById("webinar-title").textContent = webinar.title;
document.getElementById("webinar-date").textContent = formatDate(webinar.startsAt);
updateCountdown();
setInterval(updateCountdown, 1000);

renderReference();
document.getElementById("ref-prev").addEventListener("click", () => {
  refIndex = (refIndex - 1 + references.length) % references.length;
  renderReference();
});
document.getElementById("ref-next").addEventListener("click", () => {
  refIndex = (refIndex + 1) % references.length;
  renderReference();
});
