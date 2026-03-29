# [문제 푼 날짜]
# 1. 12월 27일 (O) 9분 19초 OK


while True:
    arr = []
    n = int(input())

    if n == -1:
        break
    else:
        for i in range(1, n+1):
            if n % i == 0:
                arr.append(i)

        sum = 0
        for i in range(len(arr) - 1):
            sum += arr[i]
        
        if sum == n:
            print(f"{n} =", end = " ")
            for i in range(len(arr) - 1):
                print(arr[i], end = " ")

                if i != len(arr) - 2:
                    print("+", end = " ")
                else:
                    print()
                    break
        else:
            print(f"{n} is NOT perfect.")