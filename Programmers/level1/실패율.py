'''
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 
스테이지에 도달한 플레이어 수
'''

def solution(N, stages):
    playerCount = len(stages)
    solvingDict = {}
    solvedDict = {}
    failRateDict = {}
    answer = []

    for stage in stages:
        for i in list(range(1, stage + 1)):
            if i != N+1:
                k = i
                v = solvingDict.get(k, 0)
                solvingDict.update({k:v+1})
            if i != stage:
                k = i
                v = solvedDict.get(k, 0)
                solvedDict.update({k:v+1})
    
    for stage in list(range(1, N+1)):
        solvingPlayer = solvingDict.get(stage, 0)
        solvedPlayer = solvedDict.get(stage, 0)
        if solvingPlayer == 0:
            failRate = 0
        else:
            failRate = round((solvingPlayer - solvedPlayer) / solvingPlayer, 1)
        failRateDict.update({stage:failRate})
        
    for k, v in sorted(failRateDict.items(), reverse=True, key=lambda item: item[1]):
        answer.append(k)
    
    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]	
print(solution(N, stages))


N = 4
stages = [4,4,4,4,4]		
print(solution(N, stages))
