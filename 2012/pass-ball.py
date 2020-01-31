import math

J = int(input())


def comb(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


if J >= 4:
    print(int(comb(J - 1, 3)))
else:
    print(0)
