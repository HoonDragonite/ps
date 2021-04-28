def solution(answers):
    answer = []
    
    type1 = [1, 2, 3, 4, 5]
    type2 = [2, 1, 2, 3, 2, 4, 2, 5]
    type3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    count1 = 0
    count2 = 0
    count3 = 0
    pointer1 = 0
    pointer2 = 0
    pointer3 = 0
    for a in answers:
        if type1[pointer1] == a:
            count1 += 1
        if type2[pointer2] == a:
            count2 += 1
        if type3[pointer3] == a:
            count3 += 1
        
        if pointer1 == len(type1)-1:
            pointer1 = 0
        else: pointer1 += 1
        if pointer2 == len(type2)-1:
            pointer2 = 0
        else: pointer2 += 1
        if pointer3 == len(type3)-1:
            pointer3 = 0
        else: pointer3 += 1
    
    counts = [count1, count2, count3]
    maxCount = max(counts)

    for i, count in enumerate(counts):
        if count == maxCount:
            answer.append(i+1)
    
    return answer

answers = [1, 3, 2, 4, 2]
print(solution(answers))