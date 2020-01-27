# part from https://github.com/elibroftw/contest-questions/blob/master/CCC/2019/S4%20Tourism.py

import math

N, K = [int(char) for char in input().split()]
A = [int(char) for char in input().split()]

# N = 5
# K = 3
# A = [2, 5, 7, 1, 4]

# n/k remainder is 0, that means that at each day, move k steps
# else you have leeway of k - remainder

dictionary = {}


def recurse(arr, n, k):

    tuple_arr = tuple(arr)

    if (n, k, tuple_arr) in dictionary:
        return dictionary[(n, k, tuple_arr)]
    else:
        if n <= k:
            temp = max(arr)
            dictionary[(n, k, tuple_arr)] = temp
            return temp

        remainder = n % k

        if remainder == 0:
            scores = 0
            for i in range(0, n, k):
                scores += max(arr[i:i + k])
            dictionary[(n, k, tuple_arr)] = scores
            return scores
        else:
            possible_max = 0
            for i in range(remainder, k + 1):
                today_max = max(arr[:i])

                future_max = recurse(arr[i:], n - i, k)

                possible_max = max(possible_max, today_max + future_max)

            dictionary[(n, k, tuple_arr)] = possible_max
            return possible_max


out = recurse(A, N, K)
print(out)

# def recurse(arr, sofar):

#     if sofar > days:
#         return 0

#     if len(arr) == 0:
#         return 0
#     elif len(arr) == 1:
#         return arr[0]
#     else:
#         possible_futures = []
#         for i in range(1, min(K + 1, len(arr) + 1)):
#             subset = arr[:i]

#             max_today = max(subset)

#             max_future = recurse(arr[i:], sofar + 1)

#             possible_futures.append(max_today + max_future)

#         future = max(possible_futures)
#         return future


# out = recurse(A[:], 1)
# print(out)
