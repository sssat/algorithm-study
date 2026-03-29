x = int(input())
y = int(input())
c = 0

for i in range(y):
    a, b = map(int, input().split())
    
    c = c + a*b

if c == x:
    print("Yes")
else:
    print("No")