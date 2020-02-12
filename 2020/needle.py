import copy

N = input()
H = input()

new_h = []
len_needle = len(N)
for i in range(len(H) - len_needle + 1):
    new_h.append(H[i:i + len_needle])

N_list = list(N)

permutations = []

n_permutations = 0

N_dict = {}

for char in N_list:
    if char in N_dict:
        N_dict[char] += 1
    else:
        N_dict[char] = 1


def permute(str_dict, sofar=""):

    global N_list

    keys = list(str_dict.keys())

    for key in keys:
        if str_dict[key] > 0:
            sofar2 = copy.deepcopy(sofar)

            sofar2 += key

            if len(sofar2) == len(N_list):
                if sofar2 not in permutations:
                    permutations.append(sofar2)

            else:
                str_dict_2 = copy.deepcopy(str_dict)
                str_dict_2[key] -= 1

                permute(str_dict_2, sofar2)


permute(N_dict)

for permutation in permutations:

    if permutation in new_h:
        n_permutations += 1
    # if H.find(permutation) != -1:
    #     n_permutations += 1

print(n_permutations)


# def permute(string, sofar=""):

#     global N_list

#     for i in range(len(string)):
#         string2 = copy.deepcopy(string)
#         sofar2 = copy.deepcopy(sofar)

#         char = string2[i]
#         # print(char)

#         sofar2 += char

#         if len(sofar2) == len(N_list):
#             if sofar2 not in permutations:
#                 permutations.append(sofar2)
#             # fix
#             # print(sofar2)
#         else:
#             string2.pop(i)

#             permute(string2, sofar2)


# permute(N_list)

# # permutations = set(permutations)
# # permutations = list(permutations)

# # print(permutations)

# for permutation in permutations:

#     if H.find(permutation) != -1:
#         n_permutations += 1

# print(n_permutations)
