# [핵심 아이디어]
# 1. 앞 뒤 문자가 그대로면 통과
# 2. 문자가 바뀌는 순간에는, 그 문자가 뒤쪽에 다시 나오면 그룹 단어가 아니다.


# [문제 푼 날짜]
# 1. 12월 17일 (X) 접근 실패(아이디어 X)
# 2. 12월 19일 (O) 6분 50초 OK
# 3. 12월 21일 (O) 11분 50초 SLOW(>10) => cnt -= 1 누락으로 디버깅 지연
# 4. 12월 28일 (O) 5분 42초 OK


n = int(input())

cnt = 0
for i in range(n):
    a = input()
    for j in range(len(a)-1):
        if a[j] == a[j+1]:
            pass                    # 여기서는 pass 대신 continue를 써도 된다.
        else:
            if a[j] in a[j+1:]:
                cnt -= 1
                break
    cnt += 1

print(cnt)