# [핵심 아이디어]
# 1. 파이썬에선 C처럼 진짜 배열을 선언만 하는건 없고, 대신 초기값으로 채운 2차원 리스트를 만들어야 한다.
# 2. 1번 배열, 2번 배열을 만들어야 한다.


# [실수 포인트]
# 1. map(함수, 반복가능한것): 여러 값에 같은 함수를 한 번에 적용해주는 함수 -> map(int, ...)로 각각의 요소들에 int 적용

# 2. a, b, c = map(int, input().split()) vs a = map(int, input().split())
# (1) a, b, c = map(int, input().split())
# 입력이 정확히 3개여야 한다.
# a, b, c에 각각 정수(int)가 저장된다.

# (2) a = map(int, input().split())
# 입력의 개수에 정해진게 없다.
# a에는 정수(int)가 들어가는게 아니라 map 객체가 들어간다. 
# 즉, a에 1, 2, 3을 입력해도 바로 쓸 수 있지 않고 나중에 하나씩 꺼내 쓸 수 있다.
# 이 문제의 a = list(map(int, input().split())) 처럼 1, 2, 3을 list로 입력받아서 a에 전달하는 식으로 사용할 수 있다.

# 3. n행 1열 리스트 vs 1행 n열 리스트 vs n행 m열 리스트 (셋 다 2차원 배열)
# 파이썬에는 c언어처럼 배열을 선언만 할 수 없기 때문에 배열을 만들기 전에 우선 틀을 제작해야한다. 그리고 그 틀 제작법은 공식처럼 외워놔도 된다.
# (1) n행 1열
# 공식: arr = [[0] for _ in range(n)]
# n행 1열: [[0],[0],[0],[0]]
# [
#     [0],
#     [0],
#     [0],
#     [0]
# ]

# (2) 1행 n열
# 공식: arr = [[0] * n]
# 1행 n열: [[0, 0, 0, 0]]
# [
#     [0, 0, 0, 0]
# ]

# (3) n행 m열
# 공식: arr = [[0] * m for _ in range(n)] or arr = [[0 for _ in range(m)] for _ in range(n)]
# 1줄 공식으로 n행 m열을 생성할때의 핵심은 행(n)이 뒤에 오고 열(m)이 앞에 온다는 것이다.
# 2줄 공식으로 2중 for문으로 생성할땐 행(n)이 바깥 for문이고, 열(m)이 안쪽 for문으로 반대이다.
# n행 m열: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# [
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ]

# 이건 3x4x1 3차원 리스트이다. 
# 쉽게말해 4행 1열 2차원 배열이 3개 있는것이라고 생각하면 된다.
# [
#   [[0],[0],[0],[0]],
#   [[0],[0],[0],[0]],
#   [[0],[0],[0],[0]]
# ]

# (4) 가변 n행 m열 배열 (행 개수는 고정, 열 개수는 가변)
# 공식: arr = [list(input().strip()) for _ in range(m)]
# 가변 n행 m열: [['h', 'd', 'f', 'a'], ['t', 't', 'd', 'h', 'a', 'd'], ['f', 'd'], ['f', 'f', 'f'], ['d']]
# [
#     ['h', 'd', 'f', 'a'], 
#     ['t', 't', 'd', 'h', 'a', 'd'], 
#     ['f', 'd'], 
#     ['f', 'f', 'f'], 
#     ['d']
# ]
# 1행은 4열, 2행은 6열 3행은 2열, 4행은 3열, 5행은 1열


# [문제 푼 날짜]
# 1. 12월 17일 (X)
# 2. 12월 20일 (X)
# 3. 12월 21일 (O) 10분 30초 SLOW(>10) => arr1, arr2 배열 생성 후 값 입력받는 input().split() 부분에서 헤맴
# 4. 12월 28일 (O) 4분 9초 OK


n, m = map(int, input().split())

arr1 = [[0] * m for _ in range(n)]      # <=> [[0 for _ in range(m)] for _ in range(n)] : n행 m열 배열
arr2 = [[0] * m for _ in range(n)]      # <=> [[0 for _ in range(m)] for _ in range(n)] : n행 m열 배열
for i in range(n):
    a = list(map(int, input().split())) # map(int, input().split())만 arr1[i]에 집어넣으면 list가 아니라 map 객체를 넣는것이 되므로, 마지막에 list로 만들어줘야 한다.
    arr1[i] = a

for i in range(n):
    a = list(map(int, input().split()))
    arr2[i] = a

for i in range(n):
    for j in range(m):
        print(arr1[i][j] + arr2[i][j], end = " ")
    print()
        