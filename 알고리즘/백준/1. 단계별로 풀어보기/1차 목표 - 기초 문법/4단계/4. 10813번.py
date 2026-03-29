n, m = map(int, input().split())
arr = list(range(1, n+1))    # 리스트의 요소가 오름차순으로 1부터 n까지 채워진다.

for i in range(m):
    a, b = map(int ,input().split())

    arr[a-1], arr[b-1] = arr[b-1], arr[a-1]

print(*arr)