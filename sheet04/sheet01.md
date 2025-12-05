# Computergrundlagen 2025
## Blatt 1: Unixgrundlagen

- Abgabetermin für die Lösungen: **26.10.2025, 20 Uhr/ für Montagsgruppe: 23.10.2025, 12 Uhr**
- Bei Fragen wendet euch bitte an eure/n Tutor/in:
    * Mo 11:30: Stephan Haag: `st170833@stud.uni-stuttgart.de`
    * Di 09:45: Julian Hoßbach: `julian.hossbach@icp.uni-stuttgart.de`
    * Mi 14:00: Julian Peters: `julian.peters@icp.uni-stuttgart.de`
    * Do 09:45: Rebecca Stephan: `rebecca.stephan@icp.uni-stuttgart.de`
    * Fr 09:45: Jonas Höpker: `st182335@stud.uni-stuttgart.de`
* Die Übungsaufgaben sollen in der Regel in **Zweiergruppen** bearbeitet werden. Nur in **begründeten Ausnahmefällen** sind Dreiergruppen möglich.
* Die Abgabe der Übungsblätter erfolgt über Ilias.
* Die ausgeführten Befehle sollen als Teil der Lösung abgegeben werden.
* Mit Abgabe der Lösungen erklärt Ihr, dass Ihr die Lösung euren Mitstudierenden im Rahmen der Übungsbesprechung vorstellen könnt. Um dies zu überprüfen, muss mindestens zweimal von jedem Teilnehmenden vorgetragen werden. Wenn Ihr das nicht könnt, werden euch die Punkte für die entsprechenden Aufgaben wieder abgezogen.


## Navigation mit der Kommandozeile (4 Punkte)
Die Kommandozeile ``bash`` ist ein häufig genutztes Tool um schnell durch Ordner zu navigieren oder Befehle auszuführen. Als erste Aufgabe sollst du mit der Kommandozeile 

- das aktuelle Arbeitsverzeichnis anzeigen.
- alle Dateien im aktuellen Verzeichnis anzeigen.
- einen Ordner `Computergrundlagen` in deinem ``$HOME`` Verzeichnis anlegen.
- in den Ordner ``Computergrundlagen`` wechseln.
- dir den Inhalt des ``root`` sowie des ``$HOME`` Verzeichnis anzeigen lassen, ohne in dieses Verzeichnis zu wechseln.
- in das Verzeichnis `etc` wechseln, das sich im Root-Verzeichnis befinet

Fügt eurer Abgabe eine Kopie des Terminals nach Ausführung der Befehle hinzu.

## Arbeiten mit Dateien und Verzeichnissen (4 Punkte)
- Gehe in den zuvor erstellten Ordner `Computergrundlagen` und erzeuge eine Datei ``directory.txt``, die den Inhalt des aktuellen Verzeichnis enthält. Der Inhalt der Datei soll dabei nicht manuell eingefügt, sondern automatisch erzeugt werden. (Hinweis: Nutze `befehl > datei` um die Ausgabe eines Befehls in eine Datei zu speichern)
- Wie kannst du den Inhalt der erstellten Datei ohne einen Texteditor anzeigen lassen?
- Erstelle nun eine Kopie ``directory_copy.txt`` der erstellten Datei im selben Verzeichnis.
- Verschiebe die Kopie in dein ``$HOME`` Verzeichnis und ändere dabei ihren Namen zu ``directory.txt``.
- Wechsle nun in deinen ``$HOME`` Verzeichnis (ohne die Verwendung von absoluten Pfaden!) und lösche die eben verschobene Datei ``directory.txt``.
- Erstelle eine Kopie des erstellten Verzeichnisses `Computergrundlagen` und lösche es anschließend wieder.

Fügt eurer Abgabe eine Kopie des Terminals nach Ausführung der Befehle hinzu.

## Hilfe für Befehle und Pipes (2 Punkt)
- Erkläre, was passiert, wenn man den Befehl ``man man`` ausführt.
- Führe den Befehl ``man man | wc`` aus und erkläre die Ausgabe. Was passiert, wenn man stattdessen ``man man | wc | wc`` ausführt?
