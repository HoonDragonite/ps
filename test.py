def calc2(num): # 자릿수의 합 + 숫자
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


print(calc2(245))

