#include <iostream>
#include <time.h>
int main(int argc, char *argv[])
{
    srand(time(NULL));
    int maximum;
    int guess;
    int guess_count = 0;
    int random_number;
    std::cout << "Maximum: ";
    std::cin >> maximum;
    random_number = rand() % maximum;
    while (guess != random_number)
    {
        std::cin >> guess;

        if (guess > random_number)
        {
            std::cout << "to big" << std::endl;
        }
        else
        {
            std::cout << "to small" << std::endl;
        }
        guess_count++;
    }
    std::cout << "yay" << guess_count << std::endl;
    return 0;
}