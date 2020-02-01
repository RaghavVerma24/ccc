N = int(input())

table = []

for _ in range(N):
    temp = [int(char) for char in input().split()]
    table.append(temp)


def check(arr):
    for c in range(N):
        val = -1
        for r in range(N):
            if arr[r][c] < val:
                return False
            else:
                val = arr[r][c]

    for r in range(N):
        val = -1
        for c in range(N):
            if arr[r][c] < val:
                return False
            else:
                val = arr[r][c]

    return True


def print_table(arr):
    for r in range(N):
        out = ""
        for c in range(N):
            out += str(arr[r][c]) + " "
        print(out)


def rotate(arr):
    new_arr = []

    for c in range(N):
        temp = []
        for r in range(N-1, -1, -1):
            temp.append(arr[r][c])
        new_arr.append(temp)

    return new_arr


while True:
    out = check(table)
    if out:
        print_table(table)
        break
    else:
        table = rotate(table)
