# [핵심 아이디어]
# 1. 5073번의 아이디어인 [삼각형이 되기 위한 조건: 가장 긴 변의 길이가 나머지 두 변의 길이의 합이 짧아야 한다] 를 이용해야한다.
# 2. 길이는 늘리는건 불가능하고 줄이는것만 가능하므로 만약 삼각형이 아니라면 가장 긴 변의 길이를 나머지 두 변의 길이의 합 - 1로 줄인다.
# 3. 만약 삼각형이 맞다면 그냥 세 변 더하면 답이다.


# [문제 푼 날짜]
# 1. 12월 29일 (O) 6분 16초 OK


arr = list(map(int, input().split()))
max_len = max(arr)

if max_len < sum(arr) - max_len:
    print(sum(arr))
else:
    print((sum(arr) - max_len) + (sum(arr) - max_len - 1))