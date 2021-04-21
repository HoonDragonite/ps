dataArr = []
dataCount = int(input())

for _ in range(dataCount):
    dataArr.append(input())

for data in dataArr:
    stack = []
    for d in data:
        if d == "(":
            stack.append(d)
        elif d == ")" and len(stack) == 0:
            stack.append("err")
        elif d == ")" and len(stack) != 0:
            if stack[-1] == "err":
                continue
            stack.pop()
    if len(stack) == 0:
        print("YES")
    else: print("NO")
