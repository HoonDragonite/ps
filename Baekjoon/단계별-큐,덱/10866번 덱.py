from collections import deque
import sys

myDeque = deque()

orderCount = int(input())

orderArr = []

# input order
for _ in range(orderCount):
    order = list(sys.stdin.readline().split())
    if order[0] == "push_front":
        myDeque.appendleft(int(order[1]))
    if order[0] == "push_back":
        myDeque.append(int(order[1]))
    if order[0] == "pop_front":
        if len(myDeque) != 0: print(myDeque.popleft())
        else : print(-1)
    if order[0] == "pop_back":
        if len(myDeque) != 0: print(myDeque.pop())
        else : print(-1)
    if order[0] == "size":
        print(len(myDeque))
    if order[0] == "empty":
        if len(myDeque) == 0:
            print(1)
        else: print(0)
    if order[0] == "front":
        if len(myDeque) == 0:
            print(-1)
        else: print(myDeque[0])
    if order[0] == "back":
        if len(myDeque) == 0:
            print(-1)
        else: print(myDeque[-1])