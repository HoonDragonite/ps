num = int(input())

for i in range(1, num+1):
    check1 = i / 10
    check2 = i % 10
    if(check1 == 3 or check1 == 6 or check1 == 9):
        print("X", end=' ')
    elif(check2 == 3 or check2 == 6 or check2 == 9):
        print("X", end=' ')
    else:
        print(i, end=' ')
