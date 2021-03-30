num = int(input())

result = 0
addNum = 0

while True:
    addNum = addNum + 1
    result = result + addNum
    if result >= num:
        print(addNum)
        break

