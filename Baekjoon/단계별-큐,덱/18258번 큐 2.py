from collections import deque
import sys

que = deque()

orderCount = int(input())

orderArr = []

# input order
for _ in range(orderCount):
    order = list(sys.stdin.readline().split())
    if order[0] == "push":
        que.append(int(order[1]))
    if order[0] == "pop":
        if len(que) != 0: print(que.popleft())
        else : print(-1)
    if order[0] == "size":
        print(len(que))
    if order[0] == "empty":
        if len(que) == 0:
            print(1)
        else: print(0)
    if order[0] == "front":
        if len(que) == 0:
            print(-1)
        else: print(que[0])
    if order[0] == "back":
        if len(que) == 0:
            print(-1)
        else: print(que[-1])

'''
시간 초과
import sys

queue = []

def push(x):
    queue.append(x)

def pop():
    if len(queue) != 0:
        return queue.pop(0)
    else:
        return -1

def size():
    return len(queue)

def empty():
    if len(queue) == 0:
        return 1
    else:
        return 0

def front():
    if len(queue) != 0:
        return queue[0]
    else:
        return -1

def back():
    if len(queue) != 0:
        return queue[-1]
    else:
        return -1

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
    if order[0] == "front":
        print(front())
    if order[0] == "back":
        print(back())
'''