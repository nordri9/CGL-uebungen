#include <iostream>
// --- HIER DIE FUNKTION DEFINIEREN ---
bool pruefeTipp(int tipp, int loesung)
{
    if (tipp == loesung)
    {
        std::cout << "Treffer! Gut gemacht." << std::endl;
        return true; // Rückgabe für Erfolg
    }
    else if (tipp > loesung)
    {
        std::cout << "Zu hoch!" << std::endl;
    }
    else
    {
        std::cout << "Zu niedrig!" << std::endl;
    }
    return false; // Rückgabe für "noch nicht gefunden"
}
int main()
{
    int secret = 42; // Beispiel-Zufallszahl
    int guess;
    bool gefunden = false;
    std::cout << "Willkommen zum Zahlen-Raten!" << std::endl;
    while (!gefunden)
    {
        std::cout << "Dein Tipp: ";
        std::cin >> guess;
        // --- HIER DEN FUNKTIONSAUFRUF EINFÜGEN ---
        gefunden = pruefeTipp(guess, secret);
    }
    return 0;
}