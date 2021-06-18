def switchBW(c):
    result = ""
    if c == "W":
        result = "B"
    else:
        result = "W"
    return result

y, x = map(int, input().split())

dataArr = []
for _ in range(y):
    str = input()
    data = []
    for s in str:
        data.append(s)
    dataArr.append(data)

count = 0
base = dataArr[0][0]
for i, data in enumerate(dataArr):
    now = base
    for j, d in enumerate(data):
        if d != now:
            count += 1
            # data[i][j] = now
        now = switchBW(now)
    base = switchBW(base)

print(count)
print(dataArr)
