count = int(input())

numArr = []

for _ in range(count):
    num = int(input())
    if num != 0:
        numArr.append(num)
    else:
        numArr.pop()

sum = 0
for n in numArr:
    sum += n

print(sum)