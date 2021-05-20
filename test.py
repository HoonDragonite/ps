def solution(hour):
    answer = 0

    time = ""
    count = 0
    for h in list(range(0, hour+1)):
        for m in list(range(0, 60)):
            for s in list(range(0, 60)):
                time = str(h) + str(m) + str(s)
                if "3" in time:
                    count += 1
    answer = count
    return answer

print(solution(hour=5))

'''
0 <= hour <= 23
0 <= min <= 59
0 <= sdc <= 59
'''