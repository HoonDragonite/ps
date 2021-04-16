numStr = input()

num = ""
numArr = []
result = 0

for i,c in enumerate(numStr):
    if c != "+" and c != "-":
        num += c
    else:
        numArr.append(num)
        num = "" + c
    if i == len(numStr) -1:
        numArr.append(num)

isMinus = False
for i, n in enumerate(numArr):
    if int(n) < 0:
        isMinus = True
        result += int(n)
    if isMinus == False and int(n) > 0:
        result += int(n)
    if isMinus == True and int(n) > 0:
        result -= int(n)
    #print(n)
print(result)