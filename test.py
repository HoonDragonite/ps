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


for i, data in enumerate(dataArr):
    print(i)
    for j, d in enumerate(data):
        print(j, end = ' ')
    print("")