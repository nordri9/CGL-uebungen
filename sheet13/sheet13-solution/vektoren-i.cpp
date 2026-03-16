#include <iostream>
#include <vector>
using namespace std;

double sum_below_limit(const vector<double> &vector0, double limit)
{
    double summ = 0.0;
    for (int i : vector0)
    {
        if (i < limit)
        {
            summ += i;
        }
    }
    return summ;
}
int main()
{
    vector<double> v = {1.0, 2.0, 3.0, 4.0, 5.0, 42.0};
    cout << sum_below_limit(v, 4.0) << "\n";
    return 0;
}
