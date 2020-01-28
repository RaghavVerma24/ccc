#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

std::map<std::vector<int>, int> dict;

int recurse(std::vector<int> arr, int n, int k)
{
    std::vector<int> tempvec(arr);
    tempvec.push_back(n);
    tempvec.push_back(k);

    if (dict.find(tempvec) == dict.end())
    {
        if (n <= k)
        {
            int temp = *max_element(arr.begin(), arr.end());
            dict[tempvec] = temp;
            return temp;
        }

        int remainder = n % k;

        if (remainder == 0)
        {
            int scores = 0;

            int i = 0;
            while (i < n)
            {
                int temp = *max_element(arr.begin() + i, arr.begin() + i + k);
                scores += temp;

                i += k;
            }

            dict[tempvec] = scores;
            return scores;
        }
        else
        {
            int possible_max = 0;
            for (int i = remainder; i < k + 1; ++i)
            {
                int today_max = *max_element(arr.begin(), arr.begin() + i);

                std::vector<int> temp_vec = std::vector<int>(arr.begin() + i, arr.end());
                std::vector<int> temp2(temp_vec);
                int future_max = recurse(temp2, n - i, k);

                possible_max = std::max(possible_max, today_max + future_max);
            }

            dict[tempvec] = possible_max;
            return possible_max;
        }
    }
    else
    {
        return dict[tempvec];
    }
}

int main()
{

    int N;
    int K;

    std::vector<int> A;

    cin >> N >> K;

    for (int i = 0; i < N; ++i)
    {
        int temp;
        cin >> temp;
        A.push_back(temp);
    }

    int out = recurse(A, N, K);

    cout << out << endl;

    return 0;
}