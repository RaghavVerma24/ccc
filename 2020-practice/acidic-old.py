N = int(input())


freq = {}

freq_inverse = {}

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

    for key in list(freq.keys()):
        val = freq[key]

        if val in freq_inverse:
            freq_inverse[val] += [key]
        else:
            freq_inverse[val] = [key]

    max_freq_readings = freq_inverse[max(freq_inverse.keys())]
    freq_inverse.pop(max(freq_inverse.keys()))
    second_max_freq_readings = freq_inverse[max(freq_inverse.keys())]

    if len(max_freq_readings) == 1 and len(second_max_freq_readings) == 1:
        print(abs(max_freq_readings[0] - second_max_freq_readings[0]))
    if len(max_freq_readings) == 1 and len(second_max_freq_readings) > 1:
        second_max_freq_readings.sort()

        print(max(abs(max_freq_readings[0] - second_max_freq_readings[0]),
                  abs(max_freq_readings[0] - second_max_freq_readings[-1])))
    if len(max_freq_readings) > 1 and len(second_max_freq_readings) == 1:
        max_freq_readings.sort()

        print(max(abs(max_freq_readings[0] - second_max_freq_readings[0]),
                  abs(max_freq_readings[-1] - second_max_freq_readings[0])))

    if len(max_freq_readings) > 1 and len(second_max_freq_readings) > 1:
        max_freq_readings.sort()
        second_max_freq_readings.sort()

        print(max(max(abs(max_freq_readings[0] - second_max_freq_readings[0]),
                      abs(max_freq_readings[0] - second_max_freq_readings[-1])), max(abs(max_freq_readings[-1] - second_max_freq_readings[0]), abs(max_freq_readings[-1] - second_max_freq_readings[-1]))))
