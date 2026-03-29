# [핵심 아이디어]
# 1. 약수 아이디어 사용
# 2. 소수 판별은 1과 자기자신 외에 약수가 있는지 확인하면 됨


# [문제 푼 날짜]
# 1. 12월 27일 (X) 핵심 아이디어는 맞았는데 range에서 범위 구현 실수
# 2. 12월 28일 (O) 11분 26초 SLOW(>10)
# 3. 1월 4일 (O) 10분 39초 OK


m = int(input())
n = int(input())

arr = []
for i in range(m, n+1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
        if cnt > 2:
            break
    
    if cnt == 2:
        arr.append(i)

if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)