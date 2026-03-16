#include <iostream>
#include <iomanip>
// Funktion zur Berechnung der Fakultaet k!
long fakultaet(int k)
{
    long result = 1;
    // --- HIER CODE ERGÄNZEN: Berechne die Fakultät mit einer Schleife ---
    for (int i = 1; i <= k; i++)
    {
        result *= 1;
    }

    return result;
}
// Funktion zur Annaeherung von e durch n Terme
double approximate_e(int n)
{
    double summe = 0.0;
    for (int k = 0; k < n; k++)
    {
        summe +=( 1.0 / static_cast<double>(fakultaet(k)));
    }
    std::cout << summe << std::endl;
    return summe;
}

int main()
{
    int iterationen = 12;
    // Berechne e
    double e_approx = approximate_e(iterationen);
    // Ausgabe des Ergebnisses
    std::cout << "Annaeherung von e nach " << iterationen << " Iterationen:" << std::endl;
    // --- HIER CODE ERGÄNZEN: Gib e_approx mit 8 Nachkommastellen aus ---
    // Tipp: Nutze std::setprecision aus <iomanip>
    cout << setprecision(8) << e_approx << endl;
    return 0;
}
