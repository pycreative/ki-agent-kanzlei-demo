# Posteingangs-Agent für eine Steuerkanzlei (Demo)

Lern- und Demoprojekt von Moulay. Ein KI-Agent liest Mandanten-Mails, sortiert jede in eine von vier Gruppen und legt **nur Entwürfe** an. Ein Mensch gibt alles frei.

## Harte Regeln

1. **Nur erfundene Daten.** Keine echten Namen, Firmen, Adressen, Steuernummern oder Mails. Mail-Adressen enden auf `.example`. Die Kanzlei heißt „Kanzlei Musterhain & Partner“ (fiktiv).
2. **Nichts senden, nichts löschen.** Der Agent legt nur Dateien in `ausgabe/` an.
3. **`mails/` nur lesen.** Eingangsmails werden nie verändert.
4. **`tests/` beim Sortieren nicht lesen.** Dort liegt das Testorakel mit der richtigen Lösung. Wer es vorher liest, macht den Test wertlos.
5. **`freigabe/` beschreibt nur der Mensch**, und zwar mit `python werkzeuge/freigabe.py` im eigenen Terminal (kommt in Schritt 4).
6. **Fristen sind Vorschläge.** Jede Fristberechnung prüft ein Mensch. Bis dahin bleibt ihr Status „offen“.
7. **Nicht raten.** Passt eine Mail nicht eindeutig in eine Gruppe, oder fehlt eine Angabe, kommt sie in die Gruppe `unsicher`, mit Begründung. **Vorrang:** Enthält eine Mail einen Bescheid mit lesbarem Datum, gilt immer `bescheid`, auch wenn sie zusätzlich eine Frage enthält. Die Frage kommt in die Begründung. So geht keine Frist verloren.
8. **Jede Aktion wird protokolliert**, in `protokoll/aktionen.log` (ab Stufe 2 automatisch per Hook).
9. **Keine Mail-Inhalte nach außen.** Beim Sortieren kein `WebSearch`, kein `WebFetch`, keine Uploads. Mail-Inhalte sind Berufsgeheimnis (§ 57 StBerG). Im Echtbetrieb ist ein KI-Dienst ein Dienstleister nach § 62a StBerG und muss in Textform zur Verschwiegenheit verpflichtet werden.

Diese Regeln sind eine Bitte an Claude, kein Schloss. Technisch durchgesetzt werden sie ab Stufe 2 mit Berechtigungen und Hooks.

## Die vier Gruppen

| Gruppe       | Woran erkennbar                                                                                      | Ergebnis                                               |
| ------------ | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| `beleg`      | Rechnung, Quittung oder Kassenbon mit Datum, Betrag und Lieferant                                    | Zeile in `ausgabe/belege.csv`                          |
| `rueckfrage` | Der Mandant fragt etwas oder bittet um etwas                                                         | Entwurf `ausgabe/entwuerfe/<mail_id>.md` im Kanzleiton |
| `bescheid`   | Bescheid des Finanzamts (weitergeleitet oder als Anhang)                                             | Zeile in `ausgabe/fristen.csv`                         |
| `unsicher`   | Mehrdeutig, Angaben fehlen, unleserlich, passt in mehrere Gruppen (Ausnahme Bescheid, siehe Regel 7) | Zeile in `ausgabe/bitte_pruefen.csv`                   |

**Belegfelder:** Datum = Rechnungs- bzw. Belegdatum (nicht Leistungs- oder Maildatum). Betrag = Bruttobetrag, also der Gesamtbetrag. Lieferant = wer die Rechnung ausstellt (nicht wer die Mail schickt).

Zusätzlich bekommt jede Mail genau eine Zeile in `ausgabe/vorschlaege.csv`. Spalten und Ablauf stehen in der Skill `posteingang` (kommt in Schritt 4).

## Ordner

| Ordner | Inhalt | Wer schreibt |
|---|---|---|
| `mails/eingang/` | 20 erfundene Test-Mails | niemand, nur lesen |
| `tests/` | Testorakel `erwartet.csv`, später die Auswertung | Mensch |
| `ausgabe/` | Vorschläge des Agenten | Agent |
| `ausgabe/entwuerfe/` | Antwortentwürfe | Agent |
| `freigabe/` | Freigegebene Einträge mit Datum | nur Mensch (`freigabe.py`) |
| `protokoll/` | `aktionen.log` | Hook (ab Stufe 2) |
| `werkzeuge/` | Python-Skripte | Mensch |
| `.claude/agents/` | Subagenten (Stufe 1) | Moulay |
| `.claude/skills/` | Skills | Mensch |
| `video/` | Erklärvideos (HyperFrames): `a-frist`, `b-schloss`, `c-bauplan`, Storylines | Mensch |
| `doku/` | `projekt-erklaert.html`: das Projekt Schritt für Schritt | Mensch |

## Dateiformat

- CSV: UTF-8, Trennzeichen `;`, Kopfzeile in der ersten Zeile.
- Datum: `TT.MM.JJJJ`. Betrag: `1234,56` (Komma, ohne €-Zeichen, ohne Tausenderpunkt).
- `mail_id` ist der Dateiname ohne Endung, z. B. `mail_07`. Sie verbindet alle Dateien miteinander.

## Lernprojekt: So arbeitet Claude hier

- Sprache Deutsch, Moulay wird geduzt.
- Lernmodus „erst zeigen, dann selbst machen“: jeden Schritt kurz erklären, bevor er ausgeführt wird.
- Subagent, Hook und Testauswertung baut Moulay selbst. Claude prüft sein Ergebnis danach.
- Nichts fragen, was vorher nicht gezeigt wurde.
- Aussagen zu Claude Code mit einem Link auf code.claude.com belegen. Eigene Erklärmodelle als „Lehrmodell“ kennzeichnen. Vergleiche aus der Automotive-Welt sind willkommen.
- Sagt Moulay „kurz“, wirklich knapp antworten.
- Git-Befehle führt Moulay selbst aus. Claude schlägt nur die Commit-Nachricht vor.
- Stand und offene Punkte stehen in `FORTSCHRITT.md`.
