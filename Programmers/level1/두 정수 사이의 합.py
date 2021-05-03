def solution(a, b):
    if a == b: return a
    elif a > b :
        tmp = a
        a = b
        b = tmp
    
    numList = list(range(a,b+1))

    answer = sum(numList)
    return answer

a = 5
b = 3

print(solution(a, b))