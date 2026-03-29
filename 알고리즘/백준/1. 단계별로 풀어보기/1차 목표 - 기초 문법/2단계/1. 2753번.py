# 배수는 / 기호가 아니라 % 기호 사용

a = int(input())

if ((a % 4 == 0) and (a % 100 != 0)) or (a % 400 == 0):
    print(1)
else:
    print(0)