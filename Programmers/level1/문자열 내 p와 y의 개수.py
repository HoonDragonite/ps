def solution(s):
    answer = True
    
    countP = 0
    countY = 0
    
    for c in s:
        if c == "P" or c == "p": countP += 1
        elif c == "Y" or c == "y": countY += 1
    
    if countP == countY: answer = True
    else: answer = False

    return answer

s = "pPoooyY"
print(solution(s))