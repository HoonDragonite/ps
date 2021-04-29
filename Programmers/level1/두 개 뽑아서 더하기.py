def solution(numbers):
    num1 = 0
    num2 = 0
    
    dataList = []
    for i, n1 in enumerate(numbers):
        for j, n2 in enumerate(numbers[i+1:]):
            dataList.append(n1 + n2)

    setAnswer = set(dataList)
    answer = list(setAnswer)

    answer.sort()

    return answer

numbers = [1,1,1]
print(solution(numbers))