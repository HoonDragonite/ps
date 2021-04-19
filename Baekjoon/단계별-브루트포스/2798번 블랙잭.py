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