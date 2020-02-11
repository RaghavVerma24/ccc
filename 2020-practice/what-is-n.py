import math

N = int(input())

if N == 1:
    print(1)
else:
    if N <= 5:
        print(int(N / 2) + 1)
    else:
        possible = 0
        for i in range(1, int(N / 2) + 1):
            left = N - i
            right = i

            if left <= 5 and right <= 5:
                possible += 1

        print(possible)


# 10
# 9 1
# 8 2
# 7 3
# 6 4
# 5 5

# 2
# 1 1

# 3
# 2 1

# 5
# 4 1
# 3 2

# 6
# 5 1
# 4 2
# 3 2

# 7
# 6 1
# 5 2
# 4 3
