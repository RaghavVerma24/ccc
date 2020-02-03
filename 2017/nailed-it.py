N = int(input())
boards = [int(char) for char in input().split()]

board_heights = {}
fence_lengths = {}

for i in range(len(boards)):
    wood1 = boards[i]

    for j in range(i + 1, len(boards)):
        # if i == j:
        #     continue

        wood2 = boards[j]

        board = wood1 + wood2

        if board in board_heights:
            if i not in board_heights[board] and j not in board_heights[board]:
                board_heights[board] += [i, j]
                fence_lengths[board] += 1

        else:
            board_heights[board] = [i, j]
            fence_lengths[board] = 1


temp = sum([1 if val == max(fence_lengths.values())
            else 0 for val in list(fence_lengths.values())])

print(max(fence_lengths.values()), temp)
