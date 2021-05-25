from itertools import permutations

n, m = map(int, input().split())

nums = list(range(1, n+1))

datas = list(permutations(nums, m))

for data in datas:
    for d in data:
        print(d, end=' ')
    print()