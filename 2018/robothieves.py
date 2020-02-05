import sys
import time
sys.setrecursionlimit(10000000)
N, M = [int(char) for char in input().split()]

robot = []

grid = []
for r in range(N):
    row = list(input())
    for c in range(M):
        if row[c] == 'S':
            robot = [r, c]
    grid.append(row)

# N = 4
# M = 5
# grid = [['W', 'W', 'W', 'W', 'W'], ['W', '.', 'W', '.', 'W'],
#         ['W', 'W', 'S', '.', 'W'], ['W', 'W', 'W', 'W', 'W']]
# walls = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 2], [
#     1, 4], [2, 0], [2, 1], [2, 4], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4]]
# empty = [[1, 1], [1, 3], [2, 3]]
# robot = [2, 2]

out_grid = [[-1 for _ in range(M)] for _ in range(N)]


def find_neighbors(x, y):
    avail_neighbors = []

    if grid[x][y - 1] == '.':
        avail_neighbors.append([x, y - 1])
    if grid[x][y + 1] == '.':
        avail_neighbors.append([x, y + 1])
    if grid[x - 1][y] == '.':
        avail_neighbors.append([x - 1, y])
    if grid[x + 1][y] == '.':
        avail_neighbors.append([x + 1, y])

    return avail_neighbors


def traverse(x, y, sofar):

    if grid[x][y] == 'S':
        i = 1
    elif grid[x][y] != '.':
        return

    # if seen, check if shortest
    if out_grid[x][y] != -1:
        if sofar >= out_grid[x][y]:
            return
        else:
            out_grid[x][y] = sofar
    else:
        out_grid[x][y] = sofar

    neighbors = find_neighbors(x, y)

    for neighbor in neighbors:
        traverse(neighbor[0], neighbor[1], sofar + 1)


traverse(robot[0], robot[1], 0)

# for c in range(M):
#     for r in range(N):
#         if [r, c] in empty:
#             if out_grid[r][c] != 0:
#                 print(out_grid[r][c])
for r in range(N):
    for c in range(M):
        if grid[r][c] == '.':
            # if [r, c] in empty:
            if out_grid[r][c] != 0:
                print(out_grid[r][c])

# 5 7
# WWWWWWW
# W.....W
# W.W...W
# WWW.S.W
# WWWWWWW

# 5 7
# WWWWWWW
# W.....W
# W.WC..W
# WWW.S.W
# WWWWWWW
