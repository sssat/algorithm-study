# [핵심 아이디어]
# 예를들어 옷이 다음과 같이 있다면
# clothes = [
#     ["yellow_hat", "headgear"],
#     ["blue_sunglasses", "eyewear"],
#     ["green_turban", "headgear"]
# ]

# 종류별 개수는
# headgear: 2개
# eyewear: 1개

# 각 종류마다 선택지는 다음과 같다.
# headgear: yellow_hat / green_turban / 안 입기 -> 3가지
# eyewear: blue_sunglasses / 안 쓰기 -> 2가지

# 그래서 전체 조합 수는 3 * 2 = 6개
# 그런데 문제에서 아무것도 안 입는 경우는 제외해야 하니까 6 - 1 = 5개


# [문제 푼 날짜]
# 1. 5월 9일 (X) 
# 2. 5월 10일 ()


def solution(clothes):
    answer = 1
    clothes_dict = {}

    for name, kind in clothes:
        if kind not in clothes_dict:
            clothes_dict[kind] = 0
        clothes_dict[kind] += 1

    for count in clothes_dict.values():
        answer *= (count + 1)

    return answer - 1