# [핵심 아이디어]
# 1. 입력받는 문자열을 대문자로 통일한다.
# 2. 입력 문자의 알파벳 A~Z의 개수를 담을 리스트를 만든다.
# 3. 아스키 코드 관련 지식 + ord() + chr() + count() + index() 함수 사용 


# [문제 푼 날짜]
# 1. 12월 16일 (X)
# 2. 12월 19일 (O) 7분 40초 OK
# 3. 12월 21일 (O) 9분 50초 OK
# 4. 12월 28일 (O) 8분 48초 OK


s = input().upper()   
cnt = [0] * 26  # 입력 문자의 알파벳 A~Z의 개수를 담을 리스트를 만듦

for i in s:
    
    # ord('M') - ord('A'): 알파벳에서 A를 0으로 봤을 때 M이 몇 번째인지 인덱스
    # 'M'은 12번째 인덱스 이므로 cnt[12] += 1
    # 따라서 입력 단어에서 'M'이 여러번 나오면 나온 횟수만큼 배열에 저장된다.
    cnt[ord(i) - ord('A')] += 1  # ord(): 문자 1개를 그 문자의 아스키코드 값으로 바꿔주는 함수. 그 반대는 chr() 함수.

max_cnt = max(cnt)

# max_cnt 값이 cnt 리스트에 몇 번 등장하는지 셈. 
# 만약 2번 이상이면 가장 많이 사용된 알파벳이 여러 개 존재하는 경우라는 소리이므로, ? 출력
if cnt.count(max_cnt) > 1:    
    print("?")

# 그게 아니라면 max_cnt가 cnt 리스트에서 몇 번째에 위치해있는지 반환한 다음 아스키 코드 표에서 + 65 후 알파벳으로 변환(chr)
else:
    print(chr(cnt.index(max_cnt) + ord('A')))

    
# 주석 없는 버전
s = input().upper()   
cnt = [0] * 26 

for i in s:
    cnt[ord(i) - ord('A')] += 1  

max_cnt = max(cnt)
if cnt.count(max_cnt) > 1:    
    print("?")
else:
    print(chr(cnt.index(max_cnt) + ord('A')))