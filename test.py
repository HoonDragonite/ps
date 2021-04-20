dataArr = list(range(5))

for i, data in enumerate(dataArr):
    print("i : " + str(i))
    for j, otherData in enumerate(dataArr):
        if i == j: continue
        print("j : " + str(j))