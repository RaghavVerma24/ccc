import copy

N, M, D = [int(char) for char in input().split()]

pipes = [[int(char) for char in input().split()] for _ in range(M)]

# N = 4
# M = 4
# D = 0

# pipes = [[1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 1, 1]]


def valid_and_cost(arr):
    unconnected_nodes = []
    cost = 0
    for (a, b, c) in arr:

        cost += c

        if a in unconnected_nodes:
            unconnected_nodes.remove(a)
        else:
            unconnected_nodes.append(a)

        if b in unconnected_nodes:
            unconnected_nodes.remove(b)
        else:
            unconnected_nodes.append(b)

    if len(unconnected_nodes) == 2:
        return cost
    else:
        return -1


start_valid_pipes = pipes[:N - 1]
possible_replacements = pipes[N - 1:]

min_cost = 1e6

min_days = 1e6
for possible_replacement in possible_replacements:
    days = 1
    for i in range(len(start_valid_pipes)):
        pipes2 = copy.deepcopy(start_valid_pipes)
        pipes2[i] = possible_replacement

        out = valid_and_cost(pipes2)

        if out <= min_cost:
            min_cost = out

            min_days = min(min_days, days)
        else:
            days += 1

print(min_days)
