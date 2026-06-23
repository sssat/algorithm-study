# [문제 푼 날짜]
# 1. 5월 3일 (O) 8분 0초 OK


def solution(arr):
    arr.sort()
    max_num = arr[-1]
    num = 1
    
    while True:
        standard = max_num * num
        
        count = 0
        for i in range(len(arr) - 1):
            if standard % arr[i] == 0:
                count += 1

        if count == len(arr) - 1:
            break
        
        num += 1
        
    return standard