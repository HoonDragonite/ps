myMoney = 1000
price = int(input())
change = myMoney - price
cnt = 0

# 500엔, 100엔, 50엔, 10엔, 5엔, 1엔

while change != 0:
    if change >= 500:
        cnt += int(change / 500)
        change = int(change % 500)
    elif change >= 100:
        cnt += int(change / 100)
        change = int(change % 100)
    elif change >= 50:
        cnt += int(change / 50)
        change = int(change % 50)
    elif change >= 10:
        cnt += int(change / 10)
        change = int(change % 10)
    elif change >= 5:
        cnt += int(change / 5)
        change = int(change % 5)
    elif change >= 1:
        cnt += int(change / 1)
        change = int(change % 1)

print(cnt)