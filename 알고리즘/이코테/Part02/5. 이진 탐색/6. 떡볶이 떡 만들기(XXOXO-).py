# [핵심 아이디어]
# 이 문제의 아이디어는 적절한 높이를 찾을 때까지 절단기의 높이 h를 반복해서 조정하는 것이다.
# 그래서 현재 "이 높이로 자르면 조건을 만족할 수 있는가?" 를 확인한 뒤에 조건의 만족 여부("예" or "아니오")에 따라서 탐색 범위를 좁혀 나간다.
# 절단기의 높이 h의 범위는 1 <= h <= 10억인데, 이처럼 큰 수를 보면 가장 먼저 이진 탐색을 떠올려야한다.
# 만약 높이 h를 이진탐색으로 찾는 다면 약 31번 만에 경우의 수를 모두 고려할 수 있다.
# 이때 떡의 개수 n이 최대 100만 이므로, 이진 탐색으로 절단기 h의 높이를 바꾸면서, 바꿀 때마다 모든 떡을 체크하는 경우 
# 문제의 제한시간은 2초이므로 100만 x 31 = 약 3100만 번 정도의 연산으로 문제를 풀 수 있다.

# <문제 풀이 과정>
# 예를들어 필요한 떡이 길이가 6이고, 떡의 높이가 차례대로 19, 15, 10, 17 이라고 해보자.
# 이때 시작점은 0, 끝점은 가장 긴 떡의 길이인 19으로 설정하면 중간점은 9이다.
# 9로 자르면 잘려진 떡의 합이 25가 나오는데, 이는 m보다 크므로 시작점을 증가시킨다.

# 그럼 이제 시작점은 10, 끝점은 19, 중간점은 14이다.
# 14로 잘라보면 떡의 합은 9가 나오므로, 이는 m보다 크므로 시작점을 증가시킨다.

# 그럼 이제 시작점은 15, 끝점은 19, 중간점은 17이다.
# 17로 잘라보면 떡의 합은 2가 나오는데 이는 m보다 작으므로, 끝점을 감소시킨다.

# 그럼 이제 시작점은 15, 끝점은 16, 중간점은 15이다.
# 15로 잘라보면 떡의 합은 6이 나오는데 이는 m과 같으므로 h = 15이다.

# (참고) 이 문제는 정확히 정확히 m이 가능하면 딱 맞춰야하고, 
# 정확히 m이 불가능하면 어쩔 수 없이 m보다 크게(초과해서) 잘리는 높이를 선택해야한다.
# 그래서 total < m 이 아니라 total >= m 일때 result를 갱신하는 것이다.


# [시간 복잡도]
# 1. while문 => O(log max(arr)) -> 떡의 개별 높이의 상한은 10억
# 2. for문 => O(떡의 개수 n)
# 3. 총합: O(log 10억) x O(n) = O(n log 10억) = O(100만 log 10억) = O(100만 x 30) = 약 3000만번


# [문제 푼 날짜]
# 1. 1월 20일 (X)
# 2. 1월 21일 (X) => 다른 부분은 알맞게 구현했지만, total과 m을 비교하는 범위 부분에서 result 갱신을 거꾸로 함
# 3. 1월 28일 (O) 16분 21초 OK => while의 경계조건에서 while start < end: 이라고 하는 실수함
# 4. 2월 20일 (X) => 다른 부분은 다 맞았지만, 경계조건을 잘 구현하지 못함
# 5. 3월 5일 (O) 12분 11초 OK


# [풀이 과정]

"""
입력 케이스
4 6 
19 15 10 17
"""

n, m = map(int, input().split())         # 떡의 개수, 요청한 총 길이
arr = list(map(int, input().split()))  

# target은 이 문제에선 정확히 알 수 없기 때문에 선언 안함
start = 0
end = max(arr)  # end = max(arr)-1 이라고 해도 되는데, 큰 차이는 없다.

# 참고로 여기선 arr를 가지고 탐색을 하는게 아니라 arr의 최대값을 가지고 탐색을 하는것이라서 따로 sort()를 할 필요가 없다.
result = 0
while start <= end:
    total = 0  # 잘려진 떡의 길이를 합한 값을 저장하는 변수
    mid = (start + end) // 2

    for i in arr:
        if i > mid:
            total += i - mid

    # 왼쪽 탐색 -> total이 m보다 작다는건 현재 mid는 정답이 될 수 없다는 의미이므로 result를 갱신하면 안된다.
    if total < m:
        end = mid - 1
    # 오른쪽 탐색 -> total이 m보다 크거나 같다는것은 현재 mid가 정답 후보가 될 수 있으므로 result를 갱신해도 된다.
    # 또한 초반에는 mid가 낮은 편이어서 total이 크게 나오기 쉽다 -> 따라서 오른쪽 탐색이 많이 나올 수 있지만, 어느 정도 높아지면 total이 줄면서 왼쪽/오른쪽을 번갈아 탐색하게 될것이다.
    else:
        result = mid
        start = mid + 1

print(result)


# [내가 4번째로 푼 풀이 수정본]

"""
입력 케이스
4 6 
19 15 10 17
"""

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search(arr, start, end):
    result = 0
    
    while start <= end:
        sum_len = 0
        mid = (start + end) // 2

        for i in arr:
            if i > mid:
                sum_len += (i - mid)

        # 오른쪽 탐색 -> sum_len이 m보다 크거나 같다는것은 현재 mid가 정답 후보가 될 수 있으므로 result를 갱신해도 된다.
        if sum_len >= m:
            result = mid
            start = mid + 1

        # sum_len이 m보다 작다는 것은 현재 mid가 절대 정답이 아니라서 루프를 더 돌아야 하므로 result를 갱신하면 안된다.
        else:
            end = mid - 1

    return result

print(binary_search(arr, 0, max(arr)))


# [내가 5번째로 푼 풀이]
n, m = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search(start, end):
    result = 0
    
    while start <= end:
        height = 0
        mid = (start + end) // 2

        for i in arr:
            if i > mid:
                height += (i - mid)

        if height >= m:
            start = mid + 1
            result = mid
        else:
            end = mid - 1

    return result

print(binary_search(0, max(arr)))