# [핵심 아이디어]
# 이런 문제는 펜으로 그려보면서 하자.
# 유튜브 https://www.youtube.com/watch?v=D1TsU1YTeFI 이 영상 보면서 복습하기
# 아니면 테블릿에 정리한거 보면서 복습하기


# [문제 푼 날짜]
# 1. 2월 21일(탑다운) (X) => 문제도 잘 이해하지 못했고 핵심 아이디어도 떠올리지 못함
# 2. 3월 7일(탑다운) (X)


# [탑다운 풀이]
import sys
sys.setrecursionlimit(100000)

n = int(input())

# (참고) 탑다운은 dp 테이블을 -1로 초기화하고 바텀업은 0으로 초기화하는게 좋다.
dp = [-1] * (n + 1)

def f(n):
    if dp[n] != -1:
        return dp[n]

    if n == 1:
        dp[n] = 1
        return dp[n]
    
    if n == 2:
        dp[n] = 3
        return dp[n]

    dp[n] = 1 * f(n - 1) + 2 * f(n - 2)
    return dp[n]

print(f(n) % 796796)