arr = [list(map(int, input().split())) for _ in range(9) ]

max_num = -1
row = 0
col = 0
for i in range(9):
    if max_num < max(arr[i]):
        max_num = max(arr[i])
        row = i+1
        col = arr[i].index(max(arr[i])) + 1

print(max_num)
print(row, col)