#include <iostream>
#include <vector>
#include <algorithm>
#include "stdio.h"

using namespace std;

int N;
int K;

int triangle[3000][3000];

int get_triangle(int r, int c, int size, int triangle[][3000])
{
    int max_val = 0;

    for (int i = 0; i < size; ++i)
    {
        for (int j = 0; j < i + 1; ++j)
        {
            max_val = max(max_val, triangle[i + r][j + c]);
        }
    }

    return max_val;
}

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> K;

    int temp = 1;
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < temp; ++j)
        {
            cin >> triangle[i][j];
        }

        temp += 1;
    }

    int ans = 0;
    for (int i = 0; i < N - K + 1; ++i)
    {
        for (int j = 0; j < i + 1; ++j)
        {
            ans += get_triangle(i, j, K, triangle);
        }
    }

    cout << ans;

    return 0;
}