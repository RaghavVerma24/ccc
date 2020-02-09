N = int(input())

xs = {}
ys = {}

points = []
for i in range(N):
    x, y = [int(char) for char in input().split()]

    if x in xs:
        xs[x] += [y]
    else:
        xs[x] = [y]

    if y in ys:
        ys[y] += [x]
    else:
        ys[y] = [x]

    points.append([x, y])

# N = 12
# xs = {-3: [6, 2, -3, -6], 1: [6, 2, -3, -4], -1: [4, -4], 4: [2], -4: [-3]}
# ys = {6: [-3, 1], 4: [-1], 2: [-3, 1, 4], -
#       3: [-4, -3, 1], -4: [-1, 1], -6: [-3]}
# points = [[-3, 6], [1, 6], [-1, 4], [-3, 2], [1, 2], [4, 2],
#           [-4, -3], [-3, -3], [1, -3], [-1, -4], [1, -4], [-3, -6]]

num_bow_ties = 0

for x, y in points:
    x_neighbors = ys[y]
    y_neighbors = xs[x]

    if len(x_neighbors) >= 3 and len(y_neighbors) >= 3:
        x_neighbors_pos = x_neighbors.index(x)
        y_neighbors_pos = y_neighbors.index(y)

        if (x_neighbors_pos == 0 or x_neighbors_pos == len(x_neighbors) - 1) or (y_neighbors_pos == 0 or y_neighbors_pos == len(y_neighbors) - 1):
            continue
        else:
            num_above = len(y_neighbors[:y_neighbors.index(y)])
            num_below = len(y_neighbors[y_neighbors.index(y) + 1:])
            num_left = len(x_neighbors[:x_neighbors.index(x)])
            num_right = len(x_neighbors[x_neighbors.index(x) + 1:])

            num_bow_ties += 2 * num_above * num_below * num_left * num_right

print(num_bow_ties)

# possible_x_values = []
# possible_y_values = []

# y_keys = list(ys.keys())

# for x_key in xs:
#     if len(xs[x_key]) >= 3:
#         possible_x_values.append(x_key)

# for y_key in ys:
#     if len(ys[y_key]) >= 3:
#         possible_y_values.append(y_key)

# possible_vertices = []

# for possible_x_value in possible_x_values:
#     for possible_y_value in possible_y_values:
#         pair = [possible_x_value, possible_y_value]
#         if pair in points:
#             possible_vertices.append(pair)

# possible = 0
# for possible_vertex in possible_vertices:
#     x, y = possible_vertex

#     x_index = ys[y].index(x)
#     y_index = xs[x].index(y)

#     if (0 < x_index and x_index < len(ys[y]) - 1) and (0 < y_index and y_index < len(xs[x]) - 1):
#         possible += (len(xs[x][y_index + 1:]) * len(xs[x][:y_index])) * \
#             (len(ys[y][x_index + 1:]) * len(ys[y][:x_index]))

# print(possible * 2)


# 12
# -3 6
# 1 6
# -1 4
# -3 2
# 1 2
# 4 2
# -4 -3
# -3 -3
# 1 -3
# -1 -4
# 1 -4
# -3 -6
