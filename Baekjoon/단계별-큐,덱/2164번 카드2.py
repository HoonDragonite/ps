from collections import deque

count = int(input())
dataDeque = deque(list(range(1, count+1)))

while True:
    if len(dataDeque) == 1:
        print(dataDeque[0])
        break
    dataDeque.popleft()
    dataDeque.append(dataDeque.popleft())
