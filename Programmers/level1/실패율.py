def solution(N, stages):
    result = {}
    peopleCount = len(stages)
    for stage in range(1, N+1):
        if peopleCount != 0:
            count = stages.count(stage)
            result[stage] = count / peopleCount
            peopleCount -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)

'''

내가 한 풀이(시간 초과)

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
'''

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]	
print(solution(N, stages))


N = 4
stages = [4,4,4,4,4]		
print(solution(N, stages))
