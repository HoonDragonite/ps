import math
from itertools import combinations

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(nums):
    answer = -1

    count = 0
    
    dataList = list(combinations(nums, 3))
    sumList = []

    for data in dataList:
        if is_prime_number(sum(data)):
            count += 1

    answer = count

    return answer


nums = [1,2,3,4]
nums2 = [1,2,7,6,4]
print(solution(nums))
print(solution(nums2))