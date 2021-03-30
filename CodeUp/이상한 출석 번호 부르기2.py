count = int(input())
say = list(map(int, input().split()))

say.reverse()

for i in say:
    print(i, end=" ")
    