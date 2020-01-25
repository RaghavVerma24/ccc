import math

t = int(input())

N = [int(input()) for _ in range(t)]

memoize = {}


def is_prime(x):
    if x in memoize:
        return memoize[x]
    else:
        if x < 2:
            memoize[x] = False
            return False

        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                memoize[x] = False
                return False

        memoize[x] = True
        return True


for n in N:
    for i in range(0, n + 1):
        comp = (2 * n) - i

        if is_prime(i) and is_prime(comp):
            print(i, comp)
            break
