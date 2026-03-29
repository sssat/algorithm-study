# [핵심 아이디어]
# (이름, 점수) 형태의 튜플을 리스트에 저장한 뒤, key를 점수로 두고 오름차순 정렬한다.


# [문제 푼 날짜]
# 1. 1월 19일 (X) => 딕셔너리에 직접 입력을 받으려고 해서 못품
# 2. 1월 20일 (X) => 리스트에 튜플을 입력받는 부분을 잘 구현 못함 + setting 함수의 return에 int를 안씌움
# 3. 1월 27일 (O) 14분 15초 OK => setting 함수를 만들어놓고 arr.sort() 에서 setting 함수 사용하는 법이 잘 기억이 안나서 살짝 헤맴
# 4. 2월 19일 (X) => a를 입력받을 때 (a[0], int(a[1])) 이와 같이 두번째 원소의 타입을 int로 전환해줘야 했는데 하지 않음 -> 나는 arr.append(tuple(a)) 이렇게만 함
# 5. 3월 4일 (O) 4분 2초 OK


# [정석 풀이]

"""
입력 케이스
2
홍길동 95
이순신 77
"""
n = int(input())
arr = []

for i in range(n):
    a = input().split()
    arr.append((a[0], int(a[1])))  # arr: 튜플들을 원소로 갖는 리스트

def setting(data):
    return data[1]

# sorted(arr, key) : key 함수가 만든 값 기준으로 오름차순 정렬 => 여기선 key 함수가 만든 값인 data[1] 기준으로 오름차순 정렬
arr = sorted(arr, key = setting)
for i in arr:
    print(i[0], end = " ")


# [내가 2번째로 푼 풀이 수정본]
n = int(input())
arr = [0] * n

for i in range(n):
    arr[i] = tuple(input().split())
    # arr[i][1] = int(arr[i][1]) => 튜플은 불변이기 때문에 이와같이 수정 불가

def setting(data):
    return int(data[1])

# sorted(arr, key) : key 함수가 만든 값 기준으로 오름차순 정렬 => 여기선 key 함수가 만든 값인 int(data[1]) 기준으로 오름차순 정렬
arr = sorted(arr, key = setting)
for i in arr:
    print(i[0], end = " ")


# [내가 3번째로 푼 풀이]
n = int(input())

arr = []
for i in range(n):
    a, b = input().split()
    b = int(b)
    arr.append((a, b))

def setting(data):
    return data[1]

arr.sort(key = setting)
for i in range(n):
    print(arr[i][0], end = " ")