#include <iostream>
using namespace std;
const int TEST = 4;

int main()
{
    cout << "Hello" << endl;
    for (int i = 0; i < 10; i++)
    {
        cout << i;

        cout << TEST + 1;
    }
}