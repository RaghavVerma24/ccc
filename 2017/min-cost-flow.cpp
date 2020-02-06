#include <iostream>

int N;
int M;
int D;

int pipes[200000][3];

int start_cost = 0;

int main()
{
    std::cin.sync_with_stdio(0);
    std::cin.tie(0);

    std::cin >> N >> M >> D;

    for (int i = 0; i < M; ++i)
    {
        int temp[3];
        std::cin >> temp[0] >> temp[1] >> temp[2];

        pipes[i][0] = temp[0];
        pipes[i][1] = temp[1];
        pipes[i][2] = temp[2];

        if (i < N - 1)
        {
            start_cost += temp[2];
        }
    }

    for (int i = N; i < M; ++i)
    {
        }

    return 0;
}