#include <string>
#include <iostream> // Ein- und Ausgabebibliothek

int main()
{                                                       // Hauptfunktion
    std::cout << "Hallo, du schöne Welt!" << std::endl; // Ausgabe eines Textes
    unsigned int s = 0;
    for (int i = 0; i <= 10; i++)
    {
        s +=i;
        std::cout << s << std::endl;
    }
// int i =1.2;
    return 0;
}