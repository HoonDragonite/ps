a = int(input())
b = int(input())
c = int(input())

abc = a * b * c
array = [0 for _ in range(10)]

while True:
    if abc == 0:
        break
    
    num = int(abc % 10)
    array[num] += 1

    abc = int(abc / 10)

for i in array:
    print(i)