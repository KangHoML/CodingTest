import sys
from collections import deque

sys.stdin = open("13460.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, dir):
    cnt = 0
    
    while board[x + dx[dir]][y + dy[dir]] != '#' and board[x][y] != 'O':
        x, y = x + dx[dir], y + dy[dir]
        cnt += 1
    
    return x, y, cnt

def bfs(rx, ry, bx, by):
    queue = deque([(1, rx, ry, bx, by)])
    visited = [(rx, ry, bx, by)]

    while(queue):
        cnt, rx, ry, bx, by = queue.popleft()

        # 종료 조건
        if cnt > 10: break
        
        for dir in range(4):
            nrx, nry, rcnt = move(rx, ry, dir)
            nbx, nby, bcnt = move(bx, by, dir)

            # 파란색이 빠지면 실패
            if board[nbx][nby] == 'O': continue
            
            # 빨간색만 빠지면 성공
            if board[nrx][nry] == 'O':
                return cnt
            
            # 둘이 겹친 경우 처리
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx, nry = nrx - dx[dir], nry - dy[dir]
                else:
                    nbx, nby = nbx - dx[dir], nby - dy[dir]

            # 방문 확인 후 queue에 추가
            if (nrx, nry, nbx, nby) not in visited:
                visited.append((nrx, nry, nbx, nby))
                queue.append((cnt + 1, nrx, nry, nbx, nby))
    
    return -1
            

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R': rx, ry = i, j
            elif board[i][j] == 'B': bx, by = i, j

    print(f"#{t}: {bfs(rx, ry, bx, by)}")