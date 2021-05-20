n = int(input())
orderList = list(input().split())
x = 1
y = 1
for order in orderList:
    if order == "L":
        if y == 1:
            continue
        else:
            y -= 1
    elif order == "R":
        if y == n:
            continue
        else:
            y += 1
    elif order == "U":
        if x == 1:
            continue
        else:
            x -= 1
    else:
        if x == n:
            continue
        else:
            x += 1

print(str(x) + " " + str(y))

'''
5
R R R U D D
'''