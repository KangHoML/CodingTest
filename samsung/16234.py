import sys
from collections import deque
sys.stdin = open("16234.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    tlst = []
    
    while(queue):
        nx, ny = queue.popleft()
        if visited[nx][ny] == 1: continue
        else: visited[nx][ny] = 1

        for dir in range(4):
            nnx, nny = nx + dx[dir], ny + dy[dir]
            
            # 범위 체크
            if not (0 <= nnx < N and 0 <= nny < N and visited[nnx][nny] == 0): continue

            # 조건 체크
            if L <= abs(board[nnx][nny] - board[nx][ny]) <= R:
                queue.append((nnx, nny))
                if (nx, ny) not in tlst: tlst.append((nx, ny))
                if (nnx, nny) not in tlst: tlst.append((nnx, nny))

    return tlst
    

for T in range(1, int(input()) + 1):
    N, L, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    cnt = 0
    while True:
        visited = [[0] * N for _ in range(N)]
        union = []

        for x in range(N):
            for y in range(N):
                if visited[x][y] == 0:
                    u = bfs(x, y)
                    if len(u) != 0: union.append(u)

        # 연합이 없으면 끝
        if len(union) == 0: break
        else: cnt += 1

        # 연합 평균
        for u in union:
            avg = 0
            for r, c in u:
                avg += board[r][c]
            avg = avg // len(u)

            for r, c in u:
                board[r][c] = avg
        

    print(f"#{T}: {cnt}")