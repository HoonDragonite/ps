def solution(n):
    answer = ""
    
    i = 0
    while True:
        if i == n: break
        if i % 2 == 0: answer += "수"
        else: answer += "박"
        i += 1
    return answer

'''
def solution(n):
    s = "수박" * n
    return s[:n]
'''