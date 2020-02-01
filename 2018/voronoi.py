N = int(input())

V = [int(input()) for _ in range(N)]

V.sort()

smallest = 1e10

for i in range(1, N - 1):
    prev = V[i - 1]
    next = V[i + 1]

    current = V[i]

    left = (current - prev) / 2
    right = (next - current) / 2

    neighborhood = left + right

    smallest = min(smallest, neighborhood)

print(smallest)
