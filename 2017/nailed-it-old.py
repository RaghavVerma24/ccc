import copy
import math

N = int(input())
boards = [int(char) for char in input().split()]

# N = 4
# boards = [1, 2, 3, 4]

boards.sort()

possible_heights = [boards[0] + boards[i] for i in range(1, len(boards))]

n_heights = 0
longest_fence = 0
for possible_height in possible_heights:
    fence_length = 0

    temp_boards = copy.deepcopy(boards)

    i = 0
    while i < len(temp_boards):
        board = temp_boards[i]

        comp_board_height = possible_height - board

        if comp_board_height <= 0:
            i += 1
        else:
            temp_boards2 = temp_boards.copy()
            temp_boards2.pop(i)
            if comp_board_height in temp_boards2:
                comp_board = temp_boards2[temp_boards2.index(
                    comp_board_height)]

                temp_boards.pop(i)
                temp_boards.remove(comp_board_height)

                fence_length += 1
            else:
                i += 1  # or 2

    if fence_length > longest_fence:
        longest_fence = fence_length
        n_heights = 1
    elif fence_length == longest_fence:
        n_heights += 1


# if longest_fence == 1:
#     n_heights = int(math.factorial(
#         len(boards)) / (math.factorial(2) * math.factorial(len(boards) - 2)))

print(longest_fence, n_heights)
