# [문제 푼 날짜]
# 1. 3월 20일 (O) 15분 21초 OK
# 2. 3월 31일 (X) => 까먹음
# 3. 4월 8일 (O) 15분 3초 OK
# 4. 4월 22일 ()


import math

m, n = map(int, input().split())

arr = [True] * (n + 1)
arr[0] = False
arr[1] = False

for i in range(2, int(math.sqrt(n)) + 1):

    # 만약 arr[i]가 이미 False라면 그 i는 합성수(소수가 아닌 수)라는 뜻이므로 그 수의 배수들은 더 작은 소수의 단계에서 이미 한번 지워졌다.
    # 예를들어 i = 2 일때 4, 6, 8, 10, ... 을 지웠고, 나중에 i = 4가 되면 arr[4]는 이미 False 인데
    # 여기서 또 8, 12, 16, .... 을 지우는건 중복 작업 이므로 arr[i]가 False라면 그 숫자는 건너뛴다.
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

for i in range(m, len(arr)):
    if arr[i] == True:
        print(i)