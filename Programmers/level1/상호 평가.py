def solution(scores):
    answer = ""
    scoreByStudent = []
    averScoreByStudent = []

    # 빈 2차원 리스트 생성
    for _ in range(len(scores)):
        scoreByStudent.append([])

    # 학생별 점수 배열 생성
    for score in scores:
        for i,s in enumerate(score):
            scoreByStudent[i].append(s)

    # 자기점수가 유일한 최고점, 최소점인지 확인 
    for i, score in enumerate(scoreByStudent):
        if score[i] == max(score) or score[i] == min(score):
            if score.count(score[i]) == 1:
                scoreByStudent[i].remove(score[i])
        averScoreByStudent.append(sum(score)/len(score))

    # 학점 계산
    for score in averScoreByStudent:
        answer += calcGrade(score)

    return answer

def calcGrade(score):
    if score >= 90:
        return "A"
    elif 90 > score >= 80:
        return "B"
    elif 80 > score >= 70:
        return "C"
    elif 70 > score >= 50:
        return "D"
    else:
        return "F"

'''
1. 각 학생이 받은 점수 배열 생성 
2. 자기 자신에게 준 점수가 유일한 최고점 or 유일한 최소점 확인
3. 학생별 학점
'''

#print(solution(scores=[[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
print(solution(scores=[[50,90],[50,87]]	))
#print(solution(scores=[[70,49,90],[68,50,38],[73,31,100]]	))