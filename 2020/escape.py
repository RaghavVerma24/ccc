M = int(input())
N = int(input())

grid = []

facs = {}


for r in range(M):
    row = [int(char) for char in input().split()]

    for c in range(N):
        el = row[c]

        mult = (r + 1) * (c + 1)

        if mult in facs:
            facs[mult] += [[r, c]]
        else:
            facs[mult] = [[r, c]]

    grid.append(row)

# print(facs)

out = "no"

seen = []


def traverse(r, c, grid, prev_r, prev_c):
    global out
    global seen

    if out == "no":
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            out = "yes"
        else:
            val = grid[r][c]
            if val in facs:
                possibles = facs[val]

                seen.append([r, c])

                for x, y in possibles:

                    if [x, y] not in seen:
                        traverse(x, y, grid, r, c)

                    # if x == prev_r and y == prev_c:
                    #     continue
                    # else:
                    #     traverse(x, y, grid, r, c)


traverse(0, 0, grid, -1, -1)

print(out)
