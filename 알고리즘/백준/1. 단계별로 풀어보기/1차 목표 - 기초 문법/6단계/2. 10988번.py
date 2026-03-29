a = input()

count = 0
for i in range(len(a)//2):
    if a[i] == a[len(a)-1-i]:
        continue
    else:
        count += 1
        break

if count == 0:
    print(1)
else:
    print(0)