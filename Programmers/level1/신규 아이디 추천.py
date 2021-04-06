'''
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
'''

def solution(new_id):
    new_id = levelOne(new_id)
    new_id = levelTwo(new_id)
    new_id = levelThree(new_id)    
    new_id = levelFour(new_id)
    new_id = levelFive(new_id)
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
    result = new_id
    return result

def levelSeven(new_id):
    result = new_id
    return result

# Test
new_id = input()

print(solution(new_id))