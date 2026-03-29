# [핵심 아이디어]
# 0. 이런 문제는 잘 이해가 안되면 한번 적어보자
# 1. 두 수 중에서 하나라도 1 이하인 경우에는 더하고 두 수가 모두 2 이상일 때 곱한다.
# 2. 여기서 두 수 중 하나는 result이고, 하나는 다음에 더하거나 곱할 숫자인 num 이다.
# 3. 즉 result와 다음에 올 숫자 num, 이 두 개의 숫자 중 하나라도 2보다 작으면 더하고 두 숫자 모두 1보다 크면 곱해야 최대값이 나온다.
# 4. 예를들어 01908 이라는 숫자가 있다면 
# result = 0
# 0+1                       => result = result(0) + 1  => result와 1은 둘다 2보다 작으므로 더함
# (0+1) + 9                 => result = result(1) + 9  => 9는 1보다 크지만 result는 2보다 작으므로 더함
# ((0+1) + 9) + 0           => result = result(10) + 0 => result는 1보다 크지만 0은 2보다 작으므로 더함
# (((0+1) + 9) + 0) * 8     => result = result(10) * 8 => result와 8은 모두 2보다 크므로 곱함. 따라서 result = 80


# [시간 복잡도 계산]
# 1. s = list(map(int, input()))
# O(n)

# 2. for문
# O(n)

# 3. 총합
# O(n)


# [이 문제가 그리디인 이유]
# 각 단계에서 0이나 1이 끼면 *보다 +가 항상 결과를 더 크게(또는 같게) 만들고, 
# 둘 다 2 이상이면 *가 항상 더 크므로 매 순간의 최적 선택이 전체 최적이어서 그리디다.


# [문제 푼 날짜]
# 1. 1월 3일 (x) => 핵심 아이디어는 생각했으나 구현을 못함
# 2. 1월 4일 (O) 4분 42초 OK
# 3. 1월 11일 (O) 3분 45초 OK
# 4. 2월 27일 (X) 10분 50초 => else 문에서 elif result == 1 이 부분 빼먹음 -> 그냥 정석 풀이로 익히자


s = list(map(int, input()))
result = s[0]

for i in range(1, len(s)):
    if s[i] < 2 or result < 2:
        result += s[i]
    else:
        result *= s[i]

print(result)


# [4번째로 푼 풀이]
s = input()

result = int(s[0])
for i in range(1, len(s)):
    if s[i] == '0':
        result += int(s[i])
    elif s[i] == '1':
        result += int(s[i])
    else:
        if result == 0:
            result += int(s[i])
        elif result == 1:
            result += int(s[i])
        else:
            result = result * int(s[i])
        
print(result)