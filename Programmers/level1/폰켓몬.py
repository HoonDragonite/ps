
'''
원래 풀었던 것 : 그리드, 모든 경우 탐색
참고 풀이 해석
1. 나는 N/2만큼 선택한다. 
2-1 선택하는 수가 포켓몬 종류보다 같거나 많다 -> 모든 종류 선택 가능
2-2 선택하는 수가 포켓몬 종류보다 작다 -> 선택하는 수 만큼 종류 선택 가능
'''

def solution(nums):
    answer = 0
    
    N = len(nums)/2
    nums = set(nums)
    
    if N >= len(nums): answer = len(nums)
    else: answer = N
    return answer

'''
from itertools import permutations

def solution(nums):
    answer = 0

    count = int(len(nums) / 2)

    kind = len(set(nums))

    leng = 0
    for data in permutations(nums, count):
        tmpSet = set(data)
        if leng <= len(tmpSet):
            leng = len(tmpSet)
            if len == kind: break
    answer = leng
    return answer
'''

nums = [3,3,3,2,2,4]	
print(solution(nums))
