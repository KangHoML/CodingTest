import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [input().strip() for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
        elif graph[i][j] == 'B':
            bx, by = i, j
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = []


# 구슬이 벽에 막히거나 구멍인 경우까지 이동
def move(x, y, i):
    cnt = 0
    while graph[x + dx[i]][y + dy[i]] != '#' and graph[x][y] != 'O':
        x += dx[i]
        y += dy[i]
        cnt += 1

    return x, y, cnt 

def bfs(rx, ry, bx, by):
    queue = deque([(rx, ry, bx, by, 1)])
    visited.append((rx, ry, bx, by))

    while(queue):
        # 현재 위치
        rx, ry, bx, by, cnt = queue.popleft()

        if cnt > 10:
            break

        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, i)
            nbx, nby, bcnt = move(bx, by, i)
            
            # 파란 구슬이 구멍에 들어가지 않은 경우
            if graph[nbx][nby] != 'O': 
                # 빨간 구슬이 들어간 경우 성공
                if graph[nrx][nry] == 'O': 
                    print(cnt)
                    return
                
                # 둘이 겹친 경우, 더 많이 이동한 것 한 칸 뒤로
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
            
                # 만약 방문하지 않았다면 방문 처리
                if (nrx, nry, nbx, nby) not in visited:
                    visited.append((nrx, nry, nbx, nby))
                    queue.append((nrx, nry, nbx, nby, cnt+1))
                    
    print(-1)

bfs(rx, ry, bx, by)
    