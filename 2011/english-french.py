N = int(input())

chars = list(''.join([input() for _ in range(N)]))

s = 0
t = 0

for char in chars:
    if char == "s" or char == "S":
        s += 1
    elif char == "t" or char == "T":
        t += 1

if t > s:
    print("English")
elif s > t:
    print("French")
elif t == s:
    print("French")
