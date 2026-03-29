# [문제 푼 날짜]
# 1. 1월 19일 (O) 2분 50초 OK
# 2. 2월 19일 (O) 2분 20초 OK


# [1번째 풀이]
n = int(input())
arr = [0] * n

for i in range(n):
    arr[i] = int(input())

arr.sort()
for i in reversed(arr):
    print(i, end = " ")


# [2번째 풀이]
n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort(reverse = True)
for i in arr:
    print(i, end = ' ')