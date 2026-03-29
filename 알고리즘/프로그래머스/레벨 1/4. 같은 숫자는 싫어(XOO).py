# [핵심 아이디어]
# (1) pop(i): 리스트의 중간이나 앞쪽에서 pop(i)를 하면, i 뒤에 있는 원소들을 앞으로 한 칸씩 당겨야 하므로 시간복잡도는 O(n)이다.
# (2) append(x): 반면 append(x)는 리스트 맨 뒤에 원소를 추가하므로 평균적으로 O(1)이다.
# (3) pop(): 또한 pop(인덱스)가 아닌 pop()은 맨 뒤 원소를 제거하므로 O(1)이다.
# (4) popleft(): deque.popleft()는 맨 앞 원소를 제거하지만 deque 자료구조라서 O(1)이다.


# [문제 푼 날짜]
# 1. 3월 19일 (X) 16분 51초 => 정확성 테스트는 다 맞았지만 효율성 테스트에서 틀림
# 2. 3월 20일 (O) 4분 43초 OK => 정석 풀이로 풀자
# 3. 3월 27일 (O) 17분 20초 OK => 맞긴 했으나 너무 복잡하게 풀었음. 정석 풀이를 잘 익히자


# [정석 풀이]
# 시간 복잡도
# (1) for문: O(n)
# (2) append: O(1)
# (3) 최종: O(n)
def solution(arr):
    answer = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            answer.append(arr[i])

    return answer


# [내가 푼 풀이 -> 효율성 테스트에서 틀린 풀이]
# 시간 복잡도
# (1) while 문: O(n)
# (2) pop(i): 중간 원소 삭제 시 뒤 원소들을 앞으로 당겨야 하므로 O(n)
# (3) 최종: O(n^2)
def solution(arr):
    answer = []
    
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            arr.pop(i)
            i -= 1
        i += 1
                
    answer = arr
    
    return answer


# [내가 3번째로 푼 복잡한 풀이]
def solution(arr):
    answer = []
    
    i = 0
    count = 1
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            count += 1
        else:
            if count >= 1:
                answer.append(arr[i])
                count = 1   
        i += 1
    
    if count >= 1:
        answer.append(arr[i])
    
    return answer