# [문제 푼 날짜]
# 1. 1월 13일 (O) 7분 31초 OK
# 2. 3월 1일 (O) 3분 15초 OK


n, m = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
for i in range(n):
    for j in range(1, n - i):
        if i != j:
            count += 1

print(count)