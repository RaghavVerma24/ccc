k = int(input())

chars = {}

for _ in range(k):
    char, code = input().split()
    chars[code] = char

seq = list(input())

# k = 5
# chars = {'00': 'A', '01': 'B', '10': 'C', '110': 'D', '111': 'E'}
# seq = ['0', '0', '0', '0', '0', '1', '0', '1', '1', '1', '1']

out = ""

sofar = ""
for char in seq:
    sofar += char

    if sofar in chars:
        out += chars[sofar]
        sofar = ""

print(out)
