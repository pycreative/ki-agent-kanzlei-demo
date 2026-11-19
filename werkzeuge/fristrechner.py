"""Fristrechner für Einspruchsfristen (Demo, Feiertage Hessen).

Aufruf:  python werkzeuge/fristrechner.py <Bescheiddatum TT.MM.JJJJ> <post|elster>

Regeln:
1. Bekanntgabe am 4. Tag nach Aufgabe zur Post (§ 122 Abs. 2 Nr. 1 AO) bzw. nach
   Bereitstellung zum Abruf (§ 122a Abs. 4 AO). Für Bescheide bis 31.12.2024 galt der 3. Tag.
2. Fällt dieser Tag auf Samstag, Sonntag oder Feiertag: nächster Werktag (BFH, § 108 Abs. 3 AO).
3. Fristende einen Monat nach Bekanntgabe (§ 355 Abs. 1 AO, § 108 Abs. 1 AO mit § 188 BGB).
4. Fällt das Fristende auf Samstag, Sonntag oder Feiertag: nächster Werktag (§ 108 Abs. 3 AO).
Annahme: Bescheiddatum = Tag der Aufgabe zur Post. Das Ergebnis ist ein Vorschlag, ein Mensch prüft.
"""
import calendar
import sys
from datetime import date, timedelta

WOCHENTAG = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]


def ostersonntag(jahr):
    # Gaußsche Osterformel (gregorianischer Kalender)
    a, b, c = jahr % 19, jahr // 100, jahr % 100
    d, e = b // 4, b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = c // 4, c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    monat = (h + l - 7 * m + 114) // 31
    tag = (h + l - 7 * m + 114) % 31 + 1
    return date(jahr, monat, tag)


def feiertage_hessen(jahr):
    ostern = ostersonntag(jahr)
    beweglich = {
        "Karfreitag": ostern - timedelta(days=2),
        "Ostermontag": ostern + timedelta(days=1),
        "Christi Himmelfahrt": ostern + timedelta(days=39),
        "Pfingstmontag": ostern + timedelta(days=50),
        "Fronleichnam": ostern + timedelta(days=60),
    }
    fest = {
        "Neujahr": date(jahr, 1, 1),
        "Tag der Arbeit": date(jahr, 5, 1),
        "Tag der Deutschen Einheit": date(jahr, 10, 3),
        "1. Weihnachtstag": date(jahr, 12, 25),
        "2. Weihnachtstag": date(jahr, 12, 26),
    }
    return {d: name for name, d in {**fest, **beweglich}.items()}


def freier_tag(tag):
    """Name des Grundes, warum der Tag kein Werktag ist, sonst None."""
    if tag.weekday() == 5:
        return "Samstag"
    if tag.weekday() == 6:
        return "Sonntag"
    return feiertage_hessen(tag.year).get(tag)


def naechster_werktag(tag, schritte):
    while (grund := freier_tag(tag)) is not None:
        schritte.append(f"{f(tag)} ist {grund}")
        tag += timedelta(days=1)
    return tag


def plus_ein_monat(tag):
    jahr, monat = (tag.year, tag.month + 1) if tag.month < 12 else (tag.year + 1, 1)
    letzter = calendar.monthrange(jahr, monat)[1]
    return date(jahr, monat, min(tag.day, letzter))


def f(tag):
    return f"{WOCHENTAG[tag.weekday()]} {tag:%d.%m.%Y}"


def rechne(bescheiddatum, zugang):
    schritte = []
    tage = 4 if bescheiddatum >= date(2025, 1, 1) else 3
    roh = bescheiddatum + timedelta(days=tage)
    schritte.append(f"{f(bescheiddatum)} + {tage} Tage ({'Post' if zugang == 'post' else 'ELSTER'}) = {f(roh)}")
    bekanntgabe = naechster_werktag(roh, schritte)
    schritte.append(f"Bekanntgabe {f(bekanntgabe)}")
    ende_roh = plus_ein_monat(bekanntgabe)
    schritte.append(f"+ 1 Monat = {f(ende_roh)}")
    fristende = naechster_werktag(ende_roh, schritte)
    schritte.append(f"Fristende {f(fristende)}")
    hinweis = "" if tage == 4 else "Bescheid vor 2025: 3-Tage-Regel, bitte besonders prüfen"
    return bekanntgabe, fristende, " -> ".join(schritte), hinweis


def main(argv):
    if not sys.stdout.isatty():
        # Aufruf durch ein Programm (z. B. den Agenten): Ausgabe als UTF-8, sonst scheitern Umlaute
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    if len(argv) != 3 or argv[2] not in ("post", "elster"):
        print("Aufruf: python werkzeuge/fristrechner.py <TT.MM.JJJJ> <post|elster>", file=sys.stderr)
        return 2
    try:
        t, m, j = (int(x) for x in argv[1].split("."))
        bescheiddatum = date(j, m, t)
    except ValueError:
        print(f"Ungültiges Datum: {argv[1]} (erwartet TT.MM.JJJJ)", file=sys.stderr)
        return 2
    bekanntgabe, fristende, rechenweg, hinweis = rechne(bescheiddatum, argv[2])
    print(f"bekanntgabe={bekanntgabe:%d.%m.%Y}")
    print(f"fristende={fristende:%d.%m.%Y}")
    print(f"rechenweg={rechenweg}")
    if hinweis:
        print(f"hinweis={hinweis}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
