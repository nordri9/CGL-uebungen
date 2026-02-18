#include <iostream>
#include <vector>
#include <cstdlib> // for rand(), srand()
#include <ctime>   // for time()

class Particle
{
public:
    std::vector<double> position;
    std::vector<double> speed;
    double mass;

    Particle(std::vector<double> pos, std::vector<double> spd, double m)
        : position(pos), speed(spd), mass(m) {}

    double momentum_x() const
    {
        return mass * speed[0];
    }

    double momentum_y() const
    {
        return mass * speed[1];
    }

    void print(int index) const
    {
        std::cout << "Particle" << index << ": "
                  << "Pos: (" << position[0] << ", " << position[1] << "), "
                  << "Mass: " << mass << ", "
                  << "Momentum X: " << momentum_x() << ", "
                  << "Momentum Y: " << momentum_y()
                  << std::endl;
    }
};

double randomDouble()
{
    return (double)std::rand() / RAND_MAX;
}

int main()
{
    std::srand(std::time(0));

    std::vector<Particle> particles;
    int num_particles = 10;

    for (int i = 0; i < num_particles; ++i)
    {
        double px = randomDouble() * 100.0;
        double py = randomDouble() * 100.0;
        double vx = randomDouble() * 10.0;
        double vy = randomDouble() * 10.0;
        double mass = 1.0 + randomDouble() * 5.0;

        particles.emplace_back(std::vector<double>{px, py},
                               std::vector<double>{vx, vy},
                               mass);
    }

    for (int i = 0; i < particles.size(); ++i)
    {
        particles[i].print(i + 1);
    }

    return 0;
}
