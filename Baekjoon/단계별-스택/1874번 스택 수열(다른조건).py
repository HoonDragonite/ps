'''
문제에 오름차순으로만 Push 임
그거 없이 짠거 일단 보류용
'''

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
