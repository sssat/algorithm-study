n = int(input())
arr = list(map(int, input().split()))
temp = []

for i in range(n):
    temp.append(arr[i])

for i in range(n):
    arr[i] = (temp[i]/max(temp)) * 100

print(sum(arr)/n)