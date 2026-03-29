a, b = map(int, input().split())
c = int(input())

d = (b + c)//60
e = (b+c)%60

if d == 0:
    b = b + c
    print(a, b)

elif a+d <= 23:
    a = a + d
    b = e
    print(a, b)

elif a+d > 23:
    a = (a+d)-24
    b = e
    print(a, b)