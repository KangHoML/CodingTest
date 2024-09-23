import sys
from collections import deque
sys.stdin = open("14502.txt", "r")

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(board):
    cnt = 0
    copied_board = [r[:] for r in board]

    queue = deque([])
    for v in virus:
        queue.append(v)

    while(queue):
        x, y = queue.popleft()

        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]

            # 범위 체크
            if not (0 <= nx < n and 0 <= ny < m): continue

            # 벽인 경우
            if copied_board[nx][ny] != 0: continue

            copied_board[nx][ny] = 2
            queue.append((nx, ny))

    # 안전구역 계산
    for r in range(n):
        for c in range(m):
            if copied_board[r][c] == 0: cnt += 1
    
    return cnt
    
def combination(arr, k):
    result = []
    if k == 0: return [[]]

    for i, num in enumerate(arr):
        for j in combination(arr[i+1:], k-1):
            result.append([num] + j)
    
    return result

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    virus, wall = [], []
    for x in range(n):
        for y in range(m):
            if board[x][y] == 0: wall.append((x, y))
            elif board[x][y] == 2: virus.append((x, y))

    ans = 0
    for c in combination(wall, 3):
        # 벽 세우기
        for x, y in c:
            board[x][y] = 1
        
        # 안전구역 계산
        ans = max(ans, bfs(board))
        
        # 벽 지우기
        for x, y in c:
            board[x][y] = 0

    print(f"#{t}: {ans}")