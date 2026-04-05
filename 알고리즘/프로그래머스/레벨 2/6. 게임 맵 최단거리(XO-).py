# [문제 푼 날짜]
# 1. 3월 25일 (X) 43분 13초 => 거의 맞았는데 if maps[nx][ny] == 0 이 조건문을 
#                              if nx < 0 or nx >= n or ny < 0 or ny >= m 이 조건문 보다 먼저 써서 인덱스 에러가 났다.
# 2. 4월 5일 (O) 33분 11초 OK => 2차원 리스트 생성과정에서 초반에 save = [0 * m for _ in range(n)] 이렇게 해버림
# 3. 4월 12일 ()


from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    save = [[0] * m for _ in range(n)]
    save[0][0] = 1

    # 동 / 서 / 남 /북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        while queue:
            x, y = queue.popleft()
 
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[nx][ny] == 0:
                    continue
                if save[nx][ny] > 0:
                    continue
                    
                queue.append((nx, ny))
                save[nx][ny] = save[x][y] + 1
        
        if save[n - 1][m - 1] > 0:
            return save[n - 1][m - 1]
        else:
            return -1
    
    return bfs(0, 0)