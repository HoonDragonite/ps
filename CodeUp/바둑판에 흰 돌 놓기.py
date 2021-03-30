n = 19
m = 19
array = [[0] * m for _ in range(n)]

count = int(input())
for _ in range(count):
    x, y = map(int, input().split())
    array[x-1][y-1] = 1

for i in range(n):
    for j in range(m):
        print(array[i][j], end=" ")
    print("")
    