# [문제 푼 날짜]
# 1. 3월 25일 (X) 43분 13초 => 거의 맞았는데 if maps[nx][ny] == 0 이 조건문을 
#                              if nx < 0 or nx >= n or ny < 0 or ny >= m 이 조건문 보다 먼저 써서 인덱스 에러가 났다.
# 2. 4월 1일 ()


from collections import deque

def solution(maps):
    answer = 0
    
    # 각각 2차원 배열의 행과 열 길이
    n = len(maps)
    m = len(maps[0])
    
    save = [[0] * m for _ in range(n)]
    save[0][0] = 1

    # 동 / 서 / 남 / 북
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
        
        return save[n - 1][m - 1]
    
    answer = bfs(0, 0)
    if answer != 0:
        return answer
    else:
        return -1