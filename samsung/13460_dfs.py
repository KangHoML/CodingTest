import sys
sys.stdin = open("13460.txt", "r")

# 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 이동처리
def move(x, y, dir):
    cnt = 0
    
    # 다음 칸이 벽이거나, 현재 칸이 구멍이 아닐때까지
    while board[x + dx[dir]][y + dy[dir]] != '#' and board[x][y] != 'O': 
        x, y = x + dx[dir], y + dy[dir]
        cnt += 1
    
    return x, y, cnt

# dfs + 백트래킹
def dfs(cnt, rx, ry, bx, by):
    # 최종 정답
    global ans

    # 방문 체크
    if (cnt, rx, ry, bx, by) in visited: return
    visited.append((cnt, rx, ry, bx, by))
    
    # 시도 횟수 초과 시 종료
    if cnt > 10: return

    # 4 방향에 대해 모두 체크
    for dir in range(4):
        # 단순 이동 처리
        nrx, nry, r_cnt = move(rx, ry, dir)
        nbx, nby, b_cnt = move(bx, by, dir)
                    
        # 이동을 안한 경우
        if r_cnt == 0 and b_cnt == 0: continue
        
        # 성공, 실패 체크 (둘 다 동시에 빠진 경우 존재할 수 있으므로 먼저 체크)
        if board[nbx][nby] == 'O': continue
        else:
            if board[nrx][nry] == 'O':
                ans = min(ans, cnt)
                return
            
        # 두 위치가 동일한 경우
        if nrx == nbx and nry == nby:
            if r_cnt > b_cnt: nrx, nry = nrx - dx[dir], nry - dy[dir]
            else: nbx, nby = nbx - dx[dir], nby - dy[dir]
        
        # 백트래킹
        board[rx][ry], board[bx][by] = '.', '.'
        board[nrx][nry], board[nbx][nby] = 'R', 'B'
        
        dfs(cnt + 1, nrx, nry, nbx, nby)

        board[nrx][nry], board[nbx][nby] = '.', '.'
        board[rx][ry], board[bx][by] = 'R', 'B'

T = int(input())
for t in range(1, T + 1):
    # 초기화
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R': rx, ry = i, j
            elif board[i][j] == 'B': bx, by = i, j
    
    # visited를 통해 체크
    visited = []

    # 실행
    ans = 11
    dfs(1, rx, ry, bx, by)
    print(f"#{t} {ans if ans != 11 else -1}")