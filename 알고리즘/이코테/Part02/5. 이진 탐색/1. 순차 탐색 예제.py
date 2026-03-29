# [순차 탐색]
# 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
# 보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용한다.
# 파이썬의 count() 메서드도 내부에서 순차 탐색이 수행된다.
# 최악의 경우 시간 복잡도 O(n)


# [순차 탐색 코드]

"""
입력 케이스
5 Dongbin
Hanul Jonggu Dongbin Taeil Sangwook
"""

def sequential_search(n, target, arr):
    for i in range(n):
        if arr[i] == target:
            return i + 1
        
print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
a = input().split()
n = int(a[0])
target = a[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
arr = input().split()

print(sequential_search(n, target, arr))