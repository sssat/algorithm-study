# [시간 복잡도 계산]
# 1. arr = [[0] * m for _ in range(n)]
# O(n*m)

# 2. for문
# (1) for문 자체
# O(n) : n번 반복

# (2) arr[i] = list(map(int, input().split()))
# O(m) : m개의 요소 입력

# (3) if문에서 min(arr[i])
# O(m) : m개의 요소 비교
# 파이썬에서 min 함수의 시간복잡도는 O(입력 원소의 개수)

# (4) if문 안에서 min(arr[i])
# O(m) : m개의 요소 비교
# 총합: O(n) * (O(m) + O(m) + O(m)) = O(n) * O(3m) = O(n*m)

# 3. 총합
# O(n*m) + O(n*m) 
# 따라서 O(n*m) 
# 참고로 이 문제는 최선의 경우와 최악의 경우가 같다.


# [이 문제가 그리디인 이유]
# 각 행을 선택하면 결과가 그 행의 최솟값으로 고정되므로, 가능한 결과들(각 행의 최솟값) 중 가장 큰 값을 고르는 선택이 항상 최적이라서 그리디다.


# [문제 푼 날짜]
# 1. 1월 2일 (O) 6분 7초 OK
# 2. 2월 15일 (O) 5분 22초 OK


n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

min_num = 0
for i in range(n):
    arr[i] = list(map(int, input().split()))

    if min_num < min(arr[i]):
        min_num = min(arr[i])

print(min_num)