# 회의시간이 짧은 회의부터 고른다.

count = int(input())
arr = []

for _ in range(count):
    numArr = list(map(int, input().split()))
    arr.append(numArr)

sortedArr = sorted(arr, key=lambda x : x[1] - x[0])

result = 0
selectedArr = []
for i in range(count):
    if (arr[i][1] - arr[i][0] == 0): result += 1
    if len(selectedArr) == 0 : selectedArr.append(arr[i])
    for j in selectedArr:
        if selectedArr[j][0] <= arr[i][0] < selectedArr[j][1]:
            continue
        elif selectedArr[j][0] <= arr[i][0] < selectedArr[j][1]:
            continue
        else:
            result += 1

print(result)
    