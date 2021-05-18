'''
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 
스테이지에 도달한 플레이어 수
'''

def solution(N, stages):
    playerCount = len(stages)
    solvedDict = {}
    failRateDict = {}
    answer = {}

    for stage in stages:
        for i in list(range(1, stage + 1)): # 1부터 막힌 스테이지 N-1까지 깼다.
            if i != stage:
                k = i
                v = solvedDict.get(k, 0)
                solvedDict.update({k:v+1})
    
    for stage in list(range(1, N+1)):
        solvedPlayer = solvedDict.get(stage, 0)
        unsolvedPlayer = playerCount - solvedPlayer
        failRate = int(unsolvedPlayer / solvedPlayer)
        failRateDict.update({stage:failRate})
    
    print(solvedDict)
    print(failRateDict)

    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]	
print(solution(N, stages))

'''
{
    1: 7, 
    2: 4, 
    3: 2, 
    4: 1, 
    5: 1
} 
실패율이 높은 스테이지부터 내림차순으로

* 7
* 4
* 2
* 1
* 1


N = 4
stages = [4,4,4,4,4]		
print(solution(N, stages))
'''