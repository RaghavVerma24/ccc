N, M = [int(char) for char in input().split()]

blocks = []
for _ in range(M):
    r, c = [int(char) for char in input().split()]
    blocks.append([r, c])

pyramid = []
for i in range(1, N + 1):
    row = []
    for j in range(0, i):
        row.append(0)
    pyramid.append(row)

blocks.reverse()


def fill(r, c, pyramid):
    pyramid[r][c] = 1
    if r != len(pyramid) - 1:
        if pyramid[r + 1][c] == 0:
            pyramid[r + 1][c] = 1
            pyramid = fill(r + 1, c, pyramid)
        if pyramid[r + 1][c + 1] == 0:
            pyramid[r + 1][c + 1] = 1
            pyramid = fill(r + 1, c + 1, pyramid)

    return pyramid


for r, c in blocks:
    pyramid = fill(r - 1, c - 1, pyramid)

print(sum([sum(r) for r in pyramid]))
