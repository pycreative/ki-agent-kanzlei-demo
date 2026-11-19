# Review: Film A · Eine Mail mit Frist (86 s)

## Entscheidungen
- Durchgerechnetes Beispiel: die echte `mail_19` (Bescheid und Frage) läuft durch alle Schritte.
- Look Kanzlei-Ablage, Registerfarben je Gruppe, Fristrot nur für Fristdaten und Stempel.
- Ehrlich gekennzeichnet: Freigabe „geplant · Schritt 4“, Hook „Stufe 2 · geplant“, Schubladen zeigen den Sollwert aus dem Orakel (kein Ergebnis des Agenten), Trefferquote „wird gemessen“.
- Keine Musik (keine freie Quelle eingerichtet). 31 Effekte aus der Pixabay-Bibliothek, ohne Namensnennungspflicht.
- Nicht gebaute Storylines: B und C liegen als eigene Filme daneben.

## Geprüft
- `hyperframes check`: ok. Gemessen: Layout, Kontrast, Lesedauer, Bewegung.
- Angesehen: Einzelbilder bei 0.3, 4, 7, 10.5, 14, 19, 30, 36.5, 37, 47.5, 56, 56.5, 62, 66, 73, 79, 84 s.
- Fristdaten im Film stimmen mit `tests/erwartet.csv` überein (23.10. → 27.10. → 27.11.2026).
- Nicht geprüft: Ton nur gemessen, nicht gehört. Handy-Ansicht (360 px) nicht angesehen.

## Schwächste Stelle
- a6 (Soll/Ist): untere Bildhälfte leer. Mit mehr Zeit: Reihen größer, Trefferquote näher an die Reihen.

## Bewusst behaltene Warnungen
- Posteingangsliste in a1 mit 22 px: dient als Textur, nur die markierte Zeile muss gelesen werden (`data-layout-ignore`).
- Kleine Mail-Karten im Flug (a5) und Nummern in den Soll-Feldern (a6): Nebeninformation.
