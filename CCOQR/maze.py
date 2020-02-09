import copy

# N = int(input())

# rooms = {}
# for i in range(N):
#     corridors = [int(char) for char in input().split()]
#     corridors.pop(0)

#     rooms[i + 1] = corridors

# Q = int(input())

# queries = []
# for _ in range(Q):
#     queries.append(int(input()))


N = 6
rooms = {1: [3], 2: [5, 4], 3: [1], 4: [2, 5, 6], 5: [4, 2], 6: [4]}
Q = 6
# queries = [1, 2, 3, 4, 5, 6]
queries = [2, 3, 4, 5, 6]


def traverse(start, end, sofar, prev=None):
    root = rooms[start]

    root = copy.deepcopy(root)

    if len(root) == 1:
        return sofar + 1

    if prev in root:
        root.remove(prev)

    root.reverse()

    print(start, root)

    for neighbor in root:
        print(neighbor)
        # sofar += traverse(neighbor, start, sofar + 1)

    return sofar


for query in queries:
    root = rooms[query]
    print(query, root)

    max_len = 0

    for neighbor in root:
        path_len = traverse(neighbor, query, 1, query)

        max_len = max(path_len, max_len)
        print('maxlen', max_len)

    break
