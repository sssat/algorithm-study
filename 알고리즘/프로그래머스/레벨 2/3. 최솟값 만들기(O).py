# [문제 푼 날짜]
# 1. 3월 21일 (O) 5분 6초 OK


def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    
    for i in range(len(A)):
        answer += (A[i] * B[len(B) - i - 1])

    return answer