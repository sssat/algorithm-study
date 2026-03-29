# [핵심 아이디어]
# 책 p. 148 그림 참고
# 2차원 배열에서 각 원소 하나하나를 노드라고 생각할 수 있다.
# 예를들어 책의 그림에서 (1, 1) 노드는 현재 (1, 2), (2, 1) 노드와 인접해있다.
# 이 중에서 (1, 2) 노드를 먼저 탐색한다고 한다면 이제 (1, 2) 노드는 (1, 3), (2, 2) 노드와 인접해있게 된다.
# 여기서 또 (1, 3) 노드를 탐색한다고 하면 이제 (1, 3) 노드는 (1, 2), (2, 3) 노드와 인접하는데
# (1, 2) 노드는 이미 방문한 적 있으므로 (2, 3) 노드를 탐색하게 된다.
# 이런식으로 계속해서 깊이 파고 들어가다가 더 이상 갈곳이 없으면 이전 좌표로 되돌아와서 
# 아직 탐색하지 않은 인접 좌표를 탐색한다면 이것이 DFS 이다.

# 또한 이 문제는 DFS 뿐만 아니라 BFS로도 풀 수가 있다.
# 책의 그림에서 (1, 1) 노드는 현재 (1, 2), (2, 1) 노드와 인접해있다.
# 이제 (1, 2), (2, 1) 노드들을 전부 큐에 삽입한다.
# 현재 큐: (1, 2) (2, 1)

# 이제 큐에서 (1, 2) 노드를 꺼내면 (1, 2) 노드는 현재 (1, 3), (2, 2) 노드와 인접해 있으므로
# (1, 3), (2, 2) 노드를 전부 큐에 삽입한다.
# 현재 큐: (2, 1) (1, 3) (2, 2)

# 이제 큐에서 (2, 1) 노드를 꺼내면 (2, 1) 노드는 현재 (2, 2), (3, 1) 노드와 인접해 있다.
# 근데 (2, 2) 노드는 이미 방문한적 있으므로 (3, 1) 노드만 큐에 삽입한다.
# 현재 큐: (1, 3) (2, 2) (3, 1)

# 이런식으로 풀면 BFS로도 풀 수 있다.


# [시간 복잡도 계산]
# 1. 2중 for문
# (1) 바깥 for문 => O(n)
# (2) 안쪽 for문 => O(m)
# (3) 각 칸을 처리할 때 상하좌우 4방향을 확인한다(상수) => O(4)
# (4) 총합 => O(n*m)


# [문제 푼 날짜]
# 1. 1월 15일(DFS) (X) => 구현을 못함
# 2. 1월 16일(DFS) (X) => 구현을 못함
# 3. 1월 23일(DFS) (X) => 스스로 생각해서 구현 못함. "1. DFS 예제.py" 코드랑 답지의 아이디어 본 후에는 구현함 (약 20분)
# 4. 1월 30일(DFS) (O) 15분 28초 OK
# 5. 2월 17일(DFS) (O) 28분 25초 OK
# 6. 3월 2일(DFS) (O) 17분 29초 OK
# 7. 3월 2일(BFS) (O) 21분 15초 OK 


# [DFS 정석 풀이]

"""
입력 케이스 1
4 5
00110
00011
11111
00000

입력 케이스 2
5 6
001101
000011
111000
001111
000110

입력 케이스 3
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""

# 이 문제는 별도의 인접 리스트를 만들지 않고, 2차원 격자에서 상하좌우 좌표 이동으로 인접을 처리했다.
n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input()))


# 예를들어 dfs(0, 0)이 호출 됐을 때 스택에 쌓이는 과정
# 1. dfs(0, 0) push   => arr[0][0] = 2   =>  현재 스택: dfs(0, 0)
# 2. dfs(-1, 0) push  => dfs(-1, 0) pop 
# 3. dfs(1, 0) push   => arr[1][0] = 2   =>  현재 스택: dfs(0, 0)/dfs(1, 0)
# 4. dfs(0, 0) push   => dfs(0, 0) pop
# 5. dfs(2, 0) push   => dfs(2, 0) pop
# 6. dfs(1, -1) push  => dfs(1, -1) pop
# 7. dfs(1, 1) push   => arr[1][1] = 2   =>  현재 스택: dfs(0, 0)/dfs(1, 0)/dfs(1, 1)
# 8. dfs(0, 1) push   => arr[0][1] = 2   =>  현재 스택: dfs(0, 0)/dfs(1, 0)/dfs(1, 1)/dfs(0, 1)
# 9. dfs(-1, 1) push  => dfs(-1, 1) pop
# ...
# 이런식으로 dfs(0, 0)을 호출하면 그 연결된 0들을 전부 2로 바꾸고 한번에 한 구역 씩 카운트가 된다. 
# 그리고 현재 스택에 쌓여 있는 호출들은 이미 실행 중인 dfs들이고, 
# 각 dfs는 자신이 호출한 하위 dfs들이 끝나면 차례대로 return 하면서 스택에서 빠진다.
# (이 시점의 현재 스택에 남아 있는 dfs들은 모두 '처음 방문한 0'에서 시작된 호출들이라, 최종적으로 True를 반환하고 스택에서 빠진다.)
def dfs(x, y):
    # 2중 for문에서 호출되는 dfs(0, 0), dfs(0, 1), ..... dfs(n-1, m-1)등은 좌표가 항상 격자 안이니까 이 if문을 실행하지 않지만, 
    # 예를들어 dfs(0, 0)가 호출한 상,하,좌,우 dfs들중 격자 안을 벗어나는 애들이 이 if문을 실행하여 False를 반환한다.
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:

        # 해당 노드 방문처리
        graph[x][y] = 2

        # 상/하/좌/우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True

    return False

result = 0
for i in range(n):
    for j in range(m):
        # dfs(0, 0), dfs(0, 1), ..... dfs(n-1, m-1) 까지 전부 실행
        if dfs(i, j) == True:
            result += 1

print(result)

# 출력해보면 모든 0번 칸은 전부 방문을 하게 된다.
print(graph) 


# [내가 푼 3번째 DFS 풀이]
n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input()))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    if graph[x][y] == 1 or visited[x][y] == 1:
        return False
    
    visited[x][y] = 1
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

    return True

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)


# [내가 BFS로 푼 풀이]
from collections import deque

n, m = map(int, input().split())
arr = [[] * m for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, input()))

save = [[0] * m for _ in range(n)]

# 상 / 하 / 좌 / 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if arr[x][y] == 1 or save[x][y] == 1:
        return False

    queue = deque()
    queue.append((x, y))
    save[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if arr[nx][ny] == 1 or save[nx][ny] == 1:
                continue
            
            save[nx][ny] = 1
            queue.append((nx, ny))
    
    return True

count = 0
for i in range(n):
    for j in range(m):
        if bfs(i, j) != False:
            count += 1

print(count)