# [핵심 아이디어]
# dp[i][j]는 (i, j) 칸에서 시작해서 마지막 행까지 내려갈 때 얻을 수 있는 최대 누적합을 의미한다.
# 예를 들어 land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]] 이면
# 최종적으로 dp = [[13,14,15,16], [8,10,11,12], [4,3,2,1]] 가 된다.
# 마지막 행은 더 내려갈 곳이 없으므로 자기 자신의 값이 그대로 저장된다.
# 그 윗행부터는 현재 칸의 값 + 다음 행에서 같은 열을 제외한 칸들 중 최대값을 더해 dp를 채운다.
# 따라서 최종 정답은 첫 번째 행에서 시작했을 때 가능한 최대값인 즉 max(dp[0]) 이 된다.


# [문제 푼 날짜]
# 1. 3월 28일 (X) => 핵심 아이디어는 알았지만 dp 문제인지 짐작조차 못함
# 2. 4월 5일 (X)
# 3. 4월 12일 ()


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