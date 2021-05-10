def solution(participant, completion):
    answer = ''

    myDict = {}

    for k in participant:
        v = myDict.get(k, 0)
        myDict.update({k:v+1})
    
    for k in completion:
        v = myDict.get(k)
        myDict.update({k:v-1})

    for k in participant:
        if myDict.get(k) != 0:
            answer = k

    return answer

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]	
completion = ["josipa", "filipa", "marina", "nikola"]	

print(solution(participant, completion))