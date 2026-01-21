#include <iostream>
#include <iomanip>
using namespace std;
// Funktion zur Berechnung der Fakultaet k!
unsigned long fakultaet(int k)
{
    unsigned long result = 1;
    for (int i = 1; i <= k; i++)
    {
        result *= i;
    }
    return result;
}
// Funktion zur Annaeherung von e durch n Terme
double approximate_e(int n)
{
    double summe = 0.0;
    for (int k = 0; k < n; ++k)
    {
        summe += (1.0 / static_cast<double>(fakultaet(k)));
        // cout << summe << endl;
        //  --- HIER CODE ERGÄNZEN: Addiere 1.0 / k! zur Summe ---
        //  Hinweis: Nutze die Funktion fakultaet(k)
    }
    return summe;
}
int main()
{
    int iterationen = 20;
    // Berechne e
    double e_approx = approximate_e(iterationen);
    // Ausgabe des Ergebnisses
    cout << "Annaeherung von e nach " << iterationen << " Iterationen:" << endl;
    cout << setprecision(8) << e_approx << endl;
    // --- HIER CODE ERGÄNZEN: Gib e_approx mit 8 Nachkommastellen aus ---
    // Tipp: Nutze setprecision aus <iomanip>
    return 0;
}