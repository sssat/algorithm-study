# [스택 자료구조]
# 선입후출 구조
# 파이썬에서 스택을 이용할 때는 별도의 라이브러리를 사용할 필요가 없다.
# 기본 리스트의 append()와 pop() 메서드를 이용하면 된다.


stack = []

# stack = [5, 2, 3, 7]
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)

# stack = [5, 2, 3]
stack.pop()

# stack = [5, 2, 3, 1, 4]
stack.append(1)
stack.append(4)

# stack = [5, 2, 3, 1]
stack.pop()

# 결과 출력
print(stack)