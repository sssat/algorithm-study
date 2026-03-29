# [핵심 아이디어]
# 1. if arr[nx][ny] == 0 and save[nx][ny] == 0 => turn_time += 1 은 여기서 증가
# 2. if turn_time == 4
# => 정석 풀이 분기


# [문제 푼 날짜]
# 1. 1월 8일 (X) => 구현을 못함
# 2. 1월 10일 (X) 
# 3. 1월 11일 (O) 28분 33초 SLOW(>20)
# 4. 1월 18일 (X) => 다른건 다했는데 회전횟수 == 4 일때 구현을 못함. 또한 현재 방향에서 남쪽 direction을 빼면 반대 방향인 북쪽으로 한 칸 이동함. 마찬가지로 동쪽 방향을 빼면 서쪽 방향으로 한 칸 이동함
# 5. 1월 25일 (O) 35분 0초 OK => dx, dy 배열 채우는 과정에서 북쪽, 남쪽의 방향을 반대로 적음. turn_time == 4로 해야하는데 나는 turn_time > 4로 하려고해서 이 부분 구현하는데 시간이 오래걸림
# 6. 2월 16일 (X) => 다른건 다했는데 회전횟수 == 4 일때 구현을 못함 => 그냥 정석풀이로 풀이 방법 익히자
# 7. 2월 27일 (O) 27분 0초 OK => turn_time == 4 일때 turm_time = 0으로 초기화 하는 부분을 빼먹은 것 빼곤 다 맞게 구현함. 정석 풀이 또는 7번째 풀이로 풀이 방법 익히기


# (참고)
# 4 4 
# 1 1 0 
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
# 에서 (1, 2)의 0에서 (1, 1)의 0으로 되돌아가지 못하고 break 되는데 이렇게 구현하는게 맞는거다.


# [정석 풀이]

"""
입력 케이스
4 4 
1 1 0 
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 전체 맵 정보를 입력받기
arr = [[0] * m for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split())) 

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
d[x][y] = 1  # 현재 캐릭터의 위치 (x, y) 1로 초기화

# 북(0) / 동(1) / 남(2) / 서(3) => 인덱스 순서대로 지정해야한다.
# 북으로 이동하면 행 감소(dx = -1), 열 그대로(dy = 0)
# 동으로 이동하면 행 그대로(dx = 0), 열 증가(dy = 1)
# 참고로 여기서도 마찬가지로 왕실의 나이트처럼 moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]와 같이 해도 된다.
dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1] 

# 왼쪽으로 회전하는 함수
# 북(0) -> 서(3) -> 남(2) -> 동(1) -> 북(0) -> 서(3) -> ...
def turn_left():
    global direction      
    direction -= 1
    if direction == -1:
        direction = 3

count = 1      # 시작 위치도 방문한 칸이니까 1로 시작
turn_time = 0  # 회전 횟수
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if arr[nx][ny] == 0 and d[nx][ny] == 0:
        x = nx
        y = ny
        d[x][y] = 1
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        # 예를들어 여기서 남쪽을 바라보고 있다면 남쪽 방향의 dx[direction], dy[direction]를 빼게되면 남쪽의 반대 방향인 북쪽으로 한 칸 이동한다.
        nx = x - dx[direction]
        ny = y - dy[direction]

        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)


# [내가 7번째로 푼 풀이]
n, m = map(int, input().split())
x, y, direction = map(int, input().split())

graph = [[0] * m for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

save = [[0] * m for _ in range(n)]
save[x][y] = 1

# 북(0) / 동(1) / 남(2) / 서(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 북(0) -> 서(3) -> 남(2) -> 동(1) -> 북(0) -> 서(3)
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if graph[nx][ny] == 0:
            x = nx
            y = ny
            turn_time = 0
            continue
        else:
            break

    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        turn_time += 1
        continue

    if graph[nx][ny] == 1:
        turn_time += 1
        continue

    if save[nx][ny] == 1:
        turn_time += 1
        continue

    x = nx
    y = ny
    save[x][y] = 1
    count += 1
    turn_time = 0
    
print(count)


# [내가 4번째로 푼 풀이에서 회전횟수 == 4일때 보완한 버전]
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
arr = [[0] * m for _ in range(n)]

check = [[0] * m for _ in range(n)]
check[x][y] = 1

for i in range(n):
    arr[i] = list(map(int, input().split()))

# 북(0) / 동(1) / 남(2) / 서(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

result = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        turn_time += 1
    elif arr[nx][ny] == 1 or check[nx][ny] == 1:
        turn_time += 1
    else:
        x = nx
        y = ny
        result += 1
        check[x][y] = 1
        turn_time = 0
        continue 

    if turn_time == 4:
        # 예를들어 여기서 남쪽을 바라보고 있다면 남쪽 방향의 dx[direction], dy[direction]를 빼게되면 남쪽의 반대 방향인 북쪽으로 한 칸 이동한다.
        nx = x - dx[direction]
        ny = y - dy[direction]

        if arr[nx][ny] == 1:
            break

        x = nx
        y = ny
        turn_time = 0

print(result)


# [내가 5번째로 푼 풀이]
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
arr = [[0] * m for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

save = [[0] * m for _ in range(n)]
save[x][y] = 1

# 북 / 동 / 남 / 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 0 -> 3 -> 2 -> 1 -> 0 -> 3
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

turn_time = 0
count = 1
while True:
    turn_left()
    turn_time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    # turn_time == 4 여도 (arr[nx][ny] == 1 and save[nx][ny] == 1) 라면 전진할 수 있기 때문에 이와같이 조건문 작성함
    if turn_time == 4 and (arr[nx][ny] == 1 or save[nx][ny] == 1):
        nx = x - dx[direction]
        ny = y - dy[direction]

        if arr[nx][ny] == 0:
            x = nx
            y = ny
            turn_time = 0
        else:
            break

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    if arr[nx][ny] == 1 or save[nx][ny] == 1:
        continue

    x = nx 
    y = ny
    count += 1
    turn_time = 0
    save[nx][ny] = 1

print(count)