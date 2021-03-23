# 형변환
a = 10
int(a)
float(a)
str(a)
chr(a)
bool(a)

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

# 리스트 컴프리헨션 짝수, 홀수 
evenArr = [i for i in range(1, 11) if i % 2 == 0]

# 공백으로 구분하여 변수에 입력받기
n, m, k = map(int, input().split())

# 공백으로 구분하여 리스트에 입력받기
numArr = list(map(int, input().split()))

# 오름차순 정렬
[1, 4, 3, 2, 5].sort()
# 내림차순 정렬
[1, 4, 3, 2, 5].sort(reverse = True)

# input() 보다 빠른 문자열 입력
import sys
str = sys.stdin.readline().rstrip()

# NxM 행렬 리스트로 만들기
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

# 특정한 값의 원소 모두 지우기, remove()는 O(n)으로 오래 걸림
arr = [1, 2, 3, 4, 5, 5, 5]
removeArr = [3, 5]

result = [i for i in arr if i not in removeArr]
print(result)
