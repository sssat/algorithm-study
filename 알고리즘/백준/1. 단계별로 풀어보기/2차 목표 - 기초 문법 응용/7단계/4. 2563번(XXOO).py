# [핵심 아이디어]
# 1. 100행 100열 배열(도화지)을 생성한다.
# 2. 도화지를 격자(칸)로 생각해서, 색종이가 덮는 칸을 True로 표시하고 마지막에 True 개수를 세면 넓이가 된다.
# 3. 겹치는 부분은 이미 True라서 자동으로 중복 계산이 안 됨.


# [문제 푼 날짜]
# 1. 12월 18일 (X)
# 2. 12월 20일 (X)
# 3. 12월 21일 (O) 4분 50초 OK => arr.count(1)만으로는 2차원 배열에서 1 요소들의 개수를 셀 수 없다. 대신 2중 for문을 직접 작성해야한다.
# 4. 12월 28일 (O) 5분 56초 OK


import sys
input = sys.stdin.readline   # 입력을 더 빠르게 받으려고 쓴다. 물론 안써도 통과됨

arr = [[0] * 100 for _ in range(100)]  # 100행 100열 도화지
n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    for j in range(a, a+10):
        for k in range(b, b+10):
            arr[j-1][k-1] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)