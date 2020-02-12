N = int(input())

obs = []

for _ in range(N):
    obs.append([int(char) for char in input().split()])

obs.sort()

max_speed = 0

for i in range(N - 1):
    t1, x1 = obs[i]
    t2, x2 = obs[i + 1]

    avg_speed = abs(x2 - x1) / abs(t2 - t1)

    max_speed = max(max_speed, avg_speed)


print(max_speed)
