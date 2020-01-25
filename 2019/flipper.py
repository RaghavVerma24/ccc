flips = list(input())

h = 0
v = 0

for flip in flips:
    if flip == "H":
        h += 1
    elif flip == "V":
        v += 1

if h % 2 == 0 and v % 2 == 0:
    print(1, " ", 2)
    print(3, " ", 4)
elif h % 2 == 0:
    print(2, " ", 1)
    print(4, " ", 3)
elif v % 2 == 0:
    print(3, " ", 4)
    print(1, " ", 2)
else:
    print(4, " ", 3)
    print(2, " ", 1)
