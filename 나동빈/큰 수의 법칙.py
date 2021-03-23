n, m, k = map(int, input().split())
numArr = list(map(int, input().split()))

numArr.sort()

result = 0
first = numArr[-1]
second = numArr[-2]
isMax = k

for _ in range(m):
    if isMax != 0:
        result = result + first
        isMax = isMax - 1
    elif isMax == 0:
        result = result + second
        isMax = k

print(result)