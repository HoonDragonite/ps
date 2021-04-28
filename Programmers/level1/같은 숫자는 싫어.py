def solution(arr):
    answer = []
    
    for i, a in enumerate(arr):
        if i == 0 : answer.append(a)
        else:
            if arr[i-1] == a:
                continue
            else: answer.append(a)
    
    return answer


arr = [1,1,3,3,0,1,1]
arr2 = [4,4,4,3,3]	
arr3 = [2,2,2, 4,1,0,0]

print(solution(arr))
print(solution(arr3))