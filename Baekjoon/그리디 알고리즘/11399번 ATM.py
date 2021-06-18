num = int(input())
numArr = list(map(int, input().split()))

numArr.sort()

sum = 0
result = 0
for n in numArr:
    sum = sum + n
    result = sum + result

print(result)