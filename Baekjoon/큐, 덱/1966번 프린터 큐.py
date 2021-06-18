from collections import deque

count = int(input())

resultList = []
for _ in range(count):
    n, m = map(int, input().split())
    dataList = list(map(int, input().split())) # n개의 문서
    
    targetData = dataList[m] # m번째 페이지의 중요도

    dataQue = deque(dataList) 
    indexQue = deque(list(range(n)))
    
    count = 0
    result = 0
    while True:
        if dataQue[0] == max(dataQue):
            count += 1
            if indexQue[0] == m:
                result = count
                resultList.append(result)
                break
            dataQue.popleft()
            indexQue.popleft()
        else:
            dataQue.append(dataQue.popleft())
            indexQue.append(indexQue.popleft())

for r in resultList:
    print(r)
