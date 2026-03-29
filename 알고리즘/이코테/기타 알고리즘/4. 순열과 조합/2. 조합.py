# [조합]
# 조합(Combination) 이란 "서로 다른 n개"에서 r개를 선택하되, 순서를 고려하지 않는 것이다.
# nCr의 형태로 표현하며 공식은 n! / (r! x (n - r)!) 이다.

# 예를들어 A, B, C 총 3개의 원소가 있고 이 중에서 2개를 선택한다면
# AB
# AC
# BC
# 이와 같이 총 3! / (2! x (3 - 2)!) = 3개의 경우가 나온다.


# [중복 조합]
# 중복 조합이란 "서로 다른 n개"에서 r개를 선택하되, 중복을 허용하고 순서는 고려하지 않는 것이다.
# 공식은 nHr = (n+r-1)Cr 이다.

# 예를들어 A, B, C 총 3개의 원소가 있고 이 중에서 2개를 선택하는데, 중복을 허용해서 뽑는다면
# AA
# AB
# AC
# BB
# BC
# CC
# 이와 같이 총 3H2 = 4C2 = 4! / (2! x (2!)) = 6개의 경우가 나온다.


# [조합/중복조합 코드]
import itertools

data = [1, 2, 3]

# 1. 조합
# 다음은 1부터 3까지의 수 중에서 2개를 뽑는 모든 조합을 구하는 코드이다.
for i in itertools.combinations(data, 2):
    print(list(i), end = ' ')

print()

# 2. 중복조합
# 다음은 1부터 3까지의 수 중에서 2개를 뽑되, 중복을 허용하는 모든 조합을 구하는 코드이다.
# 중복조합은 combinations()가 아닌, combinations_with_replacement()를 사용한다.
for i in itertools.combinations_with_replacement(data, 2):
    print(list(i), end = ' ')