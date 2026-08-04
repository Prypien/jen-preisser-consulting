# Jen Preisser Consulting

Die Seite zu **jenpreisser-consulting.com**. Eine einzelne, in sich geschlossene
Seite: `index.html` traegt Aufbau, Stil und Verhalten, `bilder/` die Logos und
Aufnahmen der Projekte.

## Aufbau

| Datei | wofuer |
|---|---|
| `index.html` | die ganze Seite — Markup, CSS und JavaScript in einer Datei |
| `bilder/` | Projektbilder und die weissen Wortmarken fuer den Ruhezustand |
| `funnel.html`, `lab.html` | Entwuerfe, nicht verlinkt |
| `CNAME` | die Domain fuer GitHub Pages |

## Oertlich ansehen

    cd ~/Projects/jen-preisser-consulting
    python3 -m http.server 8899
    # dann http://localhost:8899 oeffnen

## Die Kacheln

Die Projektkacheln im Bereich *Arbeiten* folgen alle demselben Bauplan. Zwei
Sonderfaelle sind wichtig:

- `.pcard.marke` sind die Kacheln mit Kundenlogo. Die Klasse heisst bewusst
  **nicht** `.logo` — diesen Namen belegt schon die Marke in der Kopfzeile, und
  die Regeln daraus faerbten frueher ungewollt in die Kacheln hinein.
- Jede Kachel bringt ihre Perspektive im eigenen `transform` mit. Eine
  `perspective` auf der Reihe wuerde allen Kacheln denselben Fluchtpunkt geben,
  und die am Rand waeren beim Kippen sichtbar verzerrt.
