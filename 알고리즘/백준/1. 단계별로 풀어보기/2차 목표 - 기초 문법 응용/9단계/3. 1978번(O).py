# [문제 푼 날짜]
# 1. 12월 27일 (O) 9분 3초 OK


n = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(len(a)):
    arr = []
    for j in range(1, a[i]+1):
        if a[i] % j == 0:
            arr.append(j)

    if len(arr) == 2:
        count += 1

print(count)
