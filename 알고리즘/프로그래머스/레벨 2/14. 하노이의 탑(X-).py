# [핵심 아이디어]
# 여기서 answer = [[1,2], [1,3], [2,3]] 다음의 뜻이다.
# [1,2] : 1번 기둥에서 2번 기둥으로 옮김
# [1,3] : 1번 기둥에서 3번 기둥으로 옮김
# [2,3] : 2번 기둥에서 3번 기둥으로 옮김
# 또한 이 코드는 그냥 외우자


# [문제 푼 날짜]
# 1. 4월 11일 (X)
# 2. 4월 25일 ()


def solution(n):
    answer = []

    # num: 옮겨야 할 원반 개수
    # start: 출발 기둥
    # mid: 보조 기둥
    # end: 도착 기둥
    # => 원반 num개를 start에서 end로 옮겨라. 이때 mid를 중간 보조로 사용한다.
    def hanoi(num, start, mid, end):

        # 원반이 1개면 고민할거 없이 출발 기둥에서 도착 기둥으로 옮기면 된다.
        if num == 1:
            answer.append([start, end])
            return

        # 1단계: 맨 아래 가장 큰 원반을 제외한 그 위에 있는 num-1개의 작은 원반들을 start에서 mid로 옮긴다. 이때 end를 보조로 사용한다.
        hanoi(num - 1, start, end, mid)

        # 2단계: 이제 가장 큰 원반 1개를 start에서 end로 옮긴다.
        answer.append([start, end])

        # 3단계: 아까 mid에 임시로 옮겨둔 num-1개의 작은 원반들을 mid에서 end로 옮긴다. 이때 start를 보조로 사용한다.
        hanoi(num - 1, mid, start, end)

    hanoi(n, 1, 2, 3)
    return answer