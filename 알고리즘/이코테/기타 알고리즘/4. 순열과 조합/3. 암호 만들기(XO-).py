# [문제 푼 날짜]
# 1. 3월 23일 (X) => 자음 및 모음 개수를 카운트하는 로직을 빼먹어서 틀림
# 2. 3월 30일 (O) 17분 44초 OK => 정석 풀이로 풀자. 또한 print(''.join(i)) 이 함수 잘 기억해두자
# 3. 4월 6일 ()


"""
입력 케이스
4 6
a t c i s w
"""


# [정석 풀이]
import itertools

l, c = map(int, input().split())
s = input().split()
s.sort()

# 모음 리스트
vowels = ['a', 'e', 'i', 'o', 'u']

for i in itertools.combinations(s, l):
    
    # 모음/자음의 개수를 담을 변수
    vowel_count = 0
    consonant_count = 0

    # 자음 및 모음 개수 카운트
    # i = ('a', 'c', 'i', 's') => 이런식으로 튜플에 담긴다
    for j in i:
        if j in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    # 모음이 1개 이상 이고 자음이 2개 이상이라면 출력
    if vowel_count >= 1 and consonant_count >= 2:
        print(''.join(i))


# [내가 2번째로 푼 풀이]
import itertools 

l, c = map(int, input().split())
s = input().split()
s.sort()

vowel = ['a', 'i', 'u', 'e', 'o']

result = []
for i in itertools.combinations(s, l):
    result.append(list(i))

for i in range(len(result)):
    count1 = 0
    count2 = 0
    for j in range(l):
        if result[i][j] in vowel:
            count1 += 1
        else:
            count2 += 1
        
    if count1 > 0 and count2 > 1:
        for k in range(l):
            print(result[i][k], end = "")
        print()