a = list(input())
b = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(b)):
    if b[i] in a:
        print(a.index(b[i]), end= " ")
    else:
        print(-1, end = " ")