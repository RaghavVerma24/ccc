#include <iostream>
#include <vector>
#include <map>

#include <string>

std::vector<std::vector<int>> grid;

std::string out = "no";

std::map<int, std::vector<std::vector<int>>> facs;

// std::vector<std::vector<int>> seen;
std::map<std::vector<int>, int> seen;

void traverse(int r, int c)
{
    if (out == "no")
    {
        if (r == grid.size() - 1 && c == grid[0].size() - 1)
        {
            out = "yes";
        }
        else
        {
            int val = grid[r][c];

            if (facs.find(val) != facs.end())
            {
                std::vector<std::vector<int>> possibles = facs[val];

                seen[{r, c}] = 1;

                for (int i = 0; i < possibles.size(); ++i)
                {
                    std::vector<int> possible = possibles[i];

                    if (seen.find(possible) == seen.end())
                    {
                        traverse(possible[0], possible[1]);
                    }
                }
            }
        }
    }
}

int main()
{

    int M;
    int N;

    std::cin >> M;
    std::cin >> N;

    for (int i = 0; i < M; ++i)
    {
        std::vector<int> row;
        for (int j = 0; j < N; ++j)
        {
            int temp;
            std::cin >> temp;

            int mult = (i + 1) * (j + 1);

            if (facs.find(mult) != facs.end())
            {
                facs[mult].push_back({i, j});
            }
            else
            {
                facs[mult] = {{i, j}};
            }

            row.push_back(temp);
        }

        grid.push_back(row);
    }

    traverse(0, 0);

    std::cout << out;

    return 0;
}