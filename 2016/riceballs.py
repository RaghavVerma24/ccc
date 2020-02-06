import copy

N = int(input())

rice_balls = [int(char) for char in list(input().split())]


memoize = {}


def combine(arr):
    if tuple(arr) in memoize:
        return memoize[tuple(arr)]
    else:
        memoize[tuple(arr)] = 1

        max_val = 0
        for i in range(0, len(arr) - 1):
            if i < len(arr) - 2:
                if arr[i] == arr[i + 2]:
                    temp = copy.deepcopy(arr)
                    temp[i] += temp[i + 1]
                    temp[i] += temp[i + 2]

                    temp.pop(i + 1)
                    temp.pop(i + 1)

                    max_val = max(max_val, max(temp))

                    temp = combine(temp)

                    max_val = max(max_val, temp)

            if arr[i] == arr[i + 1]:
                temp = copy.deepcopy(arr)
                temp[i] += temp[i + 1]
                temp.pop(i + 1)

                max_val = max(max_val, max(temp))

                temp = combine(temp)

                max_val = max(max_val, temp)

        return max_val


out = combine(rice_balls)

if out == 0:
    out = max(rice_balls)

print(out)
