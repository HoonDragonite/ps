from collections import deque

n, k = map(int, input().split())

dataDeque = deque(list(range(1, n+1)))

result = []

k = (k - 1) * -1

while True:
    if len(dataDeque) == 0:
        break
    dataDeque.rotate(k)
    result.append(dataDeque.popleft())

print("<",end='')
for i, r in enumerate(result):
    if i != len(result) - 1:
        print(r, end=', ')
    else:
        print(r, end='>')