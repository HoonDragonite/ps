num = int(input())

words = []
for _ in range(num):
    word = input()
    if word not in words: words.append(word)

words.sort()
words.sort(key=len)

for word in words:
    print(word)