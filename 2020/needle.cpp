#include <iostream>
#include <vector>
#include <string>
#include "stdio.h"
#include <map>

std::vector<std::string> N;

std::map<std::string, int> permutations;

std::vector<std::string> H;

int permute(std::map<std::string, int> str_dict, std::string sofar)
{
    for (std::map<std::string, int>::iterator it = str_dict.begin(); it != str_dict.end(); ++it)
    {
        std::string key = it->first;

        if (str_dict[key] > 0)
        {
            std::string sofar2 = sofar;

            sofar2 += key;

            if (sofar2.size() == N.size())
            {
                if (permutations.find(sofar2) == permutations.end())
                {
                    permutations[sofar2] = 1;
                }
            }
            else
            {
                std::map<std::string, int> str_dict2 = str_dict;

                str_dict2[key] -= 1;

                permute(str_dict2, sofar2);
            }
        }
    }

    return 1;
}

int main()
{

    std::string Nt;
    std::string Ht;

    std::getline(std::cin, Nt);
    std::getline(std::cin, Ht);

    std::map<std::string, int> N_dict;

    for (int i = 0; i < Nt.size(); ++i)
    {
        std::string temp = Nt.substr(i, 1);

        if (N_dict.find(temp) == N_dict.end())
        {
            N_dict[temp] = 1;
        }
        else
        {
            N_dict[temp] += 1;
        }

        N.push_back(temp);
    }

    for (int i = 0; i < Ht.size(); ++i)
    {
        std::string temp = Ht.substr(i, 1);
        H.push_back(temp);
    }

    std::map<std::string, int> new_h;

    for (int i = 0; i < Ht.size() - Nt.size() + 1; ++i)
    {
        std::string temp = Ht.substr(i, Nt.size());
        new_h[temp] = 1;
    }

    int n_permutations = 0;

    // std::vector<std::string> N2;
    // std::vector<std::string> H2;

    // for (int i = 0; i < N.size(); ++i)
    // {
    //     std::string temp = N[i];
    //     N2.push_back(temp);
    // }

    // for (int i = 0; i < H.size(); ++i)
    // {
    //     H2.push_back(H[i]);
    // }

    permute(N_dict, "");

    for (std::map<std::string, int>::iterator it = permutations.begin(); it != permutations.end(); ++it)
    {
        if (new_h.find(it->first) != new_h.end())
        {
            n_permutations += 1;
        }
    }

    std::cout << n_permutations;

    return 0;
}