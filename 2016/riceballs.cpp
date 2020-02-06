#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

int N;
std::vector<int> riceballs;

std::map<std::vector<int>, int> memoize;

int combine(std::vector<int> arr)
{
    std::map<std::vector<int>, int>::iterator iter = memoize.find(arr);

    if (iter == memoize.end())
    {
        memoize[arr] = 1;

        int max_val = 0;
        for (int i = 0; i < arr.size() - 1; ++i)
        {
            if (i < arr.size() - 2)
            {
                if (arr[i] == arr[i + 2])
                {
                    std::vector<int> temp(arr);

                    temp[i] += temp[i + 1];
                    temp[i] += temp[i + 2];

                    temp.erase(temp.begin() + i + 1);
                    temp.erase(temp.begin() + i + 1);

                    int temp_max = *std::max_element(temp.begin(), temp.end());
                    max_val = std::max(max_val, temp_max);

                    int temp2 = combine(temp);

                    max_val = std::max(max_val, temp2);
                }
            }

            if (arr[i] == arr[i + 1])
            {
                std::vector<int> temp(arr);
                temp[i] += temp[i + 1];
                temp.erase(temp.begin() + i + 1);

                int temp_max = *std::max_element(temp.begin(), temp.end());
                max_val = std::max(max_val, temp_max);

                int temp2 = combine(temp);

                max_val = std::max(max_val, temp2);
            }
        }

        return max_val;
    }
    else
    {
        return iter->second;
    }
}

int main()
{
    std::cin >> N;

    for (int i = 0; i < N; ++i)
    {
        int temp;
        std::cin >> temp;
        riceballs.push_back(temp);
    }

    int out = combine(riceballs);

    if (out == 0)
    {
        out = *std::max_element(riceballs.begin(), riceballs.end());
    }

    std::cout << out;
}