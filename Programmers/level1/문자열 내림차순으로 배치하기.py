def solution(s):
    strList = list(s)
    strList.sort(reverse=True)
    
    answer = ''.join(strList)

    return answer

s = "Zbcdefg"

print(solution(s))