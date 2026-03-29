a = list(input().split())
b = []

for i in range(len(a)):
    b.append(int(a[i][::-1]))  # [::-1] : 처음부터 끝까지 -1 스텝으로 가져오라는 뜻 => 문자열(또는 리스트)을 거꾸로 뒤집을 때 많이 씀
    
print(max(b))