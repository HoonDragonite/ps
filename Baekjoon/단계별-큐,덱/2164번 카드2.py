'''
1 위
N 아래

1을 버리고 2를 제일 밑으로 옮긴다

가장 마짐가의 카드
'''

from collections import deque

count = int(input())
dataDeque = deque(list(range(1, count+1)))

while True:
    if len(dataDeque) == 1:
        print(dataDeque[0])
        break
    dataDeque.popleft()
    dataDeque.append(dataDeque.popleft())
