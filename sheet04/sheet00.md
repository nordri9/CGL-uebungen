# Computergrundlagen 2025
### Allgemeine Hinweise zu den Übungen

* Die Übungsaufgaben sollen in der Regel in **Zweiergruppen** bearbeitet werden. Nur in **begründeten Ausnahmefällen** sind Dreiergruppen möglich. Dieses Blatt is eine Ausnahme und soll alleine bearbeitet und abgegeben werden.
* Ab nächstem Übungsblatt wird jedes Blatt Punkte geben.
* Zudem wird es **2-3 Kurztests** während des Semesters geben, die ca. 15% der Gesamtpunktzahl ausmachen werden.
* Um den **Übungsschein** zu erhalten (dies ist die Voraussetzung für die Zulassung zur Klausur), müssen **alle** folgenden Bedingungen **unabhängig voneinander** erfüllt sein:
    * **Mindestens 66 %** aller erreichbaren Gesamtpunkte.
    * **Mindestens 50 %** der Punkte auf **jedem** einzelnen Übungsblatt.
    * **Mindestens zweimaliges Vortragen** der Lösung einer Aufgabe in der Übungsgruppe.
    * **Regelmäßige Teilnahme** an den Übungen und Unterschrift in der Anwesenheitsliste (Krankmeldungen o. Ä. sind dem jeweiligen Tutor mitzuteilen).
* Die Übungsblätter müssen spätestens am **Sonntag um 20:00 Uhr** vor der nächsten Übung abgegeben werden. **Ausnahme:** Für die Übungsgruppe am Montag um 11:30 Uhr ist die Abgabe bereits am **Freitag um 12:00 Uhr**.
* Die Abgabe der Übungsblätter erfolgt über Ilias.

### Kontakte der Tutorinnen und Tutoren

Bei Fragen wendet euch bitte an eure/n Tutor/in:

* Mo 11:30: Stephan Haag: `st170833@stud.uni-stuttgart.de`
* Di 09:45: Julian Hoßbach: `julian.hossbach@icp.uni-stuttgart.de`
* Mi 14:00: Julian Peters: `julian.peters@icp.uni-stuttgart.de`
* Do 09:45: Rebecca Stephan: `rebecca.stephan@icp.uni-stuttgart.de`
* Fr 09:45: Jonas Höpker: `st182335@stud.uni-stuttgart.de`


## Blatt 0: Unix-Grundlagen – Einführung in die Befehlszeile

Dieses Arbeitsblatt dient der **Einführung** in die Grundlagen von Unix. Es unterscheidet sich von den regulären Übungsblättern des Semesters:

* Es soll **einzeln** bearbeitet werden.
* Es wird **nicht** zur benötigten Gesamtpunktzahl für den Übungsschein gezählt.
* Die Bearbeitung findet **in Präsenz** statt.

### 1. Einrichtung einer Unix-Befehlszeile

Ziel dieser Aufgabe ist es, eine **funktionsfähige Unix-Befehlszeile** einzurichten, die ihr für die weiteren Aufgaben dieses Semesters nutzen könnt.

Hierfür gibt es mehrere empfohlene Möglichkeiten:

1.  **Windows Subsystem for Linux (WSL):** Dies ist die **einfachste Variante für Windows-Nutzer**. WSL stellt eine Kernelschnittstelle zu einer Linux-Distribution (z. B. Ubuntu) bereit. Es kann kostenfrei über den Microsoft Store heruntergeladen werden. Eine offizielle Anleitung findet ihr hier: [Windows-Subsystem für Linux](https://learn.microsoft.com/de-de/windows/wsl/)
2.  **Native Unix-basierte Betriebssysteme:** Ihr könnt direkt ein Unix-basiertes System wie **Linux** (verschiedene Distributionen) oder **macOS** verwenden.
3.  **Dual-Boot-Installation:** Eine fortgeschrittene Option ist die **Neuinstallation** eines Unix-Betriebssystems (wie Linux) zusätzlich zu eurer bestehenden Windows-Installation (sogenannter **Dual-Boot**). Anleitungen dazu sind online verfügbar; das Vorgehen ist jedoch komplexer als die Verwendung von WSL.

> **Freiwillige Abgabe:** Tragt bitte in die Abgabe-Datei ein, welche Variante ihr für eure Unix-Befehlszeile nutzt. Solltet ihr dabei auf Schwierigkeiten gestoßen sein, beschreibt diese ebenfalls kurz.

### 2. Grundlegende Unix-Befehle

Führt folgende Schritte in eurer Unix-Befehlszeile durch:

1.  Erstellt einen Ordner namens `Computergrundlagen` in eurem ``$HOME``-Verzeichnis mithilfe des Befehls `mkdir`.
2.  Wechselt in den neu erstellten Ordner. (*Tipp: Die **Tabulator-Taste** kann zur Autovervollständigung sehr hilfreich sein.*)
3.  Führt in diesem Ordner die folgenden Befehle nacheinander aus:

    ```shell
    echo "Hello World!"
    echo "Hello World!" >> HelloWorld.txt
    ```

**Fragen zur Bearbeitung:**

* Lasst euch die Inhalte des aktuellen Ordners anzeigen. Was fällt auf?
* Erklärt in eigenen Worten, was die zweite Befehlszeile gemacht hat.
* Überprüft eure Vermutung mit dem Befehl `cat`.

### Bonus: Remote-Zugriff auf die CIP-Rechner

Die CIP-Rechner der Universität können aus dem Uni-Netzwerk heraus genutzt werden (von außerhalb ist hierfür ein [VPN](https://www.tik.uni-stuttgart.de/support/anleitungen/vpn/) erforderlich).

Dies ermöglicht euch, alle Übungen zu bearbeiten, ohne dass ihr zwingend etwas auf eurem eigenen PC installieren müsst.

Um ein Terminal auf einem CIP-Rechner zu öffnen, nutzt den folgenden Befehl:

```shell
ssh -J <username>@ssh.icp.uni-stuttgart.de <username>@cip1
```
Dieser öffnet ein Terminal auf dem Rechner `cip1`.
Du kannst Dir den Namen Deines Gerätes merken und `cip1` beispielsweise auch durch `cip20` ersetzen.
Um Dateien zu kopieren, bietet sich der Befehl `scp` an.
Alternativ gibt es das Tool [WinSCP](https://winscp.net/eng/index.php), welches eine grafische Benutzeroberfläche zur Verfügung stellt. Bei weiteren Fragen wende Dich hierzu an Deinen Tutor bzw. Deine Tutorin.
