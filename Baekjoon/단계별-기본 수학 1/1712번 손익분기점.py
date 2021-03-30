'''
총비용 < 판매비용이 되는 D를 구하라
A + B * D < C * D 가 되는 D를 구하라
D > A/(C-B)

A : 고정비
B : 가변비
C : 단가
D : 수량
'''

a, b, c = map(int, input().split())
d = 0

while True:
    d += 1
    if b >= c:
        print(-1)
        break
    if d > a / (c-b):
        print(d)
        break
