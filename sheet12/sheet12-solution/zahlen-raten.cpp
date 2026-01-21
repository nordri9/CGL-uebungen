#include <iostream>
#include <time.h>
using namespace std;

int main(int argc, char *argv[])
{
    srand(time(NULL));
    int maximum;
    int guess;
    int guess_count = 0;
    int random_number;
    cout << "Maximum: ";
    cin >> maximum;
    random_number = rand() % maximum;
    // cout << random_number << endl;

    while (guess != random_number)
    {
        cout << "input guess: ";
        cin >> guess;
        if (guess < random_number)
        {
            cout << "to small" << endl;
        }
        else if (guess > random_number)
        {
            cout << "to big" << endl;
        }
        guess_count++;
    }
    cout << "number of guesses: " << guess_count << endl;
    cout << "yay correct" << endl;
    return 0;
}