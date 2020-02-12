import copy

N = int(input())

B = [int(char) for char in input().split()]

prob = 0

pos = 0
total = 0

burgers = max(B)


def traverse(arr, taken=[]):
    global pos
    global total

    if len(arr) == 1:
        total += 1
        if arr[0] not in taken:
            pos += 1
    else:
        fav = arr[0]

        if fav in taken:
            for el in arr:
                arr2 = copy.deepcopy(arr)

                arr2.remove(el)
                taken2 = copy.deepcopy(taken)
                taken2 += [el]

                traverse(arr2, taken2)

        else:
            traverse(arr[1:], taken + [arr[0]])


for i in range(len(B)):
    b = B[i]

    arr = copy.deepcopy(B)

    traverse(arr[1:], [b])

print(pos, total, pos/total)

# coach = B.pop(0)

# temp = list(set(B))

# prob += 1 / (len(temp) + 1)

# print(prob)
