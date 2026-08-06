#!/usr/bin/env python3
"""Porträts für die Profil-Sektion aufbereiten.

Legt die Originale irgendwo ab (Downloads, Fotos-Export, egal) und ruft auf:

    python3 bilder/portraits-aufbereiten.py mantel=~/Downloads/IMG_1234.jpg \
                                            anzug=~/Downloads/IMG_5678.jpg

Erlaubte Schlüssel: mantel, anzug, abendlicht, valencia.
Es müssen nicht alle auf einmal kommen — was fehlt, bleibt unangetastet.

Ergebnis pro Bild: bilder/jen-<schluessel>.jpg, 4:5, 1000x1250, sRGB,
ohne EXIF (also auch ohne GPS-Koordinaten der Aufnahme).

Der Zuschnitt nimmt die volle Bildhöhe und schneidet seitlich mittig zu.
Passt das nicht, hilft --fokus: Anteil von links, 0.0 bis 1.0.

    python3 bilder/portraits-aufbereiten.py mantel=foto.jpg --fokus 0.62
"""
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow fehlt. Installieren mit:  python3 -m pip install Pillow")

ZIEL_W, ZIEL_H = 1000, 1250          # 4:5, reicht für die Kachel auf Retina
SCHLUESSEL = ("mantel", "anzug", "abendlicht", "valencia")
HIER = Path(__file__).resolve().parent


def zuschneiden(quelle: Path, ziel: Path, fokus: float) -> None:
    with Image.open(quelle) as im:
        im = ImageOps.exif_transpose(im)     # Hochformat vom Handy gerade ziehen
        im = im.convert("RGB")
        b, h = im.size
        soll = ZIEL_W / ZIEL_H

        if b / h > soll:                     # zu breit -> seitlich beschneiden
            neu_b = round(h * soll)
            links = round((b - neu_b) * fokus)
            im = im.crop((links, 0, links + neu_b, h))
        else:                                # zu hoch -> unten beschneiden,
            neu_h = round(b / soll)          # der Kopf sitzt oben
            im = im.crop((0, 0, b, neu_h))

        # nie hochrechnen — lieber etwas kleiner als weichgezogen
        breite = min(ZIEL_W, im.width)
        im = im.resize((breite, round(breite / soll)), Image.LANCZOS)
        im.save(ziel, "JPEG", quality=82, optimize=True, progressive=True)
    print(f"  {ziel.name}  <-  {quelle.name}  "
          f"({im.width}x{im.height}, {ziel.stat().st_size // 1024} KB)")


def main(argv: list[str]) -> int:
    fokus = 0.5
    if "--fokus" in argv:
        i = argv.index("--fokus")
        try:
            fokus = float(argv[i + 1])
        except (IndexError, ValueError):
            return print("--fokus braucht eine Zahl zwischen 0 und 1") or 1
        if not 0.0 <= fokus <= 1.0:
            return print("--fokus muss zwischen 0 und 1 liegen") or 1
        del argv[i:i + 2]

    paare = [a for a in argv if "=" in a]
    if not paare:
        return print(__doc__) or 1

    for paar in paare:
        schluessel, _, pfad = paar.partition("=")
        if schluessel not in SCHLUESSEL:
            print(f"  unbekannt: {schluessel} (erlaubt: {', '.join(SCHLUESSEL)})")
            return 1
        quelle = Path(pfad).expanduser()
        if not quelle.is_file():
            print(f"  nicht gefunden: {quelle}")
            return 1
        zuschneiden(quelle, HIER / f"jen-{schluessel}.jpg", fokus)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
