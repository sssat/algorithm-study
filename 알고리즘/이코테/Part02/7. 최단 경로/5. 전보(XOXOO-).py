# [핵심 아이디어]
# 0. 이 문제는 "c번 노드 -> 다른 모든 노드" 로 이동하는 문제이다.
#    따라서 출발 노드가 하나로 정해져 있으므로 "한 지점에서 다른 특정 지점까지의 최단 경로"
#    를 구하는 다익스트라 알고리즘을 사용해야 한다.
#    또한 노드의 개수와 간선의 개수가 매우 많으므로 시간 복잡도가 적은 다익스트라 알고리즘 O(E log V) 을
#    사용해야 한다고 추측해 볼 수도 있다.

# 1. 다익스트라는 플로이드 워셜과 달리 "각 노드에 연결되어있는 노드에 대한 정보를 담는 리스트" 와 "최단 거리 테이블"이 분리되어있다.
# 2. 노드-간선 정보 리스트는 값이 비어있는 n행 1열 형태인 인접 리스트인 graph를 사용해 구현한다. 
#    (참고로 노드 정보 리스트는 최단 거리 테이블과 달리 맨 처음 입력받은 값이 변화하지 않는다.)
# 3. 최단 거리 테이블 distance는 1차원 리스트로 구현한다.
# 4. 최소 힙 우선순위 큐를 사용한다.


# [문제 푼 날짜]
# 1. 2월 2일 (X) => 개선된 다익스트라 예제랑 거의 똑같은데, 내가 아직 다익스트라 코드를 체화하지 못해서 풀지 못함
# 2. 2월 3일 (O) 34분 2초 OK => 다익스트라 코드는 최대한 손으로 타이핑 해보면서 어느정도 외우는게 가장 좋다.
# 3. 2월 10일 (X) => 다익스트라 이론을 까먹음 + heapq 쓰는 방법을 까먹음 + 인접 리스트(값이 비어있는 n행 1열 배열) 생성하는 방법을 까먹음 
# 4. 2월 22일 (O) 14분 17초 OK => 다익스트라는 복습할 때 개념 및 코드 주석 부분을 한번 읽어보고 
#                                "한 지점에서 다른 특정 지점까지의 최단 경로" 라는 사실만 익힌 후 코드는 왠만하면 외우는게 좋다.
# 5. 3월 9일 (O) 18분 45초 OK


"""
입력 그대로 복붙
3 2 1
1 2 4
1 3 2
"""

import heapq
import sys
input = sys.stdin.readline

# 노드 개수, 간선 개수, 출발 노드
n, m, c = map(int, input().split())

INF = int(1e9)

distance = [INF] * (n + 1)

# 인접 리스트는 우선 n행 1열 배열로 생성하고 후에 append를 활용해서 필요한 만큼만 열을 늘리는 방식이다.
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
        
dijkstra(c)

# 도달할 수 있는 노드의 개수
count = 0

# 도달할 수 있는 노드 중에서 가장 멀리 있는 노드의 최단 거리
max_distance = 0

for i in distance:
    if i != INF:
        count += 1
        max_distance = max(max_distance, i)

# 시작 노드는 제외해야 하므로 count - 1 출력
print(count - 1, max_distance)


# [내가 2번째로 푼 풀이]
import heapq

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = int(1e9)
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist < distance[now]:
            for i in graph[now]:
                cost = dist + i[1]

                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
max_time = 0
for i in range(1, n + 1):
    if distance[i] == INF:
        continue
    else:
        if i != c:
            count += 1
            
            if max_time < distance[i]:
                max_time = distance[i]

print(count, max_time)