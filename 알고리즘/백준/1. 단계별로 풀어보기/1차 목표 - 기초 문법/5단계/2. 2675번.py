a = int(input())
arr = []
char = ''

for i in range(a):
    b, c = input().split()

    for j in range(len(c)):
        char += c[j]*int(b)
    
    arr.append(char)
    char = ''

for i in range(len(arr)):
    print(arr[i])