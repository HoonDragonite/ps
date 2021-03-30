count = int(input())
array = []
results = []

for i in range(count):
    array.append(input())

for i in array:
    point = 0
    result = 0

    for j in i:  
        if j == "O":
            point += 1
            result += point
        if j == "X":
            point = 0
    
    results.append(result)

for i in results:
    print(i)
