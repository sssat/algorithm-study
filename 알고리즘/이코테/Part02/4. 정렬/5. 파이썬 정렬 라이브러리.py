# [파이썬 정렬 라이브러리]
# 파이썬의 sort()/sorted()는 매우 최적화되어 있어 실전 코테에서는 보통 내장 정렬을 활용한다.
# 그래서 정렬 알고리즘(선택/삽입/퀵 등)을 직접 구현을 요구하는 문제는 상대적으로 드물고,
# sort()/sorted() 등의 정렬 라이브러리를 활용한 응용 문제(그리디, 이분 탐색, 투포인터 등)가 더 많이 나온다.

# 파이썬의 sorted() 함수와 리스트 메서드 sort()는 Timsort 기반이다.
# Timsort는 병합 정렬과 삽입 정렬의 아이디어를 결합한 하이브리드 정렬이며,
# 평균적으로 O(n log n), 최악의 경우에도 O(n log n)을 보장한다.


# [1. sorted(iterable) 함수]
# sorted(iterable) 함수는 원본은 그대로 유지한 채 새 리스트를 반환한다. 
# 또한 리스트 뿐 아니라 모든 iterable(튜플, 문자열, set, dict의 keys 등)에 사용 가능하다.
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = sorted(arr)
print("arr =", arr)
print("result =", result)
print()


# [2. list.sort()]
# sort()는 리스트 원본 자체를 정렬시킨다.
# 오직 list 뒤에 붙어서만 사용할 수 있다.
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
arr.sort()
print("arr =", arr)
print()


# [3. sorted(iterable), list.sort()의 공통점]
# sorted(iterable)나 list.sort()는 모두 key 매개변수를 입력으로 받을 수 있다
arr = [('사과', 5), ('바나나', 2), ('당근', 3)]  # 튜플들을 원소로 갖는 리스트

def setting(data):
    return data[1]

result = sorted(arr, key = setting)
print(result)