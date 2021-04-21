import sys
# sys.stdin.readline()

dataArr = []
while True:
    data = input()
    if data == ".":
        break
    dataArr.append(data)
    data = ""

for data in dataArr:
    stack = []
    isError = False

    for d in data:
        if d == "(" or d == "[":
            stack.append(d)
        elif d == ")" or d == "]":
            if len(stack) == 0:
                isError = True
                break
            if d == ")" and stack[-1] == "(":
                stack.pop()
            elif d== "]" and stack[-1] == "[":
                stack.pop()
            else:
                isError = True
    if len(stack) != 0:
        isError = True
    
    if isError == True:
        print("no")
    else:
        print("yes")