# [문제 푼 날짜]
# 1. 3월 27일 (O) 22분 27초 OK


# 78
# 39 - 0
# 19 - 1
# 9 - 1
# 4 - 1
# 2 - 0
# 1 - 0
# 0 - 1
def solution(n):
    answer = 0
    
    # 2진수 변환 함수
    def f(n):
        # 몫/나머지/나머지 담을 리스트
        a = n // 2
        b = n % 2
        arr = [b]
        
        while a > 0:
            b = a % 2
            a = a // 2
            arr.append(b)
        
        count = 0
        for i in arr:
            if i == 1:
                count += 1
            
        return count
    
    result = f(n)
    i = n + 1
    while True:
        if result == f(i):
            answer = i
            break
        
        i += 1
    
    return answer