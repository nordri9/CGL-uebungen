#include <iostream>
#include <vector>
#include <algorithm> // Tipp: max_element könnte hilfreich sein
using namespace std;

vector<double> normalize_vector(const vector<double> &input_vec)
{
    if (input_vec.empty())
    {
        cout << "vector is empty!!!" << endl;
        return {};
    }

    // 1. Finde das Maximum im Vektor
    // (Falls der Vektor leer ist, gib einen leeren Vektor zurück)
    double max_val = *max_element(input_vec.begin(), input_vec.end());
    if (max_val == 0)
    {
        cout << "vctor is zero!!!" << endl;

        return {};
    }

    // 2. Erstelle einen neuen Vektor für die Ergebnisse
    vector<double> result;
    for (int i = 0; i < input_vec.size(); i++)
    {
        result.push_back(input_vec[i] / max_val);
    }

    // 3. Berechne die normalisierten Werte und füge sie 'result' hinzu
    return result;
}
int main()
{
    vector<double> v = {2.0, 5.0, 10.0, 4.0};
    // vector<double> v1 = {0.0, 0.0, 0.0};
    // vector<double> v2 = {};

    vector<double> normalized = normalize_vector(v);
    // Ausgabe der neuen Werte
    for (double val : normalized)
    {
        cout << val << " ";
    }
    cout << endl;
    return 0;
}