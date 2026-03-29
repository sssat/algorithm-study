# [BFS(Breadth First Search): 너비 우선 탐색]
# 가까운 노드부터 탐색하는 알고리즘
# 그래프에서 최대한 멀리 있는 노드부터 우선 탐색하는 DFS와는 반대다.
# BFS는 큐 자료구조를 사용한다.
# 인접한 노드를 큐에 넣도록 알고리즘을 작성하면 자연스럽게 가까운 노드부터 탐색을 진행하게 된다.


# [BFS 원리]
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 모든 노드들을 큐에 삽입하고 방문 처리를 한다.
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.


# [BFS 동작 과정]
# 책 p. 144 그림 참고

# <step 1>
# 시작 노드인 1번 노드를 큐에 삽입하고 방문처리를 한다.

# 큐 queue
# 1

# 방문 처리 배열 visited
# 노드 번호  1        2        3        4        5        6        7        8
# 방문 처리  True     False    False    False    False    False    False    False 

# <step 2>
# 큐에서 노드 1을 꺼내고 방문하지 않은 인접노드 2, 3, 8 을 모두 큐에 삽입하고 방문처리를 한다.

# 큐 queue
# 2  3  8

# 방문 처리 배열 visited
# 노드 번호  1        2        3        4        5        6        7        8
# 방문 처리  True     True     True     False    False    False    False    True

# <step 3>
# 큐에서 노드 2를 꺼내고 방문하지 않은 인접 노드 7을 큐에 삽입하고 방문처리를 한다.

# 큐 queue
# 3  8  7

# 방문 처리 배열 visited
# 노드 번호  1        2        3        4        5        6        7        8
# 방문 처리  True     True     True     False    False    False    True    True

# <step 4>
# 큐에서 노드 3을 꺼내고 방문하지 않은 인접노드 4, 5를 큐에 삽입하고 방문처리를 한다,

# 큐 queue
# 8  7  4  5

# 방문 처리 배열 visited
# 노드 번호  1        2        3        4        5        6        7        8
# 방문 처리  True     True     True     True     True     False    True    True

# <step 5>
# 큐에서 노드 8을 꺼냈지만 방문하지 않은 인접노드가 없으므로 무시한다.

# 큐 queue
# 7  4  5

# 방문 처리 배열 visited
# 노드 번호  1        2        3        4        5        6        7        8
# 방문 처리  True     True     True     True     True     False    True    True

# <step 6>
# 큐에서 노드 7을 꺼내고 방문하지 않은 인접노드 6을 큐에 삽입하고 방문 처리를 한다.

# 큐 queue
# 4  5  6

# 방문 처리 배열 visited
# 노드 번호  1        2        3        4        5        6        7        8
# 방문 처리  True     True     True     True     True     True    True    True

# <step 7>
# 남아 있는 노드에 방문하지 않은 인접 노드가 더 이상 없으므로 끝낸다.

# 결과적으로 노드의 탐색 순서(큐에 들어간 순서)는 다음과 같다.
# 1 -> 2 -> 3 -> 8 -> 7 -> 4 -> 5 -> 6


# [BFS 시간 복잡도]
# O(V + E)
# 시간 복잡도는 DFS와 같지만, 실제 수행 시간은 DFS보다 더 좋은 편이다.


# [BFS 소스 코드]
from collections import deque

# ------------------------------------- BFS 함수 구현 부분 -------------------------------------
def bfs(graph, start, visited):

    # deque()에는 iterable(반복 가능한 것)을 넣을 수 있다.
    queue = deque([start])

    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:

        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end = ' ')

        # 해당 원소와 연결된, 아직 방문하지 않은 모든 인접 노드들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# ------------------------------------- 인접 리스트 및 방문 처리 리스트 선언 부분 -------------------------------------
# 여기서도 마찬가지로 그래프를 무비용 인접 리스트 방식으로 표현
# 또한 여기서도 노드 번호가 낮은 순서부터 처리되게 하려면 인접 리스트에 값을 집어넣을때 노드 번호가 작은 순서대로 입력해야 한다.
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문 처리를 위한 리스트
visited = [False] * 9

# ------------------------------------- BFS 함수 호출 부분 -------------------------------------
# 정의된 BFS 함수 호출
# 맨 처음 1번 노드부터 탐색 시작
bfs(graph, 1, visited)


# ------------------------------------- 주석 없는 버전 -------------------------------------
print()
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)