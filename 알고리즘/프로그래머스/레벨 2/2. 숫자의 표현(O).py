# [문제 푼 날짜]
# 1. 3월 21일 (O) 14분 59초 OK


def solution(n):
    answer = 0
    result = 0
    
    cnt = 1
    while cnt < n + 1:
        result = 0
        
        for i in range(cnt, n + 1):
            result += i
            
            if result > n:
                cnt += 1
                break

            if result == n:
                answer += 1
                cnt += 1
                break
    return answer