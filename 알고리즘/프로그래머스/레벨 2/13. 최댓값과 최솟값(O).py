# [문제 푼 날짜]
# 1. 4월 11일 (O) 6분 35초 OK


def solution(s):
    arr = list(map(int, s.split()))
    
    a = min(arr)
    b = max(arr)
    answer = str(a) + " " + str(b)
    
    return answer