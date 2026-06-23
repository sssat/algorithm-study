# [핵심 아이디어]
# result에는 1행 1열 -> 1행 2열 -> 1행 3열 -> 2행 1열 -> 2행 2열 -> 2행 3열 -> 3행 1열 -> ... 순서로 값이 채워진다.
# 즉, 결과 행들을 왼쪽에서 오른쪽 으로 한 행씩 채우고 밑에 행으로 내려가서 반복한다.


# [문제 푼 날짜]
# 1. 5월 1일 (X)
# 2. 5월 2일 (X)
# 3. 5월 9일 ()


def solution(arr1, arr2):
    result = []

    for i in range(len(arr1)):
        row = []

        for j in range(len(arr2[0])):
            total = 0

            for k in range(len(arr2)):
                total += arr1[i][k] * arr2[k][j]

            row.append(total)

        result.append(row)

    return result