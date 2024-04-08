import sys
from collections import deque
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 방향 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소했는가를 나타내기 위한 배열
visited = [[0] * m for _ in range(n)]


# 청소되지 않은 칸 확인
def check_clean(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < n and ny >= 0 and ny < m and visited[nx][ny] == 0 and graph[nx][ny] == 0:
            cnt += 1

    return cnt    

x, y = r, c
dir = d
while(1):
    # 현재 칸이 청소되지 않았다면 현재 칸 청소
    if visited[x][y] == 0:
        visited[x][y] = 1

    # 만약 청소되지 않은 칸 있다면
    if check_clean(x, y) != 0:
        # 반시계방향으로 회전
        dir = ((3 + dir) % 4)
            
        # 청소되지 않은 빈칸인 경우 1칸 전진
        if visited[x+dx[dir]][y+dy[dir]] == 0 and graph[x+dx[dir]][y+dy[dir]] == 0:
            x, y = x + dx[dir], y + dy[dir]

    # 만약 청소되지 않은 칸 없다면
    else:
        # 빈칸이면 1칸 후진
        if graph[x-dx[dir]][y-dy[dir]] == 0:
            x, y = x - dx[dir], y - dy[dir]
        
        # 벽이면 종료
        else:
            break

result = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            result +=1
print(result)