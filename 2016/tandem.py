q_type = int(input())

N = int(input())

dmoj = [int(x) for x in input().split()]
peg = [int(x) for x in input().split()]

dmoj.sort()
peg.sort()

val = -1 if q_type == 1 else 0

total = 0
for _ in range(N):
    total += max(dmoj.pop(-1), peg.pop(val))

print(total)
