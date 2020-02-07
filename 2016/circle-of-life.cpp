#include <iostream>
#include <vector>
#include <map>
#include <string>

int N;
int T;

int main()
{

    std::cin.sync_with_stdio(0);
    std::cin.tie(0);

    std::cin >> N >> T;

    int state[N];

    std::string tempstr;
    std::cin >> tempstr;

    for (int i = 0; i < N; ++i)
    {

        state[i] = tempstr[i];
    }

    int first_gen[N];
    int cycles_to_go = 0;

    int generation = 0;
    while (generation < T)
    {
        if (generation > 1 && std::equal(state, state + N - 1, first_gen))
        {
            int len_cycle = generation - 1;
            cycles_to_go = (T - 1) % len_cycle;
            break;
        }
        else
        {
            int temp[N];
            std::copy(state, state + N - 1, temp);

            for (int i = 0; i < N; ++i)
            {
                int left;
                int right;

                if (i == 0)
                {
                    left = N - 1;
                    right = i + 1;
                }
                else if (i == N - 1)
                {
                    left = i - 1;
                    right = 0;
                }
                else
                {
                    left = i - 1;
                    right = i + 1;
                }

                if ((state[left] == 1 and state[right] == 0) || (state[left] == 0 and state[right] == 1))
                {
                    temp[i] = 1;
                }
                else
                {
                    temp[i] = 0;
                }
            }

            generation += 1;
            std::copy(temp, temp + N - 1, state);

            if (generation == 1)
            {
                std::copy(state, state + N - 1, first_gen);
            }
        }
    }

    if (cycles_to_go > 0)
    {
        for (int i = 0; i < cycles_to_go; ++i)
        {
            int temp[N];
            std::copy(state, state + N - 1, temp);

            for (int i = 0; i < N; ++i)
            {
                int left;
                int right;

                if (i == 0)
                {
                    left = N - 1;
                    right = i + 1;
                }
                else if (i == N - 1)
                {
                    left = i - 1;
                    right = 0;
                }
                else
                {
                    left = i - 1;
                    right = i + 1;
                }

                if ((state[left] == 1 and state[right] == 0) || (state[left] == 0 and state[right] == 1))
                {
                    temp[i] = 1;
                }
                else
                {
                    temp[i] = 0;
                }
            }

            std::copy(temp, temp + N - 1, state);
        }
    }

    for (auto el : state)
    {
        std::cout << el;
    }
    return 0;
}