# [문제 푼 날짜]
# 1. 12월 29일 (O) 9분 54초 OK => 처음에 문제를 잘못 해석해서 좀 헤매서 문제가 뭔지만 GPT한테 물어봄


x, y, w, h = map(int, input().split())

arr = []

right = w - x
arr.append(right)

left = x
arr.append(left)

top = h - y
arr.append(top)

bottom = y
arr.append(bottom)

print(min(arr))