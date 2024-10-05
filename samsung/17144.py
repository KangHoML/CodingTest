import sys
sys.stdin = open("17144.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for TC in range(1, int(input()) + 1):
    R, C, T = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]

    # 청정기 위치
    for x in range(R):
        if board[x][0] == -1:
            cux, cdx = x, x + 1
            board[x][0], board[x+1][0] = 0, 0
            break
    
    for _ in range(T):
        new_board = [r[:] for r in board]

        # 1. 확산
        for x in range(R):
            for y in range(C):
                if board[x][y] < 5: continue
                v = board[x][y] // 5

                for dir in range(4):
                    nx, ny = x + dx[dir], y + dy[dir]

                    if not (0 <= nx < R and 0 <= ny < C): continue
                    if (nx, ny) == (cux, 0) or (nx, ny) == (cdx, 0): continue

                    new_board[nx][ny] += v
                    new_board[x][y] -= v
        
        board = new_board

        # 2. 시계방향
        for r in range(cux-1, 0, -1):
            board[r][0] = board[r-1][0]
        for c in range(0, C-1, 1):
            board[0][c] = board[0][c+1]
        for r in range(0, cux, 1):
            board[r][C-1] = board[r+1][C-1]
        for c in range(C-1, 0, -1):
            board[cux][c] = board[cux][c-1]

        # 3. 반시계방향
        for r in range(cdx+1, R-1, 1):
            board[r][0] = board[r+1][0]
        for c in range(0, C-1, 1):
            board[R-1][c] = board[R-1][c+1]
        for r in range(R-1, cdx, -1):
            board[r][C-1] = board[r-1][C-1]
        for c in range(C-1, 0, -1):
            board[cdx][c] = board[cdx][c-1]
    
    ans = 0
    for i in range(R):
        for j in range(C):
            ans += board[i][j]
    
    # ans = sum(map(sum, board))
    print(f"{TC}: {ans}")