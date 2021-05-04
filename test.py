from itertools import permutations

def solution(nums):
    answer = 0

    count = int(len(nums) / 2)

    dataList = list((permutations(nums, count)))
    setList = []

    leng = 0
    for data in dataList:
        setList.append(set(data))
        if leng <= len(set(data)):
            leng = len(set(data))

    answer = leng
    return answer

'''
n마리중 n/2마리 가져가라
 N마리 폰켓몬의 종류 번호가 담긴 배열 nums가 매개변수로 주어질 때, 
 N/2마리의 폰켓몬을 선택하는 방법 중, 
 가장 많은 종류의 폰켓몬을 선택하는 방법
 
 n/2개의 원소의 중복없는 조합 중 가장 종류가 많은 것 셀렉트
'''

nums = [3,3,3,2,2,4]	
print(solution(nums))