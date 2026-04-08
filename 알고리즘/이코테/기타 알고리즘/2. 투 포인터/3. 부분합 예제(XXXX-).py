"""
<문제 설명>
길이가 N인 양의 정수 배열이 주어진다.
이 배열에서 연속된 부분 수열의 합이 정확히 M이 되는 경우의 수를 구하시오.

<입력>
첫째 줄에 정수 N, M이 주어진다.
둘째 줄에 N개의 양의 정수가 공백으로 구분되어 주어진다.

<출력>
합이 M이 되는 연속 부분 수열의 개수를 출력한다.

<예시 입력>
5 5
1 2 3 2 5

<예시 출력>
3

<설명>
합이 5가 되는 연속 부분 수열은 다음 3개이다.
2 3
3 2
5

<조건>
1 ≤ N ≤ 100,000
1 ≤ M ≤ 1,000,000,000
배열의 각 원소는 1 이상의 양의 정수
"""

# [문제 푼 날짜]
# 1. 3월 21일 (X) => 이런 문제는 개념을 이해한 후 코드는 왠만하면 외우는게 좋다. 특히 반복문 경계 조건 부분이 헷갈린다.
# 2. 3월 22일 (X) => 코드가 직관적으로 받아들여지지 않아 성능은 똑같이 유지하면서 살짝 변형했다.
# 3. 3월 29일 (X) => 아직 코드를 다 습득하지 못함
# 4. 4월 8일 (X) 18분 2초 => 처음에 sum() 함수로 했다가 시간 초과나서 다시 풂. 그 후 result < m 일때 if end == n - 1:를 안써서 틀림
# 5. 4월 22일 ()


n, m = map(int, input().split())
arr = list(map(int, input().split()))

interval_sum = 0
count = 0
start = 0
end = 0

while start < n:
    while end < n and interval_sum < m:
        interval_sum += arr[end]
        end += 1

    if interval_sum == m:
        count += 1

    interval_sum -= arr[start]
    start += 1

print(count)


# [4번째로 푼 풀이]
n, m = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
start = 0
end = 0
result = arr[0]

while start < n and end < n:
    if result > m:
        result -= arr[start]
        start += 1
    elif result < m:
        if end == n - 1:
            break
        end += 1
        result += arr[end]
    else:
        count += 1
        result -= arr[start]
        start += 1

print(count)