score = {
    "A+":4.5,
    "A0":4.0,
    "B+":3.5,
    "B0":3.0,
    "C+":2.5,
    "C0":2.0,
    "D+":1.5,
    "D0":1.0,
    "F":0.0
}

sum = 0.0
score_sum = 0.0
for i in range(20):
    a, b, c = input().split()  # b에서 3.0으로 입력 받아서 input().split()으로 받는 순간 전부 문자열로 인식되기 때문에 float(b) 처럼 숫자로 변환해줘야 한다.

    if c == "P":
        pass
    else:
        sum += (float(b) * score[c])
        score_sum += float(b)
print(sum/score_sum)