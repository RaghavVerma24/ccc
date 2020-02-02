N, M = [int(char) for char in input().split()]

pho = [int(char) for char in input().split()]

tree = {}
edges = 0
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

    edges += 1


def prune_tree(tree, edges):
    tree = tree.copy()
    keys = list(tree.keys())

    for key in keys:
        if key not in pho and len(tree[key]) == 1:
            temp = tree[key][0]

            tree[temp].remove(key)
            tree.pop(key)
            edges -= 1

    return tree, edges


while True:
    new_tree, edges = prune_tree(tree, edges)

    if new_tree == tree:
        tree = new_tree
        break

    tree = new_tree

vertices = []
for x in pho:
    if len(tree[x]) == 1:
        vertices.append(x)


def traverse(start, sofar, prev):
    neighbors = tree[start]

    if prev:
        neighbors.remove(prev)

    if len(neighbors) == 0:
        return 0

    max_len = 0
    for neighbor in neighbors:

        if neighbor in vertices[1:]:
            max_len = max(max_len, sofar + 1)
        else:
            length = traverse(neighbor, sofar + 1, start)
            max_len = max(max_len, length)

    return max_len


out = traverse(vertices[0], 0, None)
print((2 * edges) - out)

# N = 8
# M = 2
# pho = [5, 2]
# tree = {0: [1, 2], 1: [0, 6, 5], 2: [0, 3], 3: [
#     2, 4, 7], 4: [3], 6: [1], 5: [1], 7: [3]}
