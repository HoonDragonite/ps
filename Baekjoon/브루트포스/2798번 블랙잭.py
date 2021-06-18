# 수의 조합은 라이브러리 사용하였음

from itertools import combinations

n, m = map(int, input().split())
cardArr = list(map(int, input().split()))

result = list(combinations(cardArr, 3))

max = 0
for z in result:
    if sum(z) <= m and sum(z) >= max:
        max = sum(z)
print(max)


'''
다른 사람의 풀이

n,m = list(map(int, input().split(' ')))
cards = list(map(int, input().split(' ')))

result = 0
length = len(cards)

# 3개만 뽑으니까 3중 반복문도 가능
for i in range (0, length):
    for j in range(i+1, length):
        for k in range (j+1, length):
            sum_value = cards[i]+cards[j]+cards[k]
            if sum_value <=m:
                result = max(result, sum_value)
print(result)

'''