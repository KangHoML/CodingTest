import sys
sys.stdin = open("15683.txt", "r")

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cctv_dir = [[0], [0, 2], [0, 3], [0, 2, 3], [0, 1, 2, 3]]

def count_edge(tlst):
    visited = [[0] * m for _ in range(n)] # 방문 배열
    
    for i, rot in enumerate(tlst):
        x, y = cctv_pos[i]      # 위치
        num = board[x][y] - 1   # 타입
        
        for d in cctv_dir[num]:
            dir = (d + rot) % 4 # 현재 방향
            
            nx, ny = x + dx[dir], y + dy[dir]
            while(0 <= nx < n and 0 <= ny < m):
                if board[nx][ny] == 6: break
                visited[nx][ny] = 1
                nx, ny = nx + dx[dir], ny + dy[dir]
    
    edge = 0
    for r in range(n):
        for c in range(m):
            if board[r][c] == 0 and visited[r][c] == 0: edge += 1

    return edge


def dfs(cnt, tlst):
    global ans

    # 종료 조건
    if cnt == len(cctv_pos):
        ans = min(ans, count_edge(tlst)) # 최솟값 갱신
        return

    # 회전
    dfs(cnt + 1, tlst + [0]) # 0도
    dfs(cnt + 1, tlst + [1]) # 90도
    dfs(cnt + 1, tlst + [2]) # 180도
    dfs(cnt + 1, tlst + [3]) # 270도

for t in range(1, int(input()) + 1):
    # 입력
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    # 카메라 위치
    cctv_pos = []
    for x in range(n):
        for y in range(m):
            if 1 <= board[x][y] <= 5: cctv_pos.append((x, y))
    
    ans = 64
    dfs(0, []) # 횟수, 각 cctv의 방향
    
    print(f"{t}: {ans}")