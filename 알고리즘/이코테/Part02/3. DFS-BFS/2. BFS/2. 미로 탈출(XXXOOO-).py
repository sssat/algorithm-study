# [핵심 아이디어]
# 이것 또한 DFS로도 풀 수 있지만, 이 문제는 음료수 얼려먹기 와는 달리 BFS로 푸는게 정석이다.


# [deque()에 값 넣는 법]
# 1. 빈 덱 만들고 좌표 추가
#    queue = deque()
#    queue.append((x, y))
#
# 2. 좌표 1개를 가진 덱으로 시작
#    queue = deque([(x, y)])
# (참고) # queue = deque((x, y)) 하면 안된다.


# [시간 복잡도 계산]
# 1. while queue        => O(n*m)
# 2. for i in range(4)  => O(4)
# 3. 최종: O(n*m)


# [문제 푼 날짜]
# 1. 1월 15일 (X) => 구현을 못함
# 2. 1월 16일 (X) => 거의 다 구현은 했는데, deque()에 값넣는 부분이랑 graph 카운트 하는 부분을 제대로 구현하지 못함. 이 문제는 count 변수 쓸 필요 없다
# 3. 1월 23일 (X)  => 스스로 생각해서 구현 못함. "1. BFS 예제.py" 코드 본 후에는 구현함 (35분 1초). 또한 deque에 값 넣는 부분 제대로 몰랐음 
# 4. 1월 30일 (O) 16분 27초 OK => from collections import deque, queue = deque() 를 import queue, deque = queue() 라고 해버림
# 5. 2월 17일 (O) 54분 2초 (SLOW>30) => graph 카운트 하는 부분에서 좀 헤맴
# 6. 3월 3일 (O) 15분 19초


# [정석 풀이]

"""
입력 케이스
5 6
101010
111111
000001
111111
111111
"""

from collections import deque

n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input()))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()        
    queue.append((x, y))
    
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 상/하/좌/우 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 맵 밖을 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            # 괴물이 있다면 무시
            if graph[nx][ny] == 0:
                continue
            
            # 해당 노드를 처음 방문하는 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1     # 직전 칸의 숫자 + 1
                queue.append((nx, ny))

    # 도착 위치가 (n, m) 이므로 graph[n-1][m-1] 반환
    return graph[n-1][m-1]

# 시작 위치가 (1, 1) 이므로 bfs(0, 0) 호출
print(bfs(0, 0))


# [내 6번째 풀이]
from collections import deque

n, m = map(int, input().split())

arr = [[] * m for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input()))

save = [[0] * m for _ in range(n)]
save[0][0] = 1

# 상 / 하 / 좌 / 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if arr[nx][ny] == 0:
                continue

            if save[nx][ny] == 1:
                continue

            queue.append((nx, ny))
            arr[nx][ny] += arr[x][y]
            save[nx][ny] = 1
            
    return arr[n - 1][m - 1]

print(bfs(0, 0))