GOAL:    Der Zuschauer versteht, warum eine Regel im Text nur eine Bitte ist und erst ein Hook ein Schloss, erklärt mit dem Regelkreis aus dem Auto.
OUTPUT:  HyperFrames, 1920 x 1080, 30 fps
TIME:    78 s x 30 = 2340 Frames. Keine Musik, nur Effekte aus assets/sfx (Pixabay).
LOOK:    Lastenheft und Blaupause. Grund #EEF3F8 mit Raster #D6E0EB alle 48 px (1 px), Tinte Kobalt #173F7A, leise Tinte #5E7391,
         Linien 4 px. Signalrot #D62828 nur für Eingriff und Blockade. Erlaubt #2E7D4F nur für den durchgelassenen Aufruf.
         Display Oswald 600/700, 52–104 px. Text Roboto 400/500, 28–44 px. Code Source Code Pro 400, 28–32 px.
         Kästen: Grund #F8FAFD, Rand 4 px Tinte, Radius 6 px. Kein Schatten, kein Korn.
OBJECTS: Auto in Seitenansicht mit Radarkegel, Ablagekorb mit Briefen, Regelkreis (Sensor, Steuergerät, Aktor, Rückführung, Mensch),
         CLAUDE.md-Blatt, Injection-Mail, Waage im Agenten, Schranke mit Hook-Kasten, Prüfstand-Tabelle, Leiter mit 5 Sprossen.
MOTION:  Linien zeichnen sich (strokeDashoffset, power2.inOut 0.8 s). Ankunft expo.out 0.5 s, Abgang power3.in 0.3 s.
         Zoom durch das Steuergerät in Szene 3. Schranke fällt power4.in 0.25 s.
SHOTS:   b1 0–10 s    Frage „Was haben ein Notbremsassistent und ein Kanzlei-Posteingang gemeinsam?“, Auto und Ablage nebeneinander.
         b2 10–26 s   Regelkreis zeichnet sich: Sensor = Posteingang, Steuergerät = Agent, Aktor = Entwürfe. Bremse → Warnung (FCW). Mensch darüber (SAE Level 2). Zoom ins Steuergerät.
         b3 26–41 s   Agent bekommt CLAUDE.md (Bitte) und mail_13 (Daten). Waage schwankt. „Eine Regel im Text ist eine Bitte.“ Doku-Zitat.
         b4 41–56 s   Schranke mit PreToolUse-Hook: rm -r mails/eingang wird blockiert (Exit-Code 2), Schreiben nach ausgabe/ wird durchgelassen.
         b5 56–66 s   Prüfstand: 6 der 20 Testbedingungen mit Sollwert, Ist „?“, „Trefferquote: wird gemessen“.
         b6 66–78 s   Leiter mit 5 Stufen (geplant), dann „15 Jahre Systems Engineering im Auto. Jetzt für den Posteingang.“
BANNED:  dunkler Grund, Glühen, Verläufe als Look, alles mittig, alles gleitet hoch, drei Karten als Selbstzweck, Logo in der Ecke,
         erfundene Ergebnisse, Behauptungen über nicht gebaute Teile ohne „geplant“.
QA:      5 s (Frage lesbar), 20 s (Regelkreis komplett mit Mensch), 35 s (Waage, Bitte und Daten), 46 s (blockiert), 52 s (erlaubt), 62 s (Tabelle), 76 s (Schlusssatz).
