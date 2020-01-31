chars = list(input())

total = 0

Rs = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

i = 0

while i < len(chars):
    A = chars[i]
    R = chars[i + 1]

    if i < len(chars) - 2:
        rnew = chars[i + 3]
    else:
        rnew = "I"

    temp = int(A) * Rs[R]

    if Rs[rnew] > Rs[R]:
        total -= temp
    else:
        total += temp

    i += 2

print(total)
