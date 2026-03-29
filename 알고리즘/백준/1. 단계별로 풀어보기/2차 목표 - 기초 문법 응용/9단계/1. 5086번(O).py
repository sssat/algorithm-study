# [핵심 아이디어]
# 1. 어떤 자연수 p와 q가 있을 때, 만일 q를 p로 나누었을 때 나머지가 0이면 p는 q의 약수이다. 
# 2. 어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 p는 q의 배수이다.


# [문제 푼 날짜]
# 1. 12월 27일 (O) 11분 12초 OK


while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    if a < b and b % a == 0:
        print("factor")
    elif a > b and a % b == 0:
        print("multiple")
    else:
        print("neither")