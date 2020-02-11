N = int(input())

swifts = [int(char) for char in input().split()]
semaphores = [int(char) for char in input().split()]

swifts_sum = 0
semaphores_sum = 0

K = 0

for i in range(N):
    swifts_sum += swifts[i]
    semaphores_sum += semaphores[i]

    if swifts_sum == semaphores_sum:
        K = i + 1


print(K)
