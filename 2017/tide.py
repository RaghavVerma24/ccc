import math

N = int(input())
arr = [int(x) for x in input().split()]

arr.sort()

mid = math.ceil(len(arr) / 2)

low = arr[:mid][::-1]
high = arr[mid:]


out = ""
for i in range(mid):
    out += str(low[i]) + " "

    if i < len(high):
        out += str(high[i]) + " "

print(out)
