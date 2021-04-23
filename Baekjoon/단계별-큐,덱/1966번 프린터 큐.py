from collections import deque

count = int(input())


resultList = []
for _ in range(count):
    n, m = map(int, input().split())
    dataList = list(map(int, input().split())) # n개의 문서
    
    page = dataList[m] # m번째 페이지의 중요도

    dataQue = deque(dataList) 

    print(dataQue)

