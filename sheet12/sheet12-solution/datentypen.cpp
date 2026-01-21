#include <string>
#include <cmath>
#include <iostream>
using namespace std;

int main()
{
    int a = 3 + 5;
    int b = 3 + 5.0;
    string c = string("3") + string("5");
    string d = string("3") + "5";
    int e = 3 / 2;
    float f = 3.0 / 2;
    int g = int(2.71828);
    int h = std::round(2.71828);
    cout
        << a << endl
        << b << endl
        << c << endl
        << d << endl
        << e << endl
        << f << endl
        << g << endl
        << h << endl;
}
