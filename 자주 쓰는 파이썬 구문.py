#자료형 정리
'''
리스트 : [1, 2, 3]
딕셔너리 : {name:"sh", age="27"}
집합,set : {1,2,3} 중복과 순서가 없는
튜플 : tuple = (1,2,3) immutable한 빠른 리스트, 다익스트라 최단경로
'''

#절대값
abs()

# 입출력 가속
import sys
sys.stdin.readline() # input()을 대체

from sys import stdin, stdout
input = stdin.readline 
print = stdout.write

# 형변환
a = 10
int(a)
float(a)
str(a)
chr(a)
bool(a)

# 리스트 슬라이싱 3번째부터 5번째까지
arr = list(range(10))
arr[3-1:5]

# 배열 순회1 정해진 수만큼
len = 10
for _ in range(10):
    print("hello")

# 배열 순회2 리스트 길이만큼
numToTen = list(range(1, 11))
for i in numToTen:
    print(i)

# 문자열 순회 문자열의 문자를 순회
str = "abcde"
for c in str:
    print(c)

# 배열 순회 자기 자신 아닌 것들과 비교
dataArr = list(range(5))

for i, data in enumerate(dataArr):
    print("i : " + str(i))
    for j, otherData in enumerate(dataArr):
        if i == j: continue
        print("j : " + str(j))

# 리스트 컴프리헨션 짝수, 홀수 
evenArr = [i for i in range(1, 11) if i % 2 == 0]

# 숫자 하나 입력받기
num = int(input())

# 공백으로 구분하여 변수에 입력받기
n, m, k = map(int, input().split())

# 공백으로 구분하여 리스트에 입력받기
numArr = list(map(int, input().split()))

# 연속된 숫자를 숫자단위 배열로 입력받기 (숫자그래프)
n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# 연속된 문자를 문자단위 배열로 입력받기 (문자그래프)
arr = [list(input()) for _ in range(N)]

# 한 줄에는 수의 개수 n 가 주어지고, 다음에는 n개의 수가 주어진다
n, *arr = map(int, input().split())


# 한 배열을 중복없이 두 개의 인덱스로 순회
numbers = list(range(5))
for i, n1 in enumerate(numbers):
        for j, n2 in enumerate(numbers[i+1:]):
            print(str(n1) + ", " + str(n2))


dataArr = []
for _ in range(y):
    str = input()
    data = []
    for s in str:
        data.append(s)
    dataArr.append(data)

# 오름차순 정렬
[1, 4, 3, 2, 5].sort()
# 내림차순 정렬
[1, 4, 3, 2, 5].sort(reverse = True)

# input() 보다 빠른 문자열 입력
import sys
str = sys.stdin.readline().rstrip()

# n개의 0으로 채운 리스트 만들기
arrayOfZero = [0 for _ in range(n)]

# NxM 리스트 만들기
'''
2
1 2 3
4 5 6
'''
arr = [list(map(int, input().split())) for _ in range(int(input()))]

# NxM 행렬 리스트로 만들기
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

# 행렬 원소로 출력
for i in range(n):
    for j in range(m):
        print(array[i][j], end=" ")
    print("")

# 행렬 변환하기
scores = [[1,2,3], [4,5,6], [7,8,9]]
newScores = list(map(list, zip(*scores)))

# 특정한 값의 원소 모두 지우기, remove()는 O(n)으로 오래 걸림
arr = [1, 2, 3, 4, 5, 5, 5]
removeArr = [3, 5]

result = [i for i in arr if i not in removeArr]
print(result)

# 한 줄 비교식
print(a if a > b else b)

# 반올림하여 소숫점 2번째 자리까지 출력
print("%.2f" % 0.036)

# 일렬로 출력하기
print(arr, end=" ")

# 지수 표현
print(3**2)

# 난수 뽑기 (랜덤)
import random
random.random(1, 11) # 1부터 10까지

# 자릿수의 합
def calc10digit(num): 
    n = 0
    sum = 0
    while True:
        n = int(num % 10)
        num = int(num / 10)
        sum = sum + n
        if num == 0:
            break

    return sum

# 자릿수의 합 + 자기자신
def calc10digit2(num): 
    n = 0
    sum = 0
    sum += num
    while True:
        n = int(num % 10)
        num = int(num / 10)
        sum = sum + n
        if num == 0:
            break

    return sum

# 배열 중복 문자 제거
def deleteJungbok(arr):
    answer = []
    
    for i, a in enumerate(arr):
        if i == 0 : answer.append(a)
        else:
            if arr[i-1] == a:
                continue
            else: answer.append(a)
    
    return answer