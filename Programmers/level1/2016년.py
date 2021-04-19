import datetime

def solution(a, b):
    dayList = ['MON','TUE','WED','THU','FRI','SAT', 'SUN']
    year = 2016
    answer = dayList[datetime.date(year,a,b).weekday()]
    return answer

print(solution(5, 24))