#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

// int get_triangle(int r, int c, int size, std::vector<std::vector<int>> triangle)
int get_triangle(int r, int c, int size, int triangle[][1000])
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

    int N;
    int K;

    // std::vector<std::vector<int>> triangle;
    int triangle[1000][1000];

    // cin >> N >> K;
    scanf("%d", &N);
    scanf("%d", &K);

    int temp = 1;
    for (int i = 0; i < N; ++i)
    {
        // std::vector<int> temp3;
        for (int j = 0; j < temp; ++j)
        {
            int temp2;
            scanf("%d", &temp2);
            triangle[i][j] = temp2;
            // temp3.push_back(temp2);
        }

        // triangle.push_back(temp3);

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

    printf("%d", ans);

    // for (auto row : triangle)
    // {
    //     for (auto el : row)
    //     {
    //         cout << el << " ";
    //     }
    //     cout << "\n";
    // }

    return 0;
}