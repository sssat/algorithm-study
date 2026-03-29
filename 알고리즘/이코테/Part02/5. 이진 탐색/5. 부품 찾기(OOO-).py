# [시간 복잡도]
# 1. arr.sort() => O(n log n)

# 2. for 문 
# (1) for i in arr2 => O(m)
# (2) binary_search() => O(log n)
# (3) 합 => O(m log n)

# 3. 총합
# O(n log n) + O(m log n)
# => O((m+n) log n)


# [문제 푼 날짜]
# 1. 1월 20일 (O) 16분 51초 OK
# 2. 2월 20일 (O) 8분 3초 OK
# 3. 3월 5일 (O) 10분 6초 OK


"""
입력 케이스
5
8 3 7 9 2
3
5 7 9
"""

n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


for i in arr2:
    if binary_search(arr1, i, 0, len(arr1) - 1) is None:
        print("no", end = ' ')
    else:
        print("yes", end = ' ')