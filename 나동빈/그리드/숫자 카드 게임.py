def solution():
    n, m = map(int, input().split())

    dataArr = []
    for i in list(range(n)):
        dataArr.append(list(map(int, input().split())))
    
    minDataAtRow = []
    for data in dataArr:
        minDataAtRow.append(min(data))

    answer = max(minDataAtRow)

    return answer


print(solution())

'''
Test Data

3 3
3 1 2
4 1 4
2 2 2


2 4
7 3 1 8
3 3 3 4
'''