# [핵심 아이디어]
# 이 문제는 경로 압축 기법의 서로소 집합 알고리즘 문제이다.
# 서로소 집합 알고리즘은 find 함수 + union 함수 + 부모 테이블만 정의하면 끝난다.


# [문제 푼 날짜]
# 1. 2월 6일 (X) => 경로 압축 기법의 서로소 집합 예제랑 거의 똑같은데, 내가 아직 코드를 체화하지 못해서 풀지 못함
# 2. 2월 7일 (O) 8분 45초 OK => 문제를 안보고 풀긴 했지만 어느정도 외워서 푼 감이 있으므로 코드를 이해할 수 있도록 하자.
#                              또한 서로소 알고리즘은 "도시 분할 계획" 문제에서 쓰이므로 이 문제는 여기서 끝냄
# 3. 2월 25일 (O) 12분 45초 OK => 서로소 집합도 마찬가지로 복습할 때 개념 및 코드 주석 부분을 한번 읽어보고 
#                                코드는 왠만하면 외우는게 좋다.

"""
입력 그대로 복붙
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
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

for i in range(0, n + 1):
    parent[i] = i
    
for i in range(m):
    oper, a, b = map(int, input().split()) 

    if oper == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")