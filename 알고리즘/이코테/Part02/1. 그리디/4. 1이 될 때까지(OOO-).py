# [시간 복잡도 계산]
# 최악의 경우: n이 1이 될때까지 계속 -1만 하는 상황
# O(n)


# [이 문제가 그리디인 이유]
# 매 단계에서 가능하면 바로 나누고, 아니면 나눌 수 있을 때까지 최소한만 1씩 빼는 선택이 항상 최적이기 때문에 그리디다.


# [문제 푼 날짜]
# 1. 1월 2일 (O) 2분 10초 OK
# 2. 2월 15일 (O) 4분 5초 OK => 기본 풀이로 풂. 다음엔 탑다운으로 풀어보기
# 3. 2월 27일(탑다운) (O) 5분 35초 OK


# [정석 풀이]
n, k = map(int, input().split())

cnt = 0
while n > 1:
    if n % k == 0:
        n = n // k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)


# [탑다운 DP를 사용한 풀이]
import sys
sys.setrecursionlimit(1000000)

n, k = map(int, input().split())

# (참고) 탑다운은 dp 테이블을 -1로 초기화하고 바텀업은 0으로 초기화하는게 좋다.
dp = [-1] * (n + 1)

def f(n):
    if n == 1:
        dp[n] = 0
        return dp[n]
    
    if n == 2:
        dp[n] = 1
        return dp[n]
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = f(n - 1) + 1

    if n % k == 0:
        dp[n] = min(dp[n], f(n // k) + 1)

    return dp[n]

print(f(n))