# [정석 풀이 시간 복잡도 계산]
# 1. plans = input().split()
# O(m)

# 2. 2중 for문
# (1) 바깥 for문: O(m)
# (2) 안쪽 for문: O(4)
# O(m) * O(4) = O(m) * O(1) = O(m)

# 3. 총합
# O(m) + O(m) = O(m)


# [이 문제가 구현인 이유]
# 입력된 이동 명령을 규칙(경계 체크 포함)대로 한 칸씩 그대로 시뮬레이션해서 좌표를 갱신하는 문제라서 구현 문제다.


# [문제 푼 날짜]
# 1. 1월 6일 (O) 30분 15초 SLOW(>15) => 구현 자체는 맞았지만 너무 복잡하게 로직을 짬. 최대한 진행상황을 확인하며 문제를 풀기위해 쓸데없는 리스트를 너무 많이 만듦
# 2. 1월 7일 (O) 6분 52초 OK
# 3. 2월 15일 (O) 8분 21초 OK


# [정석 풀이]
n = int(input())
plans = input().split()

# 시작 위치
x = 1
y = 1

# L이면 dx = 0, dy = -1  => 행 그대로 열 감소
# R이면 dx = 0, dy = 1   => 행 그대로 열 증가
# U이면 dx = -1, dy = 0  => 행 감소 열 그대로
# D이면 dx = 1, dy = 0   => 행 증가 열 그대로
# 여기서도 마찬가지로 왕실의 나이트처럼 moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]와 같이 해도된다.
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

for i in plans:
    for j in range(len(move_types)):
        if i == move_types[j]:
            nx = x + dx[j]
            ny = y + dy[j]
            break
    
    # 이동 결과 지도 안이면 최종적으로 이동 수행
    if nx > 0 and nx <= n and ny > 0 and ny <= n:
        x = nx
        y = ny

print(x, y)


# [내가 1번째로 푼 풀이]
n = int(input())
arr = [[0] * n for _ in range(n)]
arr[0][0] = 1
move = input().split()

resultx = []
resultx.append(1)
resulty = []
resulty.append(1)

j = 0
k = 0
for i in range(len(move)):
    while True:
        if move[i] == 'L' and k > 0:
            arr[j][k-1] = 1
            k -= 1
            resultx.append(j+1)
            resulty.append(k+1)
            break
        elif move[i] == 'R' and k < n-1:
            arr[j][k+1] = 1
            k += 1
            resultx.append(j+1)
            resulty.append(k+1)
            break
        elif move[i] == 'U' and j > 0:
            arr[j-1][k] = 1
            j -= 1
            resultx.append(j+1)
            resulty.append(k+1)
            break
        elif move[i] == 'D' and j < n-1:
            arr[j+1][k] = 1
            j += 1
            resultx.append(j+1)
            resulty.append(k+1)
            break
        else:
            break

print(resultx[-1], resulty[-1])


# [내가 3번째로 푼 풀이]
n = int(input())
arr = list(input().split())

# 상 / 하 / 좌 / 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x = 0
y = 0
for i in arr:
    if i == 'U':
        nx = x + dx[0]
        ny = y + dy[0]
    elif i == 'D':
        nx = x + dx[1]
        ny = y + dy[1]
    elif i == 'L':
        nx = x + dx[2]
        ny = y + dy[2]
    else:
        nx = x + dx[3]
        ny = y + dy[3]

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue

    x = nx
    y = ny

print(x + 1, y + 1)