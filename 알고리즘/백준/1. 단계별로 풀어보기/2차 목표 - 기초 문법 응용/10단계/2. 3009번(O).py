# [문제 푼 날짜]
# 1. 12월 29일 (O) 17분 46초 OK


arr1 = []
arr2 = []

for i in range(3):
    a = list(map(int, input().split()))
    arr1.append(a[0])
    arr2.append(a[1])

if arr1[0] == arr1[1]:
    x = arr1[2]
elif arr1[1] == arr1[2]:
    x = arr1[0]
else:
    x = arr1[1]

if arr2[0] == arr2[1]:
    y = arr2[2]
elif arr2[1] == arr2[2]:
    y = arr2[0]
else:
    y = arr2[1]

print(x, y)