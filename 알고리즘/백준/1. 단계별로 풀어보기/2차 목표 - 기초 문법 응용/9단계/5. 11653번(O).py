# [문제 푼 날짜]
# 1. 12월 27일 (O) 8분 1초 OK


n = int(input())

i = 2
arr = []
while n >= i:
    if n % i == 0:
        n = n // i
        arr.append(i)
    else:
        i += 1

for i in range(len(arr)):
    print(arr[i])