N = int(input())

swifts = input().split()
semaphores = input().split()

k = 0

swifts_sum = 0
semaphores_sum = 0
for i in range(len(swifts)):
    swifts_sum += int(swifts[i])
    semaphores_sum += int(semaphores[i])

    if swifts_sum == semaphores_sum:
        k = i + 1

print(k)
