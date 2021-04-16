count = int(input()) # 도시의 갯수
distanceArr = list(map(int, input().split())) # 거리
amtArr = list(map(int, input().split())) # 도시별 유류비

'''
   2   3   1 
5   2   4   1

나보다 싼 유류비가 나올때까지의 거리만큼을 지금 산다.
'''

result = 0

newAmtArr = amtArr[1:]
amt = amtArr[0]
result = 
for i, n in enumerate(amtArr[:-2]):
    if amt > n:
        amt = n
    result += distanceArr[i] * amt

    print("n: " + str(n))
    print("amt: " + str(amt))
    print("result: " + str(result))
    print("distance: " + str(distanceArr[i]))
    
print(result)
