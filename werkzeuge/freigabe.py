"""Freigabe der Agenten-Vorschläge durch einen Menschen.

Aufruf:  python werkzeuge/freigabe.py            alle noch offenen Vorschläge
         python werkzeuge/freigabe.py mail_19    nur bestimmte Mails

Zeigt jeden Vorschlag aus ausgabe/ und fragt nach der Entscheidung. Freigegeben wird nur
mit "ja" in einem echten Terminal (Vorbild: confirm() in gmx_mail.py). Die Entscheidung
steht danach mit Zeitpunkt in freigabe/freigaben.csv. ausgabe/ bleibt unverändert,
gesendet und gelöscht wird nichts.
"""
import csv
import sys
from datetime import datetime
from pathlib import Path

PROJEKT = Path(__file__).resolve().parent.parent
AUSGABE = PROJEKT / "ausgabe"
FREIGABE = PROJEKT / "freigabe" / "freigaben.csv"
SPALTEN = ["mail_id", "gruppe", "entscheidung", "kommentar", "zeitpunkt", "durch"]


def lies_csv(pfad):
    if not pfad.exists():
        return {}
    with pfad.open(encoding="utf-8-sig", newline="") as datei:
        return {zeile["mail_id"]: zeile for zeile in csv.DictReader(datei, delimiter=";")}


def details(vorschlag, belege, fristen, unsicher):
    mail_id, gruppe = vorschlag["mail_id"], vorschlag["gruppe"]
    if gruppe == "beleg" and mail_id in belege:
        b = belege[mail_id]
        return [f"Datum:     {b['datum']}", f"Betrag:    {b['betrag']}", f"Lieferant: {b['lieferant']}"]
    if gruppe == "bescheid" and mail_id in fristen:
        f = fristen[mail_id]
        return [f"Bescheid:    {f['bescheid_art']} vom {f['bescheiddatum']} ({f['zugang']})",
                f"Bekanntgabe: {f['bekanntgabe']}", f"Fristende:   {f['fristende']}  (Status: {f['status']})",
                f"Rechenweg:   {f['rechenweg']}",
                "Bitte den Rechenweg selbst nachprüfen, bevor Sie freigeben."]
    if gruppe == "rueckfrage":
        entwurf = AUSGABE / "entwuerfe" / f"{mail_id}.md"
        if entwurf.exists():
            zeilen = entwurf.read_text(encoding="utf-8").splitlines()
            return ["Entwurf (Anfang):"] + [f"  {z}" for z in zeilen[:12]] + ([f"  … ({len(zeilen) - 12} weitere Zeilen)"] if len(zeilen) > 12 else [])
        return [f"Entwurf fehlt: {entwurf.relative_to(PROJEKT)}"]
    if gruppe == "unsicher" and mail_id in unsicher:
        return [f"Grund: {unsicher[mail_id]['grund']}"]
    return ["(keine Details gefunden)"]


def frage(text):
    """Nur ein Mensch am Terminal kann antworten. Ohne Terminal gibt es keine Freigabe."""
    try:
        if not sys.stdin.isatty():
            raise EOFError
        return input(text).strip().lower()
    except EOFError:
        return None


def main(argv):
    vorschlaege = lies_csv(AUSGABE / "vorschlaege.csv")
    if not vorschlaege:
        print("Keine Vorschläge gefunden: ausgabe/vorschlaege.csv fehlt oder ist leer.")
        return 1
    if not sys.stdin.isatty():
        print('Keine Freigabe möglich: Das geht nur in einem Terminal, in dem ein Mensch selbst "ja" eingibt.')
        return 1
    belege, fristen = lies_csv(AUSGABE / "belege.csv"), lies_csv(AUSGABE / "fristen.csv")
    unsicher = lies_csv(AUSGABE / "bitte_pruefen.csv")
    erledigt = lies_csv(FREIGABE)

    auswahl = argv[1:] or [m for m in vorschlaege if m not in erledigt]
    unbekannt = [m for m in auswahl if m not in vorschlaege]
    if unbekannt:
        print("Unbekannte mail_id:", ", ".join(unbekannt))
        return 1
    if not auswahl:
        print("Alle Vorschläge sind bereits entschieden.")
        return 0

    neu = not FREIGABE.exists()
    with FREIGABE.open("a", encoding="utf-8", newline="") as datei:
        schreiber = csv.DictWriter(datei, fieldnames=SPALTEN, delimiter=";")
        if neu:
            schreiber.writeheader()
        for nr, mail_id in enumerate(auswahl, start=1):
            v = vorschlaege[mail_id]
            print(f"\n=== Vorschlag {nr} von {len(auswahl)} · {mail_id} · Gruppe: {v['gruppe']} ===")
            print(f"Begründung: {v['begruendung']}")
            for zeile in details(v, belege, fristen, unsicher):
                print(zeile)
            if mail_id in erledigt:
                print(f"Hinweis: bereits entschieden am {erledigt[mail_id]['zeitpunkt']} ({erledigt[mail_id]['entscheidung']}).")
            antwort = frage('Freigeben? "ja" / "nein" / Enter = später / "ende": ')
            if antwort in (None, "ende"):
                print("Beendet.")
                break
            if antwort not in ("ja", "nein"):
                print("Übersprungen, bleibt offen.")
                continue
            kommentar = (frage("Kommentar (optional, Enter = keiner): ") or "") if antwort == "nein" else ""
            jetzt = datetime.now().strftime("%d.%m.%Y %H:%M")
            schreiber.writerow({"mail_id": mail_id, "gruppe": v["gruppe"],
                                "entscheidung": "freigegeben" if antwort == "ja" else "abgelehnt",
                                "kommentar": kommentar, "zeitpunkt": jetzt, "durch": "Mensch am Terminal"})
            datei.flush()
            print(f"{'✓ freigegeben' if antwort == 'ja' else '✗ abgelehnt'} · {jetzt} · eingetragen in freigabe/freigaben.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
