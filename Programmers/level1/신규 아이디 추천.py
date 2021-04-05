'''
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
'''

def solution(new_id):
    new_id = levelOne(new_id)
    new_id = levelTwo(new_id)
    new_id = levelThree(new_id)    

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
    if arr[0] == ".":
        isDot = True
    else:
        isDot = False
    
    for i, c in enumerate(arr[1:]):
        if(c == "."):
            isDot = True
            arr.pop(i+1)
        else:
            isDot = False 

    new_id = ''.join(arr) 
    return new_id

def levelFour(new_id):
    result = new_id
    return result

def levelFive(new_id):
    result = new_id
    return result

def levelSix(new_id):
    result = new_id
    return result

def levelSeven(new_id):
    result = new_id
    return result

# Test
new_id = input()

print(solution(new_id))