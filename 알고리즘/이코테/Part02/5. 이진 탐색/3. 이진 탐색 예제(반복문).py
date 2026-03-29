# (참고) 정렬은 보통 파이썬 내장 정렬을 사용하면 되지만, 이진 탐색은 코테에서 매우 자주 등장하므로
# 자주 쓰이기 때문에 구현 할 줄 알아야 한다.
# 또한 실전 코테를 위해 재귀보다는 반복문으로 구현 연습하자


# [반복문 이진 탐색]

"""
입력 케이스
10 7
1 3 5 7 9 11 13 15 17 19
"""

def binary_search(arr, target, start, end):
    
    # 찾는 원소가 없을때까지 반복
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None
    
n, target = map(int, input().split())
arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)