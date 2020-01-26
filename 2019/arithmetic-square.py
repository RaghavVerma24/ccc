import copy

# square = [[char for char in input().split()] for _ in range(3)]
square = [['8', 'X', 'X'], ['16', 'X', '20'], ['24', 'X', '30']]


def print_square(square):
    for row in square:
        print(' '.join([str(char) for char in row]))


def check_and_fill_row(square, r, c):

    zero = square[r][0]
    one = square[r][1]
    two = square[r][2]

    if c == 0:
        if square[r][1] != "X" and square[r][2] != "X":
            return int(int(one) - (int(two) - int(one)))
    elif c == 1:
        if square[r][0] != "X" and square[r][2] != "X":
            return int(int(zero) + ((int(two) - int(zero)) / 2))
    else:
        if square[r][0] != "X" and square[r][1] != "X":
            return int(int(one) + (int(one) - int(zero)))

    return False


def check_and_fill_col(square, r, c):

    zero = square[0][c]
    one = square[1][c]
    two = square[2][c]

    if r == 0 and square[1][c] != "X" and square[2][c] != "X":
        return int(int(one) - (int(two) - int(one)))
    elif r == 1 and square[0][c] != "X" and square[2][c] != "X":
        return int(int(zero) + ((int(two) - int(zero)) / 2))
    elif square[0][c] != "X" and square[1][c] != "X":
        return int(int(one) + (int(one) - int(zero)))

    return False


def fill_in(square):
    for r in range(3):
        for c in range(3):
            if square[r][c] != "X":
                continue

            possible_row = check_and_fill_row(square, r, c)
            possible_col = check_and_fill_col(square, r, c)

            if possible_row:
                square[r][c] = possible_row
            elif possible_col:
                square[r][c] = possible_col
    return square


while True:

    temp = copy.deepcopy(square)

    square2 = fill_in(temp)

    if square == square2:
        square = square2
        break
    else:
        square = square2

num_numbers = 0
numbers = []
for r in range(3):
    for c in range(3):
        if square[r][c] != "X":
            num_numbers += 1
            numbers.append(square[r][c])


def fill_values(square, value):
    for r in range(3):
        for c in range(3):
            if square[r][c] == "X":
                square[r][c] = value

    return square


if num_numbers == 0:
    square = fill_values(square, 0)
elif num_numbers == 1:
    square = fill_values(square, numbers[0])


print_square(square)

# work on when more than 1 x in row or col
