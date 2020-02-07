import copy

N, T = [int(char) for char in input().split()]

state = list(input())

memoize = {}

first_gen = []
cycles_to_go = 0

generation = 0
while generation < T:

    if generation > 1 and state == first_gen:
        len_cycle = generation - 1
        cycles_to_go = (T - 1) % len_cycle
        break
    else:
        temp = copy.deepcopy(state)

        for i in range(N):
            if i == 0:
                left = N - 1
                right = i + 1
            elif i == N - 1:
                left = i - 1
                right = 0
            else:
                left = i - 1
                right = i + 1

            if (state[left] == "1" and state[right] == "0") or (state[left] == "0" and state[right] == "1"):
                temp[i] = "1"
            else:
                temp[i] = "0"

        generation += 1
        state = temp

        if generation == 1:
            first_gen = state

    # print(''.join(state))

if cycles_to_go > 0:
    for cycle in range(cycles_to_go):
        temp = copy.deepcopy(state)

        for i in range(N):
            if i == 0:
                left = N - 1
                right = i + 1
            elif i == N - 1:
                left = i - 1
                right = 0
            else:
                left = i - 1
                right = i + 1

            if (state[left] == "1" and state[right] == "0") or (state[left] == "0" and state[right] == "1"):
                temp[i] = "1"
            else:
                temp[i] = "0"

        state = temp

print(''.join(state))

# 5 10
# 01011

# out
# 5 10
# 01011
# 00011
# 10111
# 10100
# 00011
# 10111
# 10100
# 00011
# 10111
# 10100
# 00011
# 00011

# 5 9
# 01011
# 00011
# 10111
# 10100
# 00011
# 10111
# 10100
# 00011
# 10111
# 10100
# 10100
