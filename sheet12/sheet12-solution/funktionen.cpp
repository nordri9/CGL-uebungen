#include <iostream>
using namespace std;

bool pruefeTipp(int tipp, int loesung)
{
    if (tipp == loesung)
    {
        cout << "Treffer! Gut gemacht." << endl;
        return true; // Rückgabe für Erfolg
    }
    else if (tipp > loesung)
    {
        cout << "Zu hoch!" << endl;
    }
    else
    {
        cout << "Zu niedrig!" << endl;
    }
    return false; // Rückgabe für "noch nicht gefunden"
}

int main()
{
    int secret = 42;
    int guess;
    bool gefunden = false;

    cout << "Willkommen zum Zahlen-Raten!" << endl;

    while (!gefunden)
    {
        cout << "Dein Tipp: ";
        cin >> guess;

        gefunden = pruefeTipp(guess, secret);
    }
    return 0;
}