N, K = [int(char) for char in input().split()]

triangle = [[int(char) for char in input().split()] for _ in range(N)]

# N = 4
# K = 2
# triangle = [[3], [1, 2], [4, 2, 1], [6, 1, 4, 2]]

ans = 0


def get_triangle(r, c, size):
    max_val = 0
    for i in range(0, size):
        for j in range(0, i + 1):

            max_val = max(max_val, triangle[i + r][j + c])

    return max_val


for i in range(0, N - K + 1):
    for j in range(0, i + 1):
        ans += get_triangle(i, j, K)

print(ans)
