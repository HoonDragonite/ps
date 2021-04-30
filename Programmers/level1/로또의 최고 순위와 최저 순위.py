def rank(score):
    rank = 0
    if score == 6:
        rank = 1
    elif score == 5:
        rank = 2
    elif score == 4:
        rank = 3
    elif score == 3:
        rank = 4
    elif score == 2:
        rank = 5
    else:
        rank = 6
    return rank

def solution(lottos, win_nums):
    answer = []
    zeroCount = 0
    correct = 0

    leng = len(lottos)

    for i in list(range(leng)):
        if lottos[i] == 0:
            zeroCount += 1
        else:
            if lottos[i] in win_nums:
                correct += 1
    
    maxScore = correct + zeroCount
    minusScore = correct
    
    answer.append(rank(maxScore))
    answer.append(rank(minusScore))
    
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

lottos2 = [0, 0, 0, 0, 0, 0]
win_nums2 = [38, 19, 20, 40, 15, 25]

lottos3 = [45, 4, 35, 20, 3, 9]
win_nums3 = [20, 9, 3, 45, 4, 35]


print(solution(lottos, win_nums))
print(solution(lottos2, win_nums2))
print(solution(lottos3, win_nums3))