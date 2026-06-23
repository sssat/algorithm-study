# [핵심 아이디어]
# 만약 원래 내 코드처럼 set를 안쓰고 not in words[:i + 1] 처럼 검사했다면 
# 매번 words[:i + 1]이라는 새 리스트를 만들고, 그 안에서 또 단어를 찾아야 하므로 속도가 매우 느려진다.
# 하지만 used라는 set 자료형을 만들고 매번 used에 값을 추가한 후 not in used 처럼 검사하면 훨씬 빠르게 검사할 수 있다. 


# [문제 푼 날짜]
# 1. 5월 5일 (O) 29분 22초 OK
# 2. 5월 19일 ()


import math

def solution(n, words):
    answer = []
    used = set()
    
    count = 0
    for i in range(len(words) - 1):         
        used.add(words[i])

        if words[i][-1] == words[i+1][0] and words[i+1] not in used:
            continue
        else:
            count = i + 2
            break
    
    if count == 0:
        answer = [0, 0]
    else:
        turn = math.ceil(count / n)
        human = count - (turn - 1) * n
        answer = [human, turn]

    return answer