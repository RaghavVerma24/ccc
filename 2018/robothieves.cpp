#include <iostream>
#include <vector>

int N;
int M;

std::string grid[100][100];
int out_grid[100][100];

using namespace std;

int traverse(int x, int y, int sofar)
{

    if (grid[x][y] == "S")
    {
        int ii = 1;
    }
    else if (grid[x][y] != ".")
    {
        return 0;
    }

    if (out_grid[x][y] != -1)
    {
        if (sofar >= out_grid[x][y])
        {
            return 0;
        }
        else
        {
            out_grid[x][y] = sofar;
        }
    }
    else
    {
        out_grid[x][y] = sofar;
    }

    if (grid[x][y - 1] == ".")
    {
        traverse(x, y - 1, sofar + 1);
    }

    if (grid[x][y + 1] == ".")
    {
        traverse(x, y + 1, sofar + 1);
    }

    if (grid[x + 1][y] == ".")
    {
        traverse(x + 1, y, sofar + 1);
    }

    if (grid[x - 1][y] == ".")
    {
        traverse(x - 1, y, sofar + 1);
    }

    return 0;
}

int main()
{
    cin >> N >> M;

    int x;
    int y;

    std::vector<std::vector<int>> cameras;

    for (int i = 0; i < N; ++i)
    {
        string row;
        cin >> row;

        for (int j = 0; j < M; ++j)
        {
            if (row[j] == 'S')
            {
                x = i;
                y = j;
            }

            grid[i][j] = row[j];
            out_grid[i][j] = -1;
        }
    }

    traverse(x, y, 0);

    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            if (grid[i][j] == ".")
            {
                cout << out_grid[i][j] << "\n";
            }
        }
    }

    return 0;
}