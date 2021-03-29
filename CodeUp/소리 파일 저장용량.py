h, b, c, s = map(int, input().split())

data = h * b * c * s

result = round(data/8/1024/1024, 1)

print(str(result) + " MB")