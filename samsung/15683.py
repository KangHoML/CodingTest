import sys
sys.stdin = open("15683.txt", "r")

# 방향 (동쪽부터 시계방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 각 카메라 방향
cam_dir = [
    [[0], [1], [2], [3]], # 1
    [[0, 2], [1, 3]], # 2
    [[0, 3], [0, 1], [1, 2], [2, 3]], # 3
    [[0, 2, 3], [0, 1, 3], [0, 1, 2], [1, 2, 3]], # 4
    [[0, 1, 2, 3]] # 5
]

def count_edge(lst):
    # cctv 감시 구역 찾기
    cctv_lst = []
    for idx, (num, x, y) in enumerate(cam_pos):
        for dir in cam_dir[num][lst[idx] % len(cam_dir[num])]:
            nx, ny = x + dx[dir], y + dy[dir]

            while(0 <= nx < n and 0 <= ny < m):
                if board[nx][ny] == 6: break
                elif board[nx][ny] == 0: cctv_lst.append((nx, ny))
                nx, ny = nx + dx[dir], ny + dy[dir]
    
    # 사각지대 찾아서 반환
    edge = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0 and (i, j) not in cctv_lst: edge += 1
    
    return edge

def dfs(cnt, tlst):
    global ans

    # 종료 조건
    if cnt == len(tlst):
        ans = min(ans, count_edge(tlst))
        return
    
    for c in range(4):
        tlst[cnt] = c
        dfs(cnt+1, tlst)

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    # (카메라 번호, x, y) 순서로 저장
    cam_pos = []
    for r in range(n):
        for c in range(m):
            for k in range(1, 6):
                if board[r][c] == k: cam_pos.append((k-1, r, c))
    
    ans = 64
    dfs(0, [0] * len(cam_pos))

    print(f"{t}: {ans}")
