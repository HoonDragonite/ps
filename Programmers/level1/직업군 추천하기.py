def solution(table, languages, preference):
    score = [5, 4, 3, 2, 1]
    jobs = []
    scoreByJob = []
    maxScoredJobs = []
    answer = ''

    for row in table:
        jobs.append(list(row.split())[0])
        data = list(row.split())[1:]
        lanScore = 0
        for i, lan in enumerate(data):
            if lan in languages:
                lanScore += score[i] * preference[languages.index(lan)]
        scoreByJob.append(lanScore)

    #print(jobs)
    #print(scoreByJob)

    maxScore = max(scoreByJob)
    for i,v in enumerate(scoreByJob):
        if v == maxScore:
            maxScoredJobs.append(jobs[i])
    answer = sorted(maxScoredJobs)[0]

    return answer

print(solution(table=["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
,languages=["PYTHON", "C++", "SQL"], preference=[7, 5, 5]))

'''
if lan in languages:
                print(score[i], preference[languages.index(lan)])

1. table 한 줄씩 순회하면서
2. 한줄을 배열로만든다. 
3. for i, lan in enumerate(row[1:5]):
    if lan in languages[]:
        score[i] * preference[languages.idx(lan)]
4. max값 리턴

O(N^2)
'''