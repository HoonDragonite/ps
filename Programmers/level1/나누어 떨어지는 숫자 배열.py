def solution(arr, divisor):
    answer = []

    for n in arr:
        if n % divisor == 0:
            answer.append(n)
            
    answer.sort()
    
    if len(answer) == 0:
        answer.append(-1)
    
    return answer

arr = [5, 9, 7, 10]
div = 5

print(solution(arr, div))