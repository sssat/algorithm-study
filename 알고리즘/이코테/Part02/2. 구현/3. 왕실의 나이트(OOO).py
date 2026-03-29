# [이 문제가 구현인 이유]
# 정해진 규칙(나이트의 8가지 이동)을 그대로 좌표로 계산하고, 
# 체스판 범위만 체크해 개수를 세면 끝이라 알고리즘보다 구현(시뮬레이션) 능력이 핵심이어서 구현 문제다.


# [문제 푼 날짜]
# 1. 1월 7일 (O) 28분 20초 SLOW(>20) => 구현 자체는 맞았지만 나이트 이동을 if로 케이스 분기하여 조건문이 너무 많아짐. 이 문제는 상하좌우 문제에서 사용한 스킬과 비슷하다.
# 2. 1월 8일 (O) 7분 46초 OK 
# 3. 2월 15일 (O) 9분 37초 OK


# [정석 풀이]
n = input()
row = int(n[1])
col = ord(n[0]) - ord('a') + 1

# 나이트가 이동할 수 있는 8가지 경우의 수
# 예를들어 (2, 1)은 오른쪽으로 2칸 이동(열 2 증가), 아래로 1칸 이동(행 1 증가)
# 참고로 여기서도 마찬가지로 상하좌우에서 처럼 dx = [...], dy = [...]로 해도 된다.
move_index = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
count = 0
for i in move_index:
    if (row + i[1] > 0 and row + i[1] < 9) and (col + i[0] > 0 and col + i[0] < 9):
        count += 1

print(count)


# [내가 1번째로 푼 풀이]
a = list(input())
pos_row = int(a[1])
pos_col = ord(a[0]) - ord('a') + 1
pos = [pos_row, pos_col]

count = 0
if pos[0] + 2 < 9:
    if (pos[1] + 1 < 9):
        count += 1
    if (pos[1] - 1 > 0):
        count += 1
if pos[0] - 2 > 0:
    if (pos[1] + 1 < 9):
        count += 1  
    if (pos[1] - 1 > 0):
        count += 1 
if pos[1] + 2 < 9:
    if (pos[0] + 1 < 9):
        count += 1  
    if (pos[0] - 1 > 0):
        count += 1 
if pos[1] - 2 > 0:
    if (pos[0] + 1 < 9):
        count += 1 
    if (pos[0] - 1 > 0):
        count += 1  

print(count)


# [내가 3번째로 푼 풀이]
s = input()

# 경우의 수
# 상좌, 상우, 하좌, 하우, 좌상, 좌하, 우상, 우하
moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

x = ord(s[0]) - ord('a')
y = int(s[1]) - 1

count = 0
for i in moves:
    nx = x + i[0]
    ny = y + i[1]

    if nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
        count += 1

print(count)