import sys

stack = []

def push(element):
    stack.append(element)

def pop():
    if len(stack) == 0 : return -1
    else: return stack.pop()

def size():
    return len(stack)

def empty():
    if len(stack) == 0 : return 1
    else : return 0

def top():
    if len(stack) == 0 : return -1
    else : return stack[-1]

orderCount = int(input())

orderArr = []

# input order
for _ in range(orderCount):
    orderArr.append(list(sys.stdin.readline().split()))

for order in orderArr:
    if order[0] == "push":
        push(int(order[1]))
    if order[0] == "pop":
        print(pop())
    if order[0] == "size":
        print(size())
    if order[0] == "empty":
        print(empty())
    if order[0] == "top":
        print(top())
