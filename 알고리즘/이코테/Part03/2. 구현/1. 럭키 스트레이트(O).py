# [문제 푼 날짜]
# 1. 1월 12일 (O) 4분 59초 OK


n = input()

left = 0
right = 0
for i in range(int(len(n)//2)):
    left += int(n[i])
    right += int(n[-(i+1)])

if left == right:
    print("LUCKY")
else:
    print("READY")