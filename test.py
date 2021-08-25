scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]

score=[ [i[j] for i in scores] for j in range(len(scores))]
score2 = list(map(list, zip(*scores)))
print(score)
print(score2)