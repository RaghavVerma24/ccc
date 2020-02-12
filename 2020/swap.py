import copy

chars = input().split()

min_dist = 1e10


def is_c(arr):


def swap(arr, dist=0):
    for i in range(len(chars)):
        for j in range(len(chars)):

            chars2 = copy.deepcopy(chars)
            temp = chars2[i]
            chars2[i] = chars2[j]
            chars2[j] = temp

            if is_c(chars2):
