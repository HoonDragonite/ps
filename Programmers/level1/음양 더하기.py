def solution(absolutes, signs):
    leng = len(absolutes)

    sum = 0
    for i in list(range(leng)):
        if signs[i] == True: sum += absolutes[i] * 1
        else : sum += absolutes[i] * -1

    answer = sum
    
    return answer


absolutes = [4,7,12]
signs = [True, False, True]

print(solution(absolutes, signs))