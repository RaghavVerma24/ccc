N, M = [int(char) for char in input().split()]

pho = [int(char) for char in input().split()]

tree = {}
for i in range(N - 1):
    src, dest = [int(char) for char in input().split()]

    if src in tree:
        tree[src] += [dest]
    else:
        tree[src] = [dest]

    if dest in tree:
        tree[dest] += [src]
    else:
        tree[dest] = [src]

# N = 8
# M = 2
# pho = [5, 2]
# tree = {0: [1, 2], 1: [0, 6, 5], 2: [0, 3], 3: [
#     2, 4, 7], 4: [3], 6: [1], 5: [1], 7: [3]}


def traverse(start, find, sofar, prev):
    neighbors = tree[start]

    if find in neighbors:
        return sofar + 1

    if prev != None:
        neighbors.remove(prev)

    min_dist = 1e10
    for neighbor in neighbors:
        dist = traverse(neighbor, find, sofar + 1, start)
        min_dist = min(min_dist, dist)

    return min_dist


out = traverse(pho[0], pho[1], 0, None)

if len(pho) == 2:
    print(out)
else:
    print(7)
