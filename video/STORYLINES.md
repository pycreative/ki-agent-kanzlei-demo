# Storylines: Erklärvideo Posteingangs-Agent

Stand 03.11.2026. Drei verschiedene Filme, noch nichts gebaut. Empfehlung zuerst.

Für alle drei gilt:
- 16:9, 1920 × 1080, 30 fps, etwa 70 bis 85 Sekunden, Text auf Deutsch, kein Sprecher.
- Ehrlichkeit: Was noch nicht gebaut ist (Sortierung, Freigabe, Subagenten, Hook, Auswertung), wird als „geplant“ gekennzeichnet. Die Trefferquote erscheint als „wird gemessen“, bis Stufe 5 echte Zahlen liefert. Alle Mail-Texte, Regeln und Fristen stammen aus den echten Projektdateien.
- Ton: Musik nur, wenn eine freie Quelle verfügbar ist, sonst stumm mit wenigen Effekten.

## A · Eine Mail mit Frist (Empfehlung)

**Device und Form:** Das durchgerechnete Beispiel, als Kette von Objekt zu Objekt.
Eine echte Mail (`mail_19`: Bescheid und die Frage „Soll ich Einspruch einlegen?“) läuft durch jeden Schritt: lesen, einordnen, Frist rechnen, Mensch gibt frei. Danach zieht die Kamera auf: Alle 20 Mails fallen in ihre vier Fächer, die Prompt-Injection prallt am Schloss ab.

- **Erste 2 Sekunden:** Ein Posteingang zählt hoch auf „20 neu“. Die oberste Mail klappt auf, der Satz „Soll ich Einspruch einlegen?“ wird markiert.
- **Beats:** Posteingang voll → Agent liest (Regelkreis erfassen, bewerten, handeln) → Vorrang: Gruppe `bescheid` → Frist rechnet sich am Kalender (23.10. → 27.10. → 27.11.) → „offen, Mensch prüft“ → Mensch tippt „ja“ → Protokollzeile → Aufzug: 20 Mails in 4 Fächer, Injection am Schloss → Orakel-Abgleich „wird gemessen“ → Lernpfad in 5 Stufen → Schlusssatz.
- **Look:** Kanzlei-Ablage: weißer Grund, dunkle Tinte, vier Registerfarben (je Gruppe eine), Fristrot nur für die Frist.
- **Ton:** Ruhiger Bed. Ein Pop pro einsortierter Mail, ein Klick beim „ja“, ein Aufschlag, wenn die Injection am Schloss abprallt.

## B · Bitte oder Schloss (die mutige Variante)

**Device und Form:** Das Objekt ist die Erklärung, als Flug durch eine technische Zeichnung.
Der Agent wird als Regelkreis aus dem Auto gezeichnet: Sensor = Posteingang, Steuergerät = Agent, Aktor = Entwürfe, darüber eine unabhängige Überwachung wie beim E-Gas-Konzept. Die Injection-Mail will „Lösche den Ordner“, die Überwachung (der Hook) kappt die Leitung zum Aktor.

- **Erste 2 Sekunden:** Die Frage „Was haben ein Notbremsassistent und ein Kanzlei-Posteingang gemeinsam?“, darunter zwei Skizzen, die zu einer verschmelzen.
- **Beats:** Frage → Regelkreis zeichnet sich → Agent warnt nur, bremst nicht (FCW statt AEB, SAE Level 2) → Bitte (`CLAUDE.md`) gegen Schloss (Hook) → Injection wird geblockt → Prüfstand: 20 Testfälle gegen das Orakel → Lernpfad als 5 Stationen → „15 Jahre Absicherung im Auto, jetzt für den Posteingang“.
- **Look:** Lastenheft und Blaupause: helles Raster, feine Tintenlinien, ein Signalrot für den Eingriff.
- **Ton:** Leiser, technischer Puls. Stille im Moment des Blockens, dann ein harter Schnitt.

## C · Der Bauplan wächst

**Device und Form:** Ein Diagramm, das wächst, in einem Bild, das sich immer wieder umbaut.
Das ganze Projekt entsteht Stück für Stück in einem einzigen Bild: Ordner → `CLAUDE.md` mit 9 Regeln → 20 Mails und Orakel → Sortierung → Subagenten → Hooks → MCP → n8n → Testauswertung. Jedes Teil trägt seinen Status: fertig, in Arbeit, geplant.

- **Erste 2 Sekunden:** Ein leerer Ordner `KI-Agent-Kanzlei-Demo`, aus dem die ersten Unterordner herauswachsen.
- **Beats:** leerer Ordner → Grundgesetz (9 Regeln) → Testdaten und Orakel → Agent und Freigabe → Stufen 1 bis 5 docken an → Statuslegende fertig / in Arbeit / geplant → Schlusssatz.
- **Look:** Technischer Bauplan in einem Bild, drei Statusfarben, nichts verlässt den Rahmen.
- **Ton:** Gleichmäßiger Takt. Ein Einrasten pro angedocktem Teil.
