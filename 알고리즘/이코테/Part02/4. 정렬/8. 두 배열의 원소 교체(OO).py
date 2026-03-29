# [문제 푼 날짜]
# 1. 1월 19일 (O) 4분 45초 OK => 이 문제는 정렬을 사용한 그리디다.
# 2. 2월 19일 (O) 4분 3초 OK


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]
    else:
        break

print(sum(a))