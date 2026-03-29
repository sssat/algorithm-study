# [핵심 아이디어]
# 0. 이 문제는 "1번 -> k번 -> x번" 노드로 이동해야 하므로 한 노드에서만 출발하는 문제가 아니다. 
#    따라서 1번 노드 뿐만 아니라 k번 노드에서도 출발해야 하므로 "모든 지점에서 다른 모든 지점까지의 최단 경로"를 
#    구하는 플로이드 워셜 알고리즘을 사용해야 한다.
#    또한 문제에서 노드의 개수와 간선의 개수가 매우 작기 때문에 시간복잡도가 큰 플로이드 워셜 알고리즘을 
#    사용해야 한다고도 추측해 볼 수도 있다.

# 1. 플로이드 워셜에선 "각 노드에 연결되어있는 노드에 대한 정보를 담는 리스트" 와 "최단 거리 테이블"을 graph 하나로 공유한다.
# 2. 플로이드 워셜은 2차원 배열이므로 "노드-간선 정보 리스트 및 최단 거리 테이블" 인 graph는 n x n 형태인 인접 행렬 방식 리스트를 사용해 구현한다.
# 3. 플로이드 점화식을 사용한다.


# [문제 푼 날짜]
# 1. 2월 1일 (O) 22분 5초 OK => 입력 변수 k가 따로 있으므로 "A번 노드 -> k번 노드 -> B번 노드" 3중 루프에서 겹치지 않기 위해 k를 mid로 고쳤어야 했다.
# 2. 2월 10일 (X) => 플로이드 알고리즘 이론을 까먹음 + 인접 행렬(2차원 n x n 배열) 생성하는 방법을 까먹음 
# 3. 2월 23일 (O) 12분 8초 OK => 플로이드 워셜도 마찬가지로 복습할 때 개념 개념 및 코드 주석 부분을 한번 읽어보고 
#                                "모든 지점에서 다른 모든 지점까지의 최단 경로" 라는 사실만 익힌 후 코드는 왠만하면 외우는게 좋다.
# 4. 3월 9일 (X) 17분 28초 => 3중 for문에서 k,a,b 순서로 적었어야 했는데 a,b,k 순서로 적음. 그 외 나머지는 맞음


"""
입력 케이스 1
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

입력 케이스 2
4 2
1 3
2 4
3 4
"""

INF = int(1e9)
n, m = map(int, input().split()) # 노드 개수, 간선 개수
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 대각선 자기자신은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 간선 정보 입력
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# x, k 입력
x, k = map(int, input().split()) # 목표: 1번 노드 -> k번 노드 -> x번 노드

# A번 노드 -> B번 노드
# 만약 여기서 mid 대신 k로 쓰면 변수가 겹쳐서 틀린 답이 나온다.
# 실제로 이 루프 끝나고 print(mid) 해보면 5가 나오는 것을 알 수 있다.
# 즉, 루프가 끝나고 mid가 살아있으므로 다른 변수 명을 써줘야한다. (파이썬은 for문 변수도 루프 밖에서 마지막 값으로 남는다)
for mid in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][mid] + graph[mid][b])

# 정답 출력
distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)


# [두 번째로 푼 풀이]
n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 이렇게 k를 나중에 입력 받으면 위의 for문에서 k를 써도 된다.
x, k = map(int, input().split())

distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)