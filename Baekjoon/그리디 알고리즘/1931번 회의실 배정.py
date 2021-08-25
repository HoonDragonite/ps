count = int(input())
arr = []
lastTime = 0
results = []
for _ in range(count):
    numArr = list(map(int, input().split()))
    arr.append(numArr)

arr.sort(key = lambda x: (x[1], x[0]))

for data in arr:
    if lastTime <= data[0]:
        results.append(data)
        lastTime = data[1]

print(len(results))