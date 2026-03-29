# [핵심 아이디어]
# 1. 노드-간선 정보 리스트는 값이 비어있는 n행 1열 형태의 인접 리스트인 graph를 사용해 구현한다. 
# 2. 진입차수 테이블 indegree는 1차원 리스트로 구현한다.
# 3. 큐에서 빠져나간 노드를 순서대로 담을 리스트 result를 구현한다.
# => 이 문제는 위상 정렬 문제이면서 구현까지도 빡쎄게 해야하는 매우 어려운 문제다.


# [문제 푼 날짜]
# 1. 2월 12일 (X) => 


"""
입력 케이스 1
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

입력 케이스 2
3 
10 -1
1 -1
5 1 2 -1
"""

from collections import deque
import copy

# 노드의 개수
v = int(input())

# 진입차수 테이블 indegree
indegree = [0] * (v + 1)

# 노드-간선 정보 리스트 -> n x 1 인접 리스트 방식
graph = [[] for _ in range(v + 1)]

# 각 강의 시간을 0으로 초기화
time = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v + 1):

    # n번째 과목의 강의 시간과 선수과목 정보를 입력받음
    # i=1 일때 data = [10, -1]
    # i=2 일때 data = [10, 1, -1]
    # ...
    data = list(map(int, input().split()))

    # data의 첫 번째 수는 각 과목의 수강 시간 수를 담고있음
    # time = [0, 10, 10, 4, 4, 3]
    time[i] = data[0]

    # data의 선수과목 정보를 토대로 인접 리스트 및 진입차수 테이블 값 채우기
    # i=1 일때 data = [10, -1]
    # i=2 일때 data = [10, 1, -1]
    # ...
    for j in data[1:-1]:

        # 노드 j에서 노드 i로 이동 가능 (인접 리스트 방식)
        # graph = [[], [2, 3, 4], [], [4, 5], [], []]
        graph[j].append(i)

        # 우선 입력 받은대로 입력 차수를 증가시킴
        # indegree = [0, 0, 1, 1, 2, 1]
        indegree[i] += 1

# 위상 정렬 함수
def toplogy_sort():

    # 알고리즘 수행 결과를 담을 리스트 => time 리스트를 그대로 복제해서 result에 넣음
    # 여기서 굳이 deepcopy를 사용한 이유는 
    # 만약 result = time을 해서 복제하면 둘이 같은 리스트(같은 객체) 를 가리키기 때문에
    # result[i]를 바꾸면 time[i]도 같이 바뀐다.
    # 반면 result = copy.deepcopy(time)로 새 리스트를 만들면
    # result만 갱신되고, 원래 time은 그대로 유지된다.
    # time = [0, 10, 10, 4, 4, 3]
    # result = [0, 10, 10, 4, 4, 3]
    result = copy.deepcopy(time)

    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    # indegree = [0, 0, 1, 1, 2, 1]
    # q = deque([1])
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        
        # 큐에서 원소 꺼내기
        now = q.popleft()

        # graph = [[], [2, 3, 4], [], [4, 5], [], []]
        # graph[now] = [2, 3, 4]
        for i in graph[now]:

            # now 노드에서 출발하는 간선들을 제거한다. (= now 노드와 연결된 노드들의 진입차수에서 1을 뺀다.)
            # indegree = [0, 0, 1, 1, 2, 1]
            indegree[i] -= 1

            # result = [0, 10, 10, 4, 4, 3]
            # time = [0, 10, 10, 4, 4, 3]
            result[i] = max(result[i], result[now] + time[i])
        
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in range(1, v + 1):
        print(result[i])

toplogy_sort()