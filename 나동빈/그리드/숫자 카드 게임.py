def solution():
    n, m = map(int, input().split())

    dataArr = []

    minDataArr = []
    for i in range(n):
        data = list(map(int, input().split()))
        minData = min(data)
        minDataArr.append(minData)

    answer = max(minDataArr)

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