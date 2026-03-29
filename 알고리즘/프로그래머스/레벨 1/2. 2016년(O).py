# [핵심 아이디어]
# 윤년: 2월 29일을 추가하여 1년 동안 날짜의 수가 366일이 되는 해


# [문제 푼 날짜]
# 1. 3월 19일 (O) 18분 48초


# [내가 푼 풀이]
def solution(a, b):
    answer = ''

    # 2016년 1월 1일 금요일의 인덱스
    pos = 4
    week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    # 2016년 1월 ~ 12월의 날짜 수
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 2016년 a월 b일의 day 수들의 합 -> 1월 1일 자체는 이미 포함되므로 count를 -1에서 시작
    count = -1

    for i in range(a - 1):
        count += days[i]
    count += b
    
    for i in range(count):
        pos += 1
        if pos == 7:
            pos = 0 
            
    answer = week[pos]
    
    return answer