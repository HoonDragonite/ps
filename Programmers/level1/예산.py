def solution(d, budget):
    answer = 0
    while True:
        if budget == 0:
            break
        if len(d) != 0:
            if min(d) > budget:
                break
            else:
                answer += 1
                budget -= min(d)
                d.remove(min(d))
        else:
            break
    return answer

#print(solution([1,3,2,5,4], 9))


print(solution([3,3,1], 10))