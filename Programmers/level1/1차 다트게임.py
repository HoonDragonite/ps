def solution(dartResult):
    answer = 0
    scoreType = ["S", "D", "T"]
    scoreList = []
    score = ""
    idx = -1

    for c in dartResult:
        if c.isdigit() == True:
            score += c
        elif c in scoreType:
            scoreList.append(int(score) ** (scoreType.index(c)+1))
            idx += 1
            score = ""
        elif c == "*":
            if len(scoreList) == 1:
                scoreList[idx] *= 2
            else:
                scoreList[idx] *= 2
                scoreList[idx-1] *= 2
        elif c == "#":
            scoreList[idx] *= -1
            
    answer = sum(scoreList)
    return answer

dartResult = "1S2D*3T"
print(solution(dartResult))

dartResult = "1D2S#10S"
print(solution(dartResult))

dartResult = "1D2S0T"
print(solution(dartResult))