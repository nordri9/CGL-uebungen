# Computergrundlagen 2025

## Blatt 2: Unixgrundlagen 2 und Zahlensysteme 1

- Abgabetermin für die Lösungen: **02.11.2025, 20 Uhr/ für Montagsgruppe: 31.10.2025, 12 Uhr**
- Bei Fragen wendet euch bitte an eure/n Tutor/in:
    - Mo 11:30: Stephan Haag: `st170833@stud.uni-stuttgart.de`
    - Di 09:45: Julian Hoßbach: `julian.hossbach@icp.uni-stuttgart.de`
    - Mi 14:00: Julian Peters: `julian.peters@icp.uni-stuttgart.de`
    - Do 09:45: Rebecca Stephan: `rebecca.stephan@icp.uni-stuttgart.de`
    - Fr 09:45: Jonas Höpker: `st182335@stud.uni-stuttgart.de`
- Die Übungsaufgaben sollen in der Regel in **Zweiergruppen** bearbeitet werden. Nur in **begründeten Ausnahmefällen** sind Dreiergruppen möglich.
- Die Abgabe der Übungsblätter erfolgt über Ilias.
- Die ausgeführten Befehle sollen als Teil der Lösung abgegeben werden.
- Mit Abgabe der Lösungen erklärt Ihr, dass Ihr die Lösung euren Mitstudierenden im Rahmen der Übungsbesprechung vorstellen könnt. Um dies zu überprüfen, muss mindestens zweimal von jedem Teilnehmenden vorgetragen werden. Wenn Ihr das nicht könnt, werden euch die Punkte für die entsprechenden Aufgaben wieder abgezogen.
- **Befehle, die nicht in der Vorlesung besprochen wurden, müssen gegebenenfalls recherchiert werden.**

## Durchsuchen von Dateien und Verzeichnissen (4 Punkte)
- Wie lautet der Befehl, um aus dem Homeverzeichnis heraus den Inhalt des Ordners ``/etc`` aufzulisten?
- Aus wie vielen Zeilen besteht die Datei ``/etc/services``? Mit welchem Befehl kann man das herausfinden?
- Gebe an, wie viele Dateien und Verzeichnisse (Unterverzeichnisse ausgeschlossen) sich in dem Ordner ``/etc`` befinden. Wie lautet der Befehl dafür?
- Finde alle Dateien in ``/etc``, deren Name mit ``.conf`` enden. Speichere alle gefundenen Namen in eine neue Datei namens ``all_config_files``.

## Prozesssteuerung (3 Punkte)

In dieser Aufgabe verwenden wir die bereitgestellten Skripte ``papagei.sh`` und ``tick-tock.sh`` um die Steuerung von Prozessen zu untersuchen. (Hinweis: Im Folgenden sind mit ``Ctrl-Z`` und ``Ctrl-C`` Tastenkombinationen und keine Zeichenfolgen gemeint.)

- Das Skript ``papagei.sh`` gibt, ähnlich wie ein Papagei, eine eingegebene Zeichenfolge nach dem Drücken der Return-Taste wieder aus. Führe das Skript aus und gebe anschließend die folgende Befehlskette ein. Erkläre, was in jedem der Schritte passiert. Denke auch daran, dass du die richtigen Rechte vergeben musst, damit das Skript ausführbar ist.

	````shell
	ls
	Ctrl-Z
	ls
	fg
	ls
	Ctrl-C
	````

- Das Skript ``tick-tock.sh`` simuliert eine Uhr, die einmal pro Sekunde tickt. Starte das Skript und führe die folgende Befehlskette aus. Erkläre deine Beobachtungen.

	````shell
	Ctrl-Z
	bg
	Ctrl-C
	fg
	Ctrl-C
	````

- Wie kannst du die Uhr von Anfang an im Hintergrund laufen lassen? Welche Befehle musst du ausführen, um den Prozess wieder zu beenden?

## Fließkommazahlen (3 Punkte)  

Ganzzahlen speichert der Computer wie oben im Zweiersystem. Da in der Physik viele Größen jedoch kontinuierliche Werte annehmen können, sind Gleitkomma- oder Fließkommazahlen für uns mindestens genau so wichtig. Während das Zweiersystem Ganzzahlen exakt abbildet, sind Fließkommazahlen nur aus zwei Ganzzahlen bestehende Näherungen für reelle Zahlen. Dies bringt in der Praxis einige Probleme mit sich, die wir hier anhand von Beispielen beleuchten.  
  
Üblicherweise werden Fließkommazahlen nach dem IEEE 754-Standard gespeichert. Wir verwenden im Folgenden 32 Bit pro Zahl, was `single precision` genannt wird. Die 32 Bit werden wie folgt verwendet:  
- 8 Bit für den Exponenten als Ganzzahl $p$, wobei vor der Speicherung sogenannte `Bias`-wert $B=127$ addiert wird.
- 23 Bit für die Mantisse als Ganzzahl $m$, wobei vor der Speicherung $1$ abgezogen wird.
- 1 Bit $s$ für das Vorzeichen der Mantisse. 

Die so gespeicherte Zahl hat dann den Wert  
$$x = (-1)^s (1+m) 2^{p-B}. $$
  
Der Exponent kann nur Werte aus $\left[-126,127\right]$ annehmen, weil $p-B=0$ und $p-B=255$ für Sonderfälle reserviert sind.  
Die Mantisse kann Werte aus $\left[1,2\right)$ annehmen.  
Genaue Erläuterungen finden sich z.B. bei [Wikipedia](https://de.wikipedia.org/wiki/IEEE_754).  

- Was sind die betragsmäßig und absolut kleinsten und größten Zahlen, die man so darstellen kann (abgesehen von der Null)? Gebt sie als Zweierpotenzen an und begründet eure Antwort. Rechnet sie ins Dezimalsystem um, und bestimmt, wie viele signifikante Stellen eine so dargestellte Zahl hat.
- Gebt die Bit-Darstellung der Zahl $3.14159$ im IEEE 754-Standard an und zeigt, wie ihr diese bestimmt habt.

