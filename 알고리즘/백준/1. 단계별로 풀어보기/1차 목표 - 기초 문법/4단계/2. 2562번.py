a = list()

for i in range(9):
    b = int(input())
    a.append(b)

max = 0
num = 0
for i in range(9):
    if a[i] > max:
        max = a[i]  
        num = i+1

print(max)
print(num)