import sys
from collections import deque
sys.stdin = open("17142.txt", "r")

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(tlst):
    visited = [[-1] * N for _ in range(N)]
    ecnt = ECNT

    queue = deque([])
    for x, y in tlst:
        queue.append((x, y))
        visited[x][y] = 0
    
    while(queue):
        # 빈칸이 없는 경우 탐색 X 
        if ecnt == 0: break
        
        # 있는 경우 진행
        x, y = queue.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]

            if not (0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1 and board[nx][ny] != 1): continue
            if board[nx][ny] == 0: ecnt -= 1
            
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))
    
    if ecnt > 0: return -1
    else: return max(map(max, visited))

def dfs(cnt, s, tlst):
    global ans
    
    if cnt == M:
        time = bfs(tlst)
        if time != -1: ans = min(ans, time)
        return
    
    for j in range(s, len(vlst)):
        dfs(cnt + 1, j + 1, tlst + [vlst[j]])

for TC in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 바이러스 위치 및 빈칸 개수 찾기
    vlst = []
    ECNT = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0: ECNT += 1
            if board[r][c] == 2: vlst.append((r, c))

    # 완전 탐색
    ans = 10000
    dfs(0, 0, [])

    ans = ans if ans != 10000 else -1
    print(f"{TC}: {ans}")