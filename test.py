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
        maxData = max(dataQue)
        if (maxData == targetData): # 최대중요도와 목표중요도가 같을 때
            if dataQue[0] == targetData:
                count += 1
                if indexQue[0] == m:
                    result = count
                    resultList.append(result)
            else: 
                dataQue.append(dataQue.popleft())
                indexQue.append(indexQue.popleft())
        else:
            if dataQue[0] == maxData:
                count += 1
                dataQue.popleft()
                indexQue.popleft()
            else:
                dataQue.append(dataQue.popleft())
                indexQue.append(indexQue.popleft())
        print(dataQue)
        print(indexQue)
for r in resultList:
    print(r)

'''
a b c d
2 1 4 3

C D A B

'''