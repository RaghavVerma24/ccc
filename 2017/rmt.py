import copy

N, M, Q = [int(char) for char in input().split()]

line_numbers = [int(char) for char in input().split()]

passengers = [int(char) for char in input().split()]

lines = [[] for _ in range(M)]

for i in range(len(line_numbers)):
    station = line_numbers[i]

    lines[station - 1].append(i)

out = []

for _ in range(Q):
    action = [int(char) for char in input().split()]

    if action[0] == 1:
        _, l, r = action

        out.append(sum(passengers[l - 1:r]))

    else:
        _, x = action

        line_to_operate = lines[x - 1]

        temp = 0
        for i, line in enumerate(line_to_operate):
            if i == 0:

                temp = passengers[line]
                passengers[line] = passengers[line_to_operate[-1]]

            else:
                temp2 = passengers[line]
                passengers[line] = temp
                temp = temp2

for x in out:
    print(x)
