N = int(input())

students = []
for _ in range(N):
    students.append(input())

correct = []
for _ in range(N):
    correct.append(input())

n_correct = 0
for i in range(N):
    if students[i] == correct[i]:
        n_correct += 1

print(n_correct)
