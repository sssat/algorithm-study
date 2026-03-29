# [기본적인 서로소 집합 알고리즘의 비효율적인 부분]
# 책 p.274 참고
# 다음과 같이 {1, 2, 3, 4, 5}의 총 5개의 원소가 존재하는 상황에서 모두 같은 집합에 속하는 경우를 가정해보자
# 구체적으로 union 연산이 순서대로 (4, 5), (3, 4), (2, 3), (1, 2)와 같이 주어졌다고 해보자
# 이때 차례대로 연산을 처리하면 다음과 같이 일렬로 나열하는 형태가 된다.

# 부모 테이블 parent
# 노드 번호  1     2     3     4     5     
#      부모  1     1     2     3     4

# 책의 그래프를 보면 1부터 5까지의 모든 원소가 루트 노드로 1이라는 값을 가진다.
# 하지만 실제로 부모 테이블에 담겨있는 값은 1, 1, 2, 3, 4 가 된다.
# 따라서 예를들어 노드 5의 루트를 찾기 위해서는 "노드 5 -> 노드 4 -> 노드 3 -> 노드 2 -> 노드 1" 의 순서대로
# 부모 노드를 거슬러 올라가야 하므로 최대 O(V)의 시간이 소요될 수 있다.

# 따라서 현재의 알고리즘을 그대로 이용하게 되면 노드의 개수가 V개이고, find 또는 union 연산의 개수가 M개일 때
# 전체 시간 복잡도는 O(VM)이 되어 비효율적이다.
# 하지만 이러한 find 함수는 아주 간단한 과정으로 최적화가 가능하다.
# 바로 경로 압축 기법을 적용하면 시간 복잡도를 개선시킬 수 있다.
# 경로 압축은 find 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 갱신하는 기법이다.

# <기존 find 함수>
# def find_parent(parent, x):
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     
#     return x

# <개선된 find 함수>
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     
#     return parent[x]

# 이렇게 함수를 수정하면 각 노드에 대하여 find 함수를 호출한 뒤에, 해당 노드의 루트 노드가 바로 부모 노드가 된다.
# 이 함수를 사용하면 다음과 같이 부모 테이블이 형성된다.

# 부모 테이블 parent
# 노드 번호  1     2     3     4     5     
#      부모  1     1     1     1     1

# 결과적으로 "경로 압축 기법"을 사용하여 find 함수를 구현하면 루트 노드에 더욱 빠르게 접근할 수 있다는 점에서
# 기존의 기본적인 서로소 집합 알고리즘과 비교했을 때 시간 복잡도가 개선된다.


# [경로 압축 기법을 사용한 개선된 서로소 집합 알고리즘 시간 복잡도]
# 노드의 개수가 V개이고, 최대 (V - 1)개의 union 연산과 find 연산이 가능할 때 
# 경로 압축 기법을 사용한 서로소 집합 알고리즘의 시간 복잡도는 O(V + M(1 + log(2-M/V)V)) 이다.
# 예를들어 노드의 개수가 1000개이고, union 및 find 연산이 총 100만 번 수행된다면 대략 1000만 번 가량의 연산이 필요하다.


# [경로 압축 기법을 사용한 개선된 서로소 집합 알고리즘]
# 개선된 서로소 집합 알고리즘에서도 마찬가지로 parent 테이블에 자기 바로 위 직접 부모 노드를 저장하지만
# find 함수를 호출하면 parent 테이블에 저장된 값이 자기 바로 위 직접 부모에서 루트 노드 값으로 업데이트 되어 저장된다.
# 따라서 해당 코드를 출력해보면 기본적인 서로소 집합 알고리즘과 달리
# 각 원소가 속한 집합과 부모 테이블에 저장된 값이 똑같은것을 알 수 있다.
# 물론 find를 호출한 노드 한정이기 때문에 find를 안해본 노드는 여전히 자기 바로 위 직접 부모 노드가 저장되어 있을 수 있다.
# => 경로 압축 기법을 사용한 find 함수로 인해 개선된 결과이다.

# (참고) 개선된 서로소 집합 알고리즘도 마찬가지로 복습할 때 개념 및 코드 주석 부분을 한번 읽어보고 코드는 왠만하면 외우는게 좋다.

"""
입력 그대로 복붙
6 4
1 4
2 3
2 4
5 6
"""

# ------------------------------------- find 연산 함수 정의 부분 -------------------------------------
def find_parent(parent, x):

    # 여기서 노드 x의 루트 노드가 자기 자신이라는 것은 재귀적으로 거슬러 올라갈 건덕지가 없다는 것이고,
    # 노드 x의 루트 노드가 자기 자신이 아니라면 해당 노드로 거슬러 올라가봐야 한다는 소리이므로
    # 루트 노드가 자기자신이 아니라면, 루트 노드가 자기 자신이 나올때까지 find 연산을 재귀적으로 호출한다.

    # 예를들어 parent = [0, 1, 2, 3, 1, 5, 6] 이고 find_parent(parent, 4)인 상황을 생각해보자
    # parent[4] == 1 이므로 parent[4] = find_parent(parent, parent[4]) = find_parent(parent, 1)을 호출한다.
    # 그럼 이제 find_parent(parent, 1)에서 parent[1] == 1 이므로 최종적으로 find_parent(parent, 4)는 1을 반환한다.
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

# ------------------------------------- union 연산 함수 정의 부분 -------------------------------------
def union_parent(parent, a, b):

    # a의 루트 노드를 찾는다.
    a = find_parent(parent, a)

    # b의 루트 노드를 찾는다.
    b = find_parent(parent, b)
    
    # a, b 중 노드 번호가 더 작은 노드가 해당 노드의 루트 노드가 된다.
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# ------------------------------------- 변수 정의 및 입력 부분 -------------------------------------
# 노드의 개수와 간선(= union 연산의 개수)의 개수 입력받기
v, e = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (v + 1)

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# ------------------------------------- union 연산 수행 부분 -------------------------------------
for i in range(e):

    # union(a, b) 수행
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# ------------------------------------- 출력 부분 -------------------------------------

# 각 원소(노드)가 속한 집합 출력 -> 각 원소(노드)의 루트노드를 출력
# 사실 위에서 union 함수를 호출하면서 find 함수도 같이 호출되기 때문에 굳이 여기서 전체 find를 한 번 더 호출할 필요는 없지만
# union 함수가 실행될 때 find가 호출되지 않은 노드가 존재할 수도 있고 
# 아래에서 경로 압축된 parent 테이블을 보여주기 위해서 한 번 더 호출할 뿐이다.
print('각 원소가 속한 집합: ', end = ' ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end = ' ')

print()

# 부모 테이블 내용 출력
# 위에서 find 함수를 한 번 더 호출했기 때문에 
# parent 테이블에 저장된 모든 노드가 루트를 직접 가리키도록 압축된다.
print('부모 테이블:', end = ' ')
for i in range(1, v + 1):
    print(parent[i], end = ' ')


# ------------------------------------- 주석 없는 버전 -------------------------------------
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

print()
v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end = ' ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end = ' ')

print()
 
print('부모 테이블: ', end = ' ')
for i in range(1, v + 1):
    print(parent[i], end = ' ')