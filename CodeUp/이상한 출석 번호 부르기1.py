students = []

for _ in range(23):
    students.append(0)

count = int(input())

say = list(map(int, input().split()))

for i in say:
    students[i-1] = students[i-1] + 1

for i in students:
    print(i, end=" ")