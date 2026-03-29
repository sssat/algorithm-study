# [시간 복잡도 계산]
# 1. arr1 = list(map(int, input().split()))
# O(n)

# 2. arr1.sort()
# O(n log n)

# 3. for문 
# (1) for문 자체
# 최악의 경우: O(n)

# (2) max(arr2)
# 최악의 경우: O(n)

# 4. 총합
# O(n) + O(n log n) + (O(n) * O(n))
# O(n) + O(n log n) + O(n^2)
# 지배항 기준: O(n^2)
# 하지만 이 문제의 n 범위는 1 <= n <= 100000 이므로 이대로 제출하면 시간초과로 오답이다.
# 따라서 시간 복잡도가 O(n log n)인 풀이로 풀어야한다.
# 다음 부터는 문제 풀 때 우선 n의 범위를 확인하고 허용되는 급을 미리 잡고 문제에 접근해야한다.


# [이 문제가 그리디인 이유]
# 공포도를 오름차순으로 정렬한 뒤 가장 작은 공포도부터 인원을 모아 "현재 인원 ≥ 현재 공포도"가 되는 순간 
# 바로 그룹을 확정하는 선택이 이후 선택을 절대 나쁘게 만들지 않아 항상 최적이기 때문에 그리디다.


# [문제 푼 날짜]
# 1. 1월 2일 (x) 20분 48초 => 핵심 아이디어는 맞았지만 시간 초과함. 내 로직은 O(n^2)이라 n이 10만일때 100억번의 연산 수행
# 2. 1월 3일 (O) 17분 17초 (SLOW>10)
# 3. 1월 11일 (O) 7분 31초 OK
# 4. 2월 27일 (O) 3분 32초 OK


# [내 원래 풀이]
"""
n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()

arr2 = []
cnt = 0
for i in range(len(arr1)):
    arr2.append(arr1[i])

    if max(arr2) == len(arr2):
        cnt += 1
        arr2 = []
    else:
        pass

print(cnt)
"""


# [시간 복잡도 초과하지 않는 정석 풀이]
# 어차피 arr2[-1]가 최대값일 것이므로 max() 함수 대신 arr2[-1]를 사용해 시간 복잡도를 개선함
# 따라서 복잡도에서 가장 큰 비중을 차지하던 max()가 사라져서 루프가 O(n)으로 내려갔고, 정렬 O(n log n)이 지배항이 됐다.
n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()

arr2 = []
cnt = 0
for i in range(len(arr1)):
    arr2.append(arr1[i])

    if arr2[-1] >= len(arr2):   # if arr1[i] >= len(arr2) 이렇게 해도 된다
        cnt += 1
        arr2 = []

print(cnt)


# [4번째 풀이]
n = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = 0
cnt = 0
for i in arr:
    cnt += 1

    if i == cnt:
        result += 1
        cnt = 0

print(result)