# [문제 푼 날짜]
# 1. 12월 29일 (O) 8분 36초 OK


while True:
    arr = list(map(int, input().split()))
    max_num = max(arr)

    if arr[0] == arr[1] == arr[2] == 0:
        break
    
    if max_num < sum(arr) - max_num:
        if arr[0] == arr[1] == arr[2]:
            print("Equilateral")
        elif arr[0] == arr[1] or arr[0] == arr[2] or arr[1] == arr[2]:
            print("Isosceles")
        elif arr[0] != arr[1] != arr[2]:
            print("Scalene")
    else:
        print("Invalid")
        