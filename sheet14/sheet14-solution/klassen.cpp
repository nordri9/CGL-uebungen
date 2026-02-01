#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

class Particle
{
public:
    std::vector<double> position;
    std::vector<double> speed;
    double mass;
    std::vector<double> impulse(const std::vector<double> &speed)
    {
        std::vector<double> impulse = {mass * speed[0], mass * speed[1]};
        return impulse;
    }
};

// 2. Helper function to get random double between 0.0 and 1.0
double randomDouble()
{
    return (double)std::rand() / RAND_MAX;
}

int main(int argc, char const *argv[])
{

    // Seed the random number generator once
    std::srand(std::time(0));

    // Vector to store particles
    std::vector<Particle> particles;
    int num_particles = 5;

    // std::vector<Particle> test_particles = { {{std::rand() % 1, {std::rand() % 1}, {23, 3}, 4}};
    //  std::cout << test_particles[0] << std::endl;
    return 0;
}
