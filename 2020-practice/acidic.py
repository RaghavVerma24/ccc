N = int(input())


freq = {}

for _ in range(N):
    reading = int(input())

    if reading in freq:
        freq[reading] += 1
    else:
        freq[reading] = 1

temp_list = list(freq.values())
if max(temp_list) == 1:
    key_list = list(freq.keys())
    print(abs(max(key_list) - min(key_list)))
else:

    freq_inverse = {}

    for key in list(freq.keys()):
        val = freq[key]

        if val in freq_inverse:
            freq_inverse[val] += [key]
        else:
            freq_inverse[val] = [key]

    freq_inverse_keys = list(freq_inverse.keys())
    freq_inverse_keys.sort()

    most_freq = freq_inverse_keys[-1]
    second_most_freq = freq_inverse_keys[-2]

    if len(freq_inverse[most_freq]) == 1 and len(freq_inverse[second_most_freq]) == 1:
        print(abs(freq_inverse[most_freq][0] -
                  freq_inverse[second_most_freq][0]))

    if len(freq_inverse[most_freq]) == 2:
        print(abs(freq_inverse[most_freq][0] - freq_inverse[most_freq][1]))

    if len(freq_inverse[most_freq]) > 2:
        temp = freq_inverse[most_freq]
        temp.sort()

        print(abs(temp[0] - temp[-1]))

    if len(freq_inverse[most_freq]) == 1 and len(freq_inverse[second_most_freq]) > 1:
        first = freq_inverse[most_freq][0]

        temp = freq_inverse[second_most_freq]
        temp.sort()

        out = max(abs(first - temp[0]), abs(first - temp[-1]))
        print(out)


# 6
# 5
# 5
# 5
# 4
# 4
# 1

# 7
# 5
# 5
# 5
# 4
# 4
# 4
# 1

# 10
# 1
# 1
# 2
# 2
# 3
# 3
# 4
# 4
# 5
# 6

# 10
# 1
# 1
# 1
# 1
# 2
# 2
# 3
# 3
# 4
# 4
