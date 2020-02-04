#include <iostream>

int G;
int P;

int planes[100000];
int gates[100000] = {};

using namespace std;

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    cin >> G >> P;

    for (int i = 0; i < P; ++i)
    {
        int temp;
        cin >> temp;
        planes[i] = temp;
    }

    int len = 0;

    for (int i = 0; i < P; ++i)
    {
        int plane = planes[i];
        int fit = 0;
        for (int j = plane; j > 0; --j)
        {
            if (gates[j - 1] == 0)
            {
                gates[j - 1] = plane;
                len += 1;
                fit = 1;
                break;
            }
        }
        if (fit == 0)
        {
            break;
        }
    }

    cout << len;

    return 0;
}