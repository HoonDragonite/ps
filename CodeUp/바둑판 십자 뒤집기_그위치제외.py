n = 19
m = 19
array = []

for i in range(m):
    array.append(list(map(int, input().split())))

count = int(input())
for _ in range(count):
    x, y = map(int, input().split())
    for i in range(n):
        if x-1 != i:
            if array[x-1][i] == 0:
                array[x-1][i] = 1
            else:
                array[x-1][i] = 0
    for j in range(m):
        if y-1 != j:
            if array[j][y-1] == 0:
                array[j][y-1] = 1
            else:
                array[j][y-1] = 0
for i in range(n):
    for j in range(m):
        print(array[i][j], end=" ")
    print("")
