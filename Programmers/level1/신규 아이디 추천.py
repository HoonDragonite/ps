def solution(new_id):
    new_id = levelOne(new_id)
    new_id = levelTwo(new_id)
    new_id = levelThree(new_id)    
    new_id = levelFour(new_id)
    new_id = levelFive(new_id)
    new_id = levelSix(new_id)
    new_id = levelSeven(new_id)

    answer = new_id
    return answer

def levelOne(new_id):
    result = new_id.lower()
    return result

def levelTwo(new_id): 
    for c in new_id:
        if (c.islower() == True) or (c.isdecimal() == True) or (c == "-") or (c == "_") or (c == "."):
            continue
        else:
            new_id = new_id.replace(c, "")
    return new_id

def levelThree(new_id):
    arr = list(new_id)
    resultArr = []

    for i,c in enumerate(arr):
        if len(resultArr) == 0:
            resultArr.append(arr[i])
        elif c != ".":
            resultArr.append(arr[i])
        elif c == "." and resultArr[-1] == ".":
            continue
        elif c == "." and resultArr[-1] != ".":
            resultArr.append(arr[i])

    return ''.join(resultArr)

def levelFour(new_id):
    arr = list(new_id)

    if len(arr) > 0 and arr[-1] == ".":
        arr.pop(-1)
    if len(arr) > 0 and arr[0] == ".":
        arr.pop(0)

    result = ''.join(arr)
    return result

def levelFive(new_id):
    if new_id == "":
        new_id = "a"
    return new_id

def levelSix(new_id): 
    arr = list(new_id)
    resultArr = []

    if len(arr) > 15:
        resultArr = arr[:15]
        if resultArr[-1] == ".": resultArr.pop()
    else:
        resultArr = arr

    return ''.join(resultArr)

def levelSeven(new_id): 
    arr = list(new_id)

    if 0 < len(arr) < 3:
        while len(arr) != 3:
            arr.append(arr[-1])
        result = ''.join(arr)
    else:
        result = new_id

    return result

# Test
new_id = input()

print(solution(new_id))