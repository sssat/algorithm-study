# [문제 푼 날짜]
# 1. 1월 12일 (X) 31분 16초 SLOW(>20) => 문자만 입력되거나 숫자만 입력되는 케이스를 제외하면 구현 자체는 맞게 함
# 2. 1월 13일 (O) 5분 0초 => 다른건 다 맞게 구현했지만 문자만 입력되는 케이스에서 틀림
# 3. 1월 20일 (O) 7분 31초 OK


# [정석 풀이]
s = input()
arr = []
num = 0

for i in s:
    if i.isalpha():
        arr.append(i)
    else:
        num += int(i)

arr.sort()                  # ord()로 알파벳을 숫자로 변환안해도 알파벳이면 sort 가능하다.

# 만약 입력에 숫자가 없어서 num이 0이라면 예를들어 ABC만 입려했을때 ABC0이 출력된다.
if num != 0:
    arr.append(str(num))    # 현재 arr 배열은 str인 원소들로 구성되어 있으므로 숫자인 num를 arr 배열에 넣으려면 str로 변환해야한다.

print(''.join(arr))         # 또한 join을 쓰려면 원소가 전부 문자열이어야 해서 num를 str로 변환하는 부분도 있다


# [내가 푼 풀이]
# 1. 숫자만 있는 입력(예: "123")에서 pop으로 리스트가 비면 s[i] 접근으로 IndexError 발생
# 2. 또한 알파벳만 있는 입력(예: "ABC")에서 "ABC0"을 출력해 정답 형식과 다를 수 있음
s = list(input())

for i in range(len(s)):
    if s[i] > '9':
        s[i] = ord(s[i])
    else:
        s[i] = int(s[i])

s.sort()
num = 0
i = 0
while True:
    if s[i] > 9:
        break
    else:
        num += s[i]
        s.pop(i)
        i -= 1
    i += 1

for i in range(len(s)):
    s[i] = chr(s[i])
    print(s[i], end = "")
print(num)