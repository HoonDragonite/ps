orderCount = int(input())

numArr = []
for _ in range(orderCount):
    numArr.append(int(input()))

stack = []
orderList = []
ascNum = 1
isImpossible = False
for num in numArr:
    while isImpossible == False:
        if len(stack) == 0:
            if num >= ascNum:
                stack.append(ascNum)
                orderList.append("+")
                ascNum += 1
            else:
                isImpossible = True
                break
        else:
            if num == stack[-1]:
                stack.pop()
                orderList.append("-")
                break
            if num >= ascNum:
                stack.append(ascNum)
                orderList.append("+")
                ascNum += 1
            elif num < ascNum:
                stack.pop()
                orderList.append("-")

if isImpossible == True:
    print("NO")
else:
    for order in orderList:
        print(order)
