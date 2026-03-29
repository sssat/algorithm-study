# [문제 푼 날짜]
# 1. 3월 21일 (O) 6분 54초 OK => 멀리 뛰기 문제랑 똑같다.


import sys
sys.setrecursionlimit(300000)

def solution(n):
    dp = [-1] * (n + 1)
    
    def f(n):
        if dp[n] != -1:
            return dp[n]
        
        if n == 0:
            dp[n] = 0
            return dp[n]
        
        if n == 1:
            dp[n] = 1
            return dp[n]
            
        dp[n] = (f(n - 1) + f(n - 2)) % 1234567
        return dp[n]
        
    return f(n)