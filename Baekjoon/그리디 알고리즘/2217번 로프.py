n = int(input())

lineList = []
for _ in range(n):
    lineList.append(int(input()))

lineList.sort(reverse=True)

weight = 0
for i, line in enumerate(lineList):
    if weight <= line * (i+1):
        weight = line * (i+1)

print(weight)

# 물건의 중량이 w일 때 k개의 로프에 걸리는 각 중량은 w/k
# 모든 로프를 사용해야 할 필요는 없다.
# 이 때, 최선의 선택이란
# 가장 무거운 중량부터 선택한다.
# 지금 로프까지의 무게