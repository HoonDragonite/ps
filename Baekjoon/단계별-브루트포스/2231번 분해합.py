num = int(input())

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

result = False
for i in range(1, num+1):
    if calc10digit2(i) == num:
        result = True
        print(i)
        break

if result == False:
    print(0)