import sys

testCaseCount = int(input())

for _ in range(testCaseCount):
    # 자료 입력
    empScores = []
    empCount = int(input())
    for _ in range(empCount):
        empScores.append(list(map(int, sys.stdin.readline().split())))
    empScores.sort()

    # 테스트케이스별 결과
    minScore = empScores[0][1]
    result = 1
    for empScore in empScores[1:]:
        if empScore[1] < minScore: 
            result += 1
            minScore = empScore[1]
    # 결과 출력
    print(result)

'''
1. 서류점수로 오름차순으로 고정
2. 1번째 행은 무조건 합격이므로 2번째 행부터 검사
3. 면접점수는 이전 행의 면접점수보다 높아야 채용
'''