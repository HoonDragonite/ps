from collections import deque

n, m = map(int, input().split()) # 큐의 크기 n, 뽑으려는 수의 개수 m
targetList = list(map(int, input().split())) # 뽑으려는 x번째의 수
dataQue = deque(list(range(1, n+1)))

count = 0
for target in targetList:
    while True:
        # print(dataQue)
        if target == dataQue[0]:
            dataQue.popleft()
            break
        else: 
            if abs(dataQue.index(target) - 0) < abs(dataQue.index(target) - len(dataQue)-1):
                count += 1
                dataQue.append(dataQue.popleft())
            else:
                count += 1
                dataQue.appendleft(dataQue.pop())
print(count)