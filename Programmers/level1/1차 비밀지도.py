'''
지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 
지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다
벽 부분을 1, 공백 부분을 0

원래의 비밀지도를 해독하여 '#', 공백으로 구성된 문자열 배열로 출력하라.
'''

def solution(n, arr1, arr2):
    answer = []

    for num in list(range(n)):
        bin1 = str(bin(arr1[num]))[2:].zfill(n)
        bin2 = str(bin(arr2[num]))[2:].zfill(n)
        answerData = []
        for num2 in list(range(n)):
            if bin1[num2] == "0" and bin2[num2] == "0":
                data = " "
            else:
                data = "#"
            answerData.append(data)
        answer.append(''.join(answerData))
        
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))