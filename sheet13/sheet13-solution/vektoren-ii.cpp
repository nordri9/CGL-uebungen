#include <iostream>
#include <vector>
using namespace std;

double scalar_product(const vector<double> &vector1,
                      const vector<double> &vector2)
{
    double summ = 0;
    if (vector1.size() != vector2.size())
    {
        return 1;
    }

    for (int i = 0; i < vector1.size(); i++)
    {
        summ += vector1[i] * vector2[i];
    }
    return summ;
}
int main()
{
    vector<double> v1 = {1.0, 2.0, 3.0, 4.0, 5.1};
    vector<double> v2 = {1.0, -1.0, -1.0, 1.0};
    cout << scalar_product(v1, v2) << "\n";
    return 0;
}