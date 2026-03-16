#include <iostream>

using namespace std;

class Particle
{
public:
    double x, y, vx, vy, m;
    double p_x(double vx, double m)
    {
        return vx * m;
    }

    double p_y(double vy, double m)
    {
        return vy * m;
    }
};

int main()
{
    Particle neutron(1, 2, 3, 4, 5);
    cout << neutron.p_x() << endl;
    return 0;
}