def solution(a, b):
    leng = len(a)
    
    sum = 0
    for i in list(range(leng)):
        sum += a[i]*b[i]
    
    answer = sum
    return answer

print(solution([1,2,3,4], [-3,-1,0,2]))