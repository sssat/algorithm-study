# [문제 푼 날짜]
# 1. 3월 23일 (X) => 자음 및 모음 개수를 카운트하는 로직을 빼먹어서 틀림
# 2. 3월 30일 ()


"""
입력 케이스
4 6
a t c i s w
"""

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
    for j in i:
        if j in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    # 모음이 1개 이상 이고 자음이 2개 이상이라면 출력
    if vowel_count >= 1 and consonant_count >= 2:
        print(''.join(i))