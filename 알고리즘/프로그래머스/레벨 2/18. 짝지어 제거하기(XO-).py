# [핵심 아이디어]
# 이 문제는 del list로 리스트 중간 삭제 방식으로 풀면 뒤에 있는 원소들을 앞으로 당겨야 해서 O(N) 시간이 걸린다.
# 이걸 반복하면 전체 시간복잡도가 거의 O(N²) 이 걸리게 된다.

# 따라서 스택으로 풀어야 한다.
# 예를들어 "baabaa" 라면 아래와 같이 동작한다.
# b 넣음       stack = [b]
# a 넣음       stack = [b, a]
# a 만나서 제거 stack = [b]
# b 만나서 제거 stack = []
# a 넣음       stack = [a]
# a 만나서 제거 stack = []


# [문제 푼 날짜]
# 1. 5월 3일 (X) => 로직은 맞았는데 시간초과 남
# 2. 5월 4일 (O) 10분 33초 OK
# 3. 5월 18일 ()


def solution(s):
    answer = -1
    stack = []
    
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
            continue
        
        if stack[-1] != s[i]:
            stack.append(s[i])
        else:
            stack.pop()
            
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0

    return answer

