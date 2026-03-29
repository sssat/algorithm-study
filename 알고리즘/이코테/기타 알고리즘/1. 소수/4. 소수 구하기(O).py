# [문제 푼 날짜]
# 1. 3월 20일 (O) 15분 21초 OK


import math

m, n = map(int, input().split())

arr = [True] * (n + 1)
arr[0] = False
arr[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

for i in range(m, len(arr)):
    if arr[i] == True:
        print(i)