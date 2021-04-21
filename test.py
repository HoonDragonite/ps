import sys
# sys.stdin.readline()

dataArr = []
while True:
    data = sys.stdin.readline()
    if data == ".":
        break
    dataArr.append(data)
    data = ""
print(dataArr)