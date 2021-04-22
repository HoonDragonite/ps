orderCount = int(input())

numArr = []
for _ in range(orderCount):
    numArr.append(int(input()))

stack = []
orderList = []
for num in numArr:
    while True:
        if len(stack) == 0:
            stack.append(1)
            orderList.append("+")
        if len(stack) != 0 and num == stack[-1]:
            stack.pop()
            orderList.append("-")
            break
        if len(stack) != 0 and num > stack[-1]:
            stack.append(stack[-1] + 1)
            orderList.append("+")
        elif len(stack) != 0 and num < stack[-1]:
            stack.pop()
            orderList.append("-")


print(orderList)
print(stack)