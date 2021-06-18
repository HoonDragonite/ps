goal = int(input())
groupMax = 1
count = 0

if goal == 1:
    print(goal)
else:
    while groupMax < goal:
        count += 1
        groupMax = groupMax + 6*count
    print(count + 1)