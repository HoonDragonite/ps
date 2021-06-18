count = int(input())
dataArr = []

for _ in range(count):
    dataArr.append(list(map(int, input().split())))

result = []
for i, data in enumerate(dataArr):
    count = 0
    for j, otherData in enumerate(dataArr):
        if i == j: continue
        if data[0] < otherData[0] and data[1] < otherData[1]:
            count += 1
    
    result.append(count + 1) # 등수는 나보다 큰 사람 + 1

for r in result:
    print(r, end=" ")