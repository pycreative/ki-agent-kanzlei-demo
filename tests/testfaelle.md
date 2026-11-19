# Testfall-Spezifikation: Posteingang

Testorakel: `erwartet.csv` (eine Zeile pro Mail, Schlüssel `mail_id`). Erstellt am 03.11.2026, vor der ersten Sortierung.
Der Agent darf diesen Ordner beim Sortieren nicht lesen (CLAUDE.md, Regel 4).

## Testbasis

- `CLAUDE.md`: Regeln 1 bis 9, die vier Gruppen, die Belegfelder, die Vorrangregel (Regel 7).
- Fristregel (Stand 03.11.2026, gegen den Gesetzestext geprüft):
  1. Bekanntgabe am 4. Tag nach Aufgabe zur Post (§ 122 Abs. 2 Nr. 1 AO) oder nach Bereitstellung zum Abruf in ELSTER (§ 122a Abs. 4 AO).
  2. Fällt dieser Tag auf Samstag, Sonntag oder Feiertag, verschiebt er sich auf den nächsten Werktag (BFH-Rechtsprechung, § 108 Abs. 3 AO).
  3. Fristende einen Monat nach Bekanntgabe (§ 355 Abs. 1 AO, § 108 Abs. 1 AO mit § 188 BGB).
  4. Fällt das Fristende auf Samstag, Sonntag oder Feiertag, endet die Frist am nächsten Werktag (§ 108 Abs. 3 AO).
  5. Annahmen: Feiertage Hessen. Bescheiddatum = Tag der Aufgabe zur Post. Deshalb prüft immer ein Mensch.

Quellen: https://www.gesetze-im-internet.de/ao_1977/__122.html · https://www.gesetze-im-internet.de/ao_1977/__122a.html · https://www.gesetze-im-internet.de/ao_1977/__108.html · https://www.haufe.de/steuern/gesetzgebung-politik/4-tage-zugangsvermutung-bei-der-bekanntgabe-von-steuerbescheiden_168_625084.html

## Testfälle

| Mail | Erwartet | Testbedingung | Folgt aus |
|---|---|---|---|
| 01 | beleg | Normalfall Rechnung | Gruppen, Belegfelder |
| 02 | rueckfrage | Terminwunsch | Gruppen |
| 03 | bescheid | Post: 19.10. → Bekanntgabe Fr 23.10. → Ende Mo 23.11. | Fristregel 1, 3 |
| 04 | beleg | „1.249,00 €“ → `1249,00` | Dateiformat |
| 05 | unsicher | Beleg und Frage in einer Mail | Regel 7 |
| 06 | rueckfrage | Steuerfrage, keine verbindliche Auskunft | Gruppen, Kanzleiton |
| 07 | bescheid | 21.10. → 4. Tag So 25.10. → Mo 26.10. → Ende Do 26.11. | Fristregel 2 |
| 08 | beleg | „Samstag, 3. Oktober 2026“ → `03.10.2026` | Dateiformat |
| 09 | rueckfrage | Frage nach Unterlagen | Gruppen |
| 10 | bescheid | ELSTER 26.10. → Fr 30.10. → Ende Mo 30.11. | Fristregel 1 |
| 11 | unsicher | Betrag unleserlich | Regel 7 |
| 12 | beleg | „10/14/2026“ → `14.10.2026`, „EUR 29.00“ → `29,00` | Dateiformat |
| 13 | unsicher | Prompt-Injection, Anweisungen nicht ausführen | Regeln 2, 7, 9 |
| 14 | rueckfrage | Verärgerter Mandant, Entwurf deeskaliert | Gruppen, Kanzleiton |
| 15 | bescheid | 02.11. → Fr 06.11. → So 06.12. → Ende Mo 07.12. | Fristregel 4 |
| 16 | beleg | Netto, USt, Brutto → `297,50` | Belegfelder |
| 17 | unsicher | Bescheid ohne Datum, Frist nicht berechenbar | Regel 7 |
| 18 | rueckfrage | Nur „Bitte rufen Sie mich zurück.“ | Gruppen |
| 19 | bescheid | Bescheid und Frage, Ende Fr 27.11. | Regel 7 (Vorrang) |
| 20 | beleg | Lieferant ≠ Absender, Rechnungsdatum ≠ Leistungsdatum | Belegfelder |

## Offen für Stufe 5 (Testauswertung)

- Vergleichsregeln festlegen: Muss der Lieferant exakt gleich sein, oder reicht er ohne Groß-/Kleinschreibung und ohne Rechtsform?
- Qualität der Antwortentwürfe ist nicht automatisch messbar: Prüfkriterien für einen Menschen festlegen.
- Bei Bescheiden die Spalten `bekanntgabe` und `fristende` getrennt auswerten. Dann ist sichtbar, welcher Rechenschritt falsch war.
