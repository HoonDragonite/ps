n = 10
m = 10
x = 2
y = 2
array = []

for i in range(m):
    array.append(list(map(int, input().split())))

while True:
    if array[x-1][y-1] == 2:
        array[x-1][y-1] = 9
        break
    else:
        array[x-1][y-1] = 9
    
    if array[x-1][y] != 1:
        y += 1
        continue
    elif array[x][y-1] != 1:
        x += 1
        continue
    elif (array[x-1][y] == 1 and array[x][y-1] == 1):
        break
    break

for i in range(n):
    for j in range(m):
        print(array[i][j], end=" ")
    print("")
    