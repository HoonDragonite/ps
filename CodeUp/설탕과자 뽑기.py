n, m = map(int, input().split())
array = [[0] * m for _ in range(n)]

count = int(input())

for i in range(count): #가로는 0 세로는 1
    l, d, x, y = map(int, input().split()) # 길이, 방향, 가장 왼위쪽 좌표

    for j in range(l):
        if d == 0:
            array[x-1][y-1+j] = 1
        if d == 1:
            array[x-1+j][y-1] = 1

for i in range(n):
    for j in range(m):
        print(array[i][j], end=" ")
    print("")
    