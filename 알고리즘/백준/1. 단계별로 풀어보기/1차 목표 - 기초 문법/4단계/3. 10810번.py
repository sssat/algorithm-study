n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(0)

for i in range(m):
    a, b, c = map(int, input().split())
    
    for j in range(a-1, b):
        arr[j] = c

for i in range(len(arr)):
    print(arr[i], end = " ")