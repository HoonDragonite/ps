def solution(n, lost, reserve):
    reserveSet = set(reserve) - set(lost)
    lostSet = set(lost) - set(reserve)
    
    for r in reserveSet:
        if r-1 in lostSet:
            lostSet.remove(r-1)
        elif r+1 in lostSet:
            lostSet.remove(r+1)
    answer = n - len(lostSet)
    return answer

n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))

print(solution(n, lost, reserve))