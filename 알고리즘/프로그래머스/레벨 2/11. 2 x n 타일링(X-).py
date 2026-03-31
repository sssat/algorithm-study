# [핵심 아이디어]
# dp 문제 중 타일링 문제는 그려가면서 풀기


# [문제 푼 날짜]
# 1. 3월 31일 (X) 26분 3초 => 거의 다 맞았는데 dp 배열을 f(n) 안에 선언해서 dp 배열이 매번 초기화되어 시간초과남
# 2. 4월 7일 ()


import sys
sys.setrecursionlimit(100000)

def solution(n):
    dp = [-1] * (n + 1)
    
    def f(n):
        if dp[n] != -1:
            return dp[n]
        if n == 1:
            dp[n] = 1
            return dp[n]
        if n == 2:
            dp[n] = 2
            return dp[n]

        dp[n] = (f(n - 1) + f(n - 2)) % 1000000007
        return dp[n]

    return f(n)