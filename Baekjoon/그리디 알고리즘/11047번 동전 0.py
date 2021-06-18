n, k = map(int, input().split())

coinUnitArr = []

for _ in range(n):
    coinUnitArr.append(int(input()))

coinUnitArr.reverse()

count = 0
for i in coinUnitArr:
    if k >= i:
        count = count + int(k / i)
        k = k % i

print(count)