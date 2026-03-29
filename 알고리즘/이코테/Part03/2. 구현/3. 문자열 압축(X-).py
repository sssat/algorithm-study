# [핵심 아이디어]
# 문자열의 길이가 1000 이하로 작기 때문에 가능한 모든 경우의 수를 탐색하는 완전 탐색을 수행할 수 있다.
# 문자열을 1개 단위, 2개 단위, 3개 단위, ... n/2 개 단위의 모든 경우의 수를 탐색하면 된다.


# [문제 푼 날짜]
# 1. 3월 1일 (X)


"""
입력 케이스 1
aabbaccc

입력 케이스 2
ababcdcdababcdcd

입력 케이스 3
abcabcabcabcdededededede
"""

s = input()

def solution(s):
    answer = len(s)

    # 1개 단위(step)부터 압축 단위를 늘려가며 확인        
    for step in range(1, len(s) // 2 + 1):

        # 압축 결과를 누적해서 저장하는 문자열
        # 예를들어 "aabbaccc"를 step=1로 압축하면 최종적으로 "2a2ba3c" 같은 결과가 여기에 저장됨
        compressed = ""

        # 이전 조각 문자열 을 저장
        # 예를들어 step = 2, s = "ababcdcd" 이면 처음엔 prev = "ab" 가 저장됨
        prev = s[0 : step]

        # prev가 현재까지 몇 번 연속으로 나왔는지 저장하는 변수
        # 처음 prev를 하나 잡았으니까 시작값이 1
        # prev = "ab"로 시작했으면 일단 "ab"는 1번 나온 상태. 다음 조각도 "ab"면 count += 1 해서 2
        count = 1

        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        # 1번째: j = 1, 2, 3, ...
        # 2번째: j = 2, 4, 6, ...
        # 3번째: j = 3, 6, 9, ...
        for j in range(step, len(s), step):

            # 이전상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j : j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                if count >= 2:
                    compressed += str(count) + prev
                else:
                    compressed += prev

                prev = s[j : j + step]
                count = 1

        # 남아 있는 문자열에 대해서 처리
        if count >= 2:
            compressed += str(count) + prev
        else:
            compressed += prev

        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))

    return answer

print(solution(s))