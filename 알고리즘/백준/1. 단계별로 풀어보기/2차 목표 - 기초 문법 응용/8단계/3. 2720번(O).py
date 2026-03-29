# [핵심 아이디어]
# 1. 예를들어 194원을 (각 동전으로 최대한 사용한 금액) 175, 10, 5, 4로 저장한다.
# 2. 그 다음 각각 25, 10, 5, 1로 나눠서 개수를 구하면 된다.


# [문제 푼 날짜]
# 1. 12월 23일 (O) 23분 40초 SLOW(>20) 


t = int(input())

for i in range(t):
    n = int(input())

    a = (n // 25) * 25
    b = ((n - a) // 10) * 10
    c = ((n - a - b) // 5) * 5
    d = (n - a - b - c)

    if a >= 25:
        print(a // 25, end = " ")
    else:
        print(0, end = " ")

    if b >= 10:
        print(b // 10, end = " ")
    else:
        print(0, end = " ")

    if c >= 5:
        print(c // 5, end = " ")
    else:
        print(0, end = " ")

    if d >= 1: 
        print(d // 1, end= " ")
    else:
        print(0, end = " ")

    print()