# Computergrundlagen 2025

## Blatt 3: Unixgrundlagen 3 und Zahlensysteme 2

- Abgabetermin für die Lösungen: **09.11.2025, 20 Uhr/ für Montagsgruppe: 07.11.2025, 12 Uhr**
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

## Zahlensysteme (2 Punkte)  
Die Schreibweise $N_{a}$ bedeutet in dieser Aufgabe, dass die Zahl $N$ in der Basis $a$ gegeben ist. Wandelt in dieser Aufgabe die gegebenen Zahlen in die Basis $b$ um (je zwei geben einen Punkt). Schreibt für jede Umwandlung einen kurzen Rechenweg auf, z.B. $100_{10\to 2} = 1100100_2$ (+Rechenweg ...).  
  
- $314_{10 \to 3}$ 
- $10011111_{2 \to 16}$ 
- $521_{6 \to 14}$ 
- $161_{7 \to 9}$   

## Herunterladen und Bearbeiten von Bildern (4 Punkte)
- Lade über das Terminal das Bild über den Link \
[``https://upload.wikimedia.org/wikipedia/commons/3/3f/Albert_Einstein_1921_by_F_Schmutzer.jpg``](https://upload.wikimedia.org/wikipedia/commons/3/3f/Albert_Einstein_1921_by_F_Schmutzer.jpg) herunter. Wie lautet der Befehl dafür?
- Um welchen Physiker handelt es sich? Nenne einen Beitrag, den er in der Physik geleistet hat.
- Das Bild ist im ``.jpg`` Format vorhanden. Konvertiere nun das Bild in das ``.png`` Format. Wie lautet der Befehl dafür?
- Wie kannst du dir die Dateigröße der beiden Bilder anzeigen lassen? Wie erklärst du den Unterschied in der Dateigröße beider Bilder?

## Dateisystem und Rechte (4 Punkte)

In einem Terminal hat der Benutzer ``pstaerk`` folgenden Dialog:

````shell
$ groups pstaerk kai cgl21-001
pstaerk : icp fluid cgl vboxusers sysguru www-data klausur stud allatom asm
kai : icp ess sysguru www-data klausur stud asm vboxusers
cgl21-001 : cgl stud

$ ls -la
total 8
drwxr-xrwx 5 pstaerk cgl  98 Nov  5 13:22 .
drwxr-xr-x 3 pstaerk icp 302 Nov  5 13:37 ..
-rw-r----- 1 pstaerk cgl 142 Nov  5 13:21 bar.txt
dr-xrwxr-x 2 pstaerk cgl  21 Nov  5 13:17 cglstuff
----rw---- 1 pstaerk cgl 142 Nov  5 13:22 foo.txt
drwxr--rwx 2 pstaerk icp   6 Nov  5 13:22 private
drwx------ 2 pstaerk icp   6 Nov  5 13:42 public
----r-x--- 1 pstaerk cgl   0 Nov  5 13:19 script.sh
````

Welche der Benutzer ``pstaerk``, ``kai`` und ``cgl21-001`` können welchen der folgenden
Befehle erfolgreich ausführen? Gebe für jeden Befehl an, welche der Benutzer ihn ausführen
können und welche nicht. Begründe deine Antworten!
Bei manchen Befehlen kann es wichtig sein, zu wissen, welche Rechte Vorrang gegenüber
anderen haben (Beispiel: Benutzerrechte sind *stärker* als Gruppenrechte).

- ``cat foo.txt``
- ``cp bar.txt cglstuff/``
- ``./script.sh``

Wie würde der folgende Befehl in Oktaldarstellung aussehen? Was könnten Vor- und Nachteile
dieser Darstellung sein?

``chmod u=rw,g=r,o= README.md``