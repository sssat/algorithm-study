# [핵심 아이디어]
# 이 문제의 핵심 아이디어는 전체 그래프에서 2개의 최소 신장 트리를 만들어야 한다는 것이다.
# 가장 간단한 방법은 우선 크루스칼 알고리즘으로 최소 신장 트리를 찾은 뒤에
# 최소 신장 트리를 구성하는 간선 중에서 가장 비용이 큰 간선을 제거하는 것이다.
# 그러면 최소 신장 트리가 2개의 부분 그래프로 나누어진다.

# 예를들어 책 p.288을 보면 완성된 최소 신장 트리에서 비용이 가장 큰 간선인 53을 제거하면
# 집합이 {1, 2, 3, 4, 6, 7}과 {5}로 분할되어 2개의 최소 신장 트리가 만들어진다.

# 또한 크루스칼 알고리즘은 서로소 집합에 사이클 원리가 사용되지만 사이클 예제처럼 직접적인 cycle 변수는 사용하지 않는다.
# 즉, find 함수 + union 함수 + 부모 테이블 + 사이클 원리 사용 + edges 리스트만 정의하면 된다.


# [문제 푼 날짜]
# 1. 2월 6일 (X) => 크루스칼 알고리즘의 코드를 아직 체화하지도 못했고, 핵심 아이디어도 떠올리지 못했다.
# 2. 2월 7일 (O) 7분 17초 OK
# 3. 2월 25일 (O) 13분 38초 OK => 크루스칼 알고리즘도 마찬가지로 복습할 때 개념 및 코드 주석 부분을 한번 읽어보고
#                                "사이클이 없으면서 모든 노드로 이동할 수 있게 연결된 트리" 라는 사실만 익힌 후 
#                                 코드는 왠만하면 외우는게 좋다.       

"""
입력 그대로 복붙
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)

edges = []
result = 0

for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

# 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선
last = 0

for i in edges:
    cost, a, b = i

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

        # 위에서 edges를 정렬해서 맨 마지막에 나오는 간선의 비용이 가장 클테니 이렇게 last에 대입하면 된다.
        last = cost

print(result - last)