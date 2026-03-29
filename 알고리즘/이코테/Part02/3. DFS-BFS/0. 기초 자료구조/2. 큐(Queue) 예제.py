# [큐 자료구조]
# 선입선출 구조 => 공정한 자료구조
# append() 와 popleft() 메서드를 사용한다.


# collections 모듈에서 제공하는 deque 자료구조
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# queue = deque([5, 2, 3, 7])
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)

# queue = deque([2, 3, 7])
queue.popleft() # 5 삭제

# queue = deque([2, 3, 7, 1, 4])
queue.append(1)
queue.append(4)

# queue = deque([3, 7, 1, 4])
queue.popleft() # 2 삭제

# 결과 출력
print(queue)

# deque 객체를 list 자료형으로 변환
print(list(queue))