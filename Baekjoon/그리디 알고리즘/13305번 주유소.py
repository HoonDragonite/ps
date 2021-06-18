count = int(input()) # 도시의 갯수
distanceArr = list(map(int, input().split())) # 거리
amtArr = list(map(int, input().split())) # 도시별 유류비

result = 0

newAmtArr = amtArr[1:]
amt = amtArr[0]
result = 0
for i, n in enumerate(newAmtArr):
    result += distanceArr[i] * amt
    if amt > n:
        amt = n
print(result)
