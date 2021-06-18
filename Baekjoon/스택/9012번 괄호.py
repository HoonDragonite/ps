# 리팩토링 ver1
# 에러 값을 스택에 저장 안하고 플래그로 처리함

dataArr = []
dataCount = int(input())

for _ in range(dataCount):
    dataArr.append(input())

for data in dataArr:
    stack = []
    isError = False

    for d in data:
        if d == "(":
            stack.append(d)
        elif d == ")":
            if len(stack) == 0:
                isError = True
                break
            if stack[-1] == "(":
                stack.pop()
            else:
                isError = True
    if len(stack) != 0:
        isError = True

    if isError == True:
        print("NO")
    else:
        print("YES")

'''
# 원래 풀이
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

'''