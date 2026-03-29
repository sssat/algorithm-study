# [문제 푼 날짜]
# 1. 3월 19일 (O) 2분 55초


def solution(s):
    answer = ''
    if len(s) % 2 == 1:
        answer = s[len(s) // 2]
    else:
        answer = s[len(s) // 2 - 1 : len(s) // 2 + 1]
    
    return answer