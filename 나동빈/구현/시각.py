def solution(hour):
    answer = 0
    time = ""
    count = 0

    for h in range(hour+1):
        for m in range(60):
            for s in range(60):
                if "3" in str(h) + str(m) + str(s):
                    count += 1

    answer = count
    return answer

print(solution(hour=5))

'''
0 <= hour <= 23
0 <= min <= 59
0 <= sdc <= 59
'''