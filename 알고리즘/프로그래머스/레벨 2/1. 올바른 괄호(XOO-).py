# [핵심 아이디어]
# 문자열을 왼쪽부터 순회하면서 '(' 이면 balance를 1 증가시키고, ')' 이면 balance를 1 감소시킨다.
# 이때 balance가 중간에 한 번이라도 0 미만이 되면 닫는 괄호가 더 많아졌다는 뜻이므로 바로 False를 반환한다.
# 순회가 끝난 뒤 balance가 0이면 올바른 괄호이므로 True, 0이 아니면 여는 괄호가 남아 있으므로 False를 반환한다.


# [문제 푼 날짜]
# 1. 3월 21일 (X)
# 2. 3월 28일 (O) 4분 38초 OK
# 3. 4월 10일 (O) 2분 49초 OK
# 4. 5월 1일 ()


def solution(s):
    balance = 0

    for i in s:
        if i == '(':
            balance += 1
        else:
            balance -= 1

        if balance < 0:
            return False

    if balance == 0:
        return True
    else:
        return False