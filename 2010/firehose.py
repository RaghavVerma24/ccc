import math
H = int(input())

houses = []

for _ in range(H):
    houses.append(int(input()))

k = int(input())


# H = 4
# houses = [0, 67000, 68000, 77000]
# k = 2

houses.sort()

hydrants = houses

hydrants_dist = {}

while len(hydrants) > k:
    min_dist = 1e10
    min_hydrant = None
    for i in range(0, len(hydrants)):
        if i == 0:
            dist = 1e6 + (hydrants[i] - hydrants[-1])
            print(dist)
        else:
            dist = hydrants[i] - hydrants[i - 1]

        if dist < min_dist:
            min_dist = dist
            min_hydrant = i

    hydrant_to_be_removed = hydrants[min_hydrant]
    hydrant_before_hydrant_to_be_removed = hydrants[min_hydrant -
                                                    1] if min_hydrant is not 0 else hydrants[-1]

    homes_attached_to_hydrant_to_be_removed = hydrants_dist[
        hydrant_to_be_removed] if hydrant_to_be_removed in hydrants_dist else []
    homes_attached_to_hydrant_before_hydrant_to_be_removed = hydrants_dist[
        hydrant_before_hydrant_to_be_removed] if hydrant_before_hydrant_to_be_removed in hydrants_dist else []

    temp = homes_attached_to_hydrant_before_hydrant_to_be_removed + \
        homes_attached_to_hydrant_to_be_removed

    temp += [hydrant_before_hydrant_to_be_removed] if hydrant_before_hydrant_to_be_removed not in temp else []

    hydrants_dist[hydrant_before_hydrant_to_be_removed] = temp + \
        [hydrant_to_be_removed]

    hydrants.pop(min_hydrant)

max_hose = 0

for hydrant in hydrants_dist:
    hydrants = hydrants_dist[hydrant]
    mid = (max(hydrants) - min(hydrants)) / 2

    max_hose = max(max_hose, mid)

print(int(math.ceil(max_hose)))
