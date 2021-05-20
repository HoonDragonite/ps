def solution(dartResult):
    answer = 0
    scoreList = []
    score = ""
    for c in dartResult:
        if c.isdigit() == True:
            score += c
        elif c == "S":
            scoreList.append(int(score))
            score = ""
        elif c == "D":
            scoreList.append(int(score) ** 2)
            score = ""
        elif c == "T":
            scoreList.append(int(score) ** 3)
            score = ""
        elif c == "*":
            if len(scoreList) == 1:
                scoreList.append(scoreList.pop() * 2)
            else:
                now = scoreList.pop() * 2
                before = scoreList.pop() * 2
                scoreList.append(before)
                scoreList.append(now)
        elif c == "#":
            now = scoreList.pop() * -1
            scoreList.append(now)
    answer = sum(scoreList)
    return answer

dartResult = "1S2D*3T"
print(solution(dartResult))

dartResult = "1D2S#10S"
print(solution(dartResult))

dartResult = "1D2S0T"
print(solution(dartResult))