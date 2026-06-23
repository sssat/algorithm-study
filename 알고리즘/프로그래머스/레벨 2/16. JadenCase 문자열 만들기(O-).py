# [핵심 아이디어]
# JadenCase 문제에서는 단어별 첫 글자만 대문자로 만들고 나머지는 소문자로 만든다.
# 단, 공백이 여러 개일 수 있으므로 일반 split()이 아니라 공백을 보존하는 방식인 split(' ')으로 처리해야 한다.


# [문제 푼 날짜]
# 1. 5월 2일 (O) 33분 20초 OK
# 2. 5월 16일 ()


# [정석 풀이]
# split(): 문자열을 기준에 따라 잘라서 리스트로 만들어주는 함수
# split 함수 안에 아무것도 안쓰면 기본적으로 공백류 문자를 기준으로 나눠서 리스트를 만든다.

# 또한 여기서 split()이 아닌 split(' ')으로 해줘야 한다.
# 만약 s = "hello  world" 와 같이 공백이 2개 이상 있을때 split()을 쓰면 ['hello', 'world'] 와 같이 공백 1개는 제외하고 저장되는데
# split(' ')을 쓰면 ['hello', '', 'world'] 와 같이 공백도 포함해서 저장되므로 split(' ')을 써줘야 한다.
def solution(s):
    answer = []

    for word in s.split(' '):
        new_word = ''

        for i in range(len(word)):
            if i == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()

        answer.append(new_word)

    return ' '.join(answer)


# [내가 1번째로 푼 풀이]
def solution(s):
    answer = ''
    
    words = []
    word = []
    for i in s:
        if i != ' ':
            word.append(i)
        else:
            words.append(word)
            word = []
    words.append(word)
    
    count = 0
    for i in words:
        for j in range(len(i)):
            if j == 0 and i[j].isalpha():
                words[count][j] = i[j].upper()
            elif j > 0 and i[j].isalpha():
                words[count][j] = i[j].lower()
                
        count += 1
    
    for i in range(len(words)):
        for j in range(len(words[i])):
            answer +=  words[i][j]
        
        if i < len(words) - 1:
            answer += ' '
    
    return answer