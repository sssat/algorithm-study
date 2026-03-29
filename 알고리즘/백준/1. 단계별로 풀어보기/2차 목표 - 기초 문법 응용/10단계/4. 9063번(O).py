# [문제 푼 날짜]
# 1. 12월 29일 (O) 7분 0초 OK


n = int(input())

arr1 = []
arr2 = []
for i in range(n):
    a, b = map(int, input().split())
    arr1.append(a)
    arr2.append(b)

if n >= 2:
    x = max(arr1) - min(arr1)
    y = max(arr2) - min(arr2)

    print(x*y)

else:
    print(0)