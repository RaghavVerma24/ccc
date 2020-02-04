import copy

G = int(input())
P = int(input())

planes = [int(input()) for _ in range(P)]

taken = [0 for _ in range(G)]
n_planes = 0

for p in planes:
    done = False
    for i in range(p, 0, -1):
        if taken[i - 1] == 0:
            taken[i - 1] = p
            n_planes += 1
            done = True
            break

    if not done:
        break


print(n_planes)

# 4
# 6
# 2
# 2
# 3
# 3
# 4
# 4
