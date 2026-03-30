# [문제 푼 날짜]
# 1. 3월 28일 (X) => 핵심 아이디어는 알았지만 dp 문제인지 짐작조차 못함
# 2. 4월 5일 ()


import sys
sys.setrecursionlimit(300000)

def solution(land):
    n = len(land)
    dp = [[-1] * 4 for _ in range(n)]

    def f(i, j):
        # 이미 구한 값이면 재사용
        if dp[i][j] != -1:
            return dp[i][j]
        
        # 마지막 행이면 자기 자신 값
        if i == n - 1:
            dp[i][j] = land[i][j]
            return dp[i][j]

        if j == 0:
            dp[i][j] = land[i][j] + max(f(i + 1, 1), f(i + 1, 2), f(i + 1, 3))
        elif j == 1:
            dp[i][j] = land[i][j] + max(f(i + 1, 0), f(i + 1, 2), f(i + 1, 3))
        elif j == 2:
            dp[i][j] = land[i][j] + max(f(i + 1, 0), f(i + 1, 1), f(i + 1, 3))
        else:
            dp[i][j] = land[i][j] + max(f(i + 1, 0), f(i + 1, 1), f(i + 1, 2))

        return dp[i][j]

    return max(f(0, 0), f(0, 1), f(0, 2), f(0, 3))