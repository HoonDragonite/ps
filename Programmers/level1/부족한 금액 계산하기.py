def solution(price, money, count):
    sum = 0 
    answer = 0

    for i in range(count):
        sum+=price*(i+1)
    if sum > money:
        answer = sum - money

    return answer

print(solution(price=3, money=20, count=4))