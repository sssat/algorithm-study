# [정석 풀이 시간 복잡도 계산]
# 1. 3중 for문
# O(n) * O(60) * O(60) = O(3600n) = O(n)


# [이 문제가 구현인 이유]
# 가능한 모든 시각(00:00:00~N:59:59)을 조건대로 하나씩 검사하며 카운트만 하면 되는 시뮬레이션(규칙 구현) 문제라서 구현 문제다.
# 또한 이 유형은 가능한 모든 경우의 수를 모두 검사해보는 방법이므로 완전 탐색 유형이다.
# 일반적으로 완전 탐색은 비효율적인 시간 복잡도를 가지고 있으므로, 데이터가 큰 경우 정상적으로 동작하지 않을 수 있지만
# 이 문제는 탐색해야할 데이터의 수가 적으므로 완전 탐색을 사용해도 된다.


# [문제 푼 날짜]
# 1. 1월 7일 (O) 24분 5초 SLOW(>15) => 구현 자체는 맞았지만 하드코딩함
# 2. 1월 8일 (O) 2분 22초 OK
# 3. 2월 15일 (O) 9분 43초 OK


# [정석 풀이]
n = int(input())

count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            str_time = str(i) + str(j) + str(k)  # 문자열로 표현한 시간: ex) 3시 2분 25초 => "3235"
            if '3' in str_time:                  # 매 시각 안에 3이 포함되어 있다면 카운트 증가
                count += 1

print(count)


# [내가 1번째로 푼 풀이]
n = int(input())
arr = [3,13,23,30,31,32,33,34,35,36,37,38,39,43,53]

count = 0
for i in range(n+1):
    for j in range(60):
        if i in arr:
            count += 3600
            break
        elif j in arr:
            count += 60
        else:
            count += 15

print(count)


# [내가 3번째로 푼 풀이]
n = int(input())

count = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(k) or '3' in str(j) or '3' in str(i):
                count += 1

print(count)