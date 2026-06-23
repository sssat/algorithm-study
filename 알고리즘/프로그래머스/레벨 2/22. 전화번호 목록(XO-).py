# [핵심 아이디어]
# 문자열.startswith(시작문자열): 이 문자열이 특정 문자열로 시작하는지 를 검사하는 함수

# sort를 하지 않으면 ["1195524421", "119"] 같은 경우는 체크하지 못할 수 있다.
# 파이썬에서 문자열 리스트를 정렬하면 문자열의 길이를 기준으로 정렬되는게 아니라 사전순으로 정렬된다.
# arr = ["1195524421", "97674223", "119"]를 정렬하면 ["119", "1195524421", "97674223"]와 같이 정렬된다.
# 따라서 접두어 관계가 있는 문자열들은 정렬 후 서로 인접하게 되므로,
# 모든 번호를 이중 반복문으로 비교하지 않고 인접한 번호끼리만 비교하면 된다.

# set 자료형에서는 s[0]과 같은 식으로 개별 요소에 접근이 불가능하다.


# [문제 푼 날짜]
# 1. 5월 6일 (X) 
# 2. 5월 9일 (O) 8분 22초 OK
# 3. 5월 23일 ()


# [내 2번째 풀이]
def solution(phone_book):
    answer = True
    
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        n = len(phone_book[i])
        
        if phone_book[i] == phone_book[i + 1][: n]:
            answer = False
            break
        
    return answer


# [정석 풀이]
def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    
    return True