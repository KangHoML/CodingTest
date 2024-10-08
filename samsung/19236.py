import sys
sys.stdin = open("19236.txt", "r")

# 방향 (반시계)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def dfs(sx, sy, sd, sm, arr, flst):
    global ans

    # 현재 위치에서 물고기 이동
    for fn in range(1, 17):
        # 현재 물고기의 정보
        fd, fx, fy = flst[fn]

        # 현재 물고기가 이미 먹힌 후인 경우
        if fx == -1 and fy == -1:
            continue

        flag = 0
        for d in range(8):
            nd = (fd + d) % 8
            nfx, nfy = fx + dx[nd], fy + dy[nd]

            # 가능한 경우
            if (0 <= nfx < 4 and 0 <= nfy < 4 and not (nfx == sx and nfy == sy)):
                flag = 1
                break

        # 이동 못한 경우 다음
        if flag == 0: continue

        # 이동한 경우 반영
        flst[fn] = [nd, nfx, nfy]
        nfn = arr[nfx][nfy]
        arr[fx][fy], arr[nfx][nfy] = nfn, fn

        # 빈칸이 아닌 경우
        if nfn != 0:
            flst[nfn][1], flst[nfn][2] = fx, fy

    # 상어가 갈 수 있는 곳 탐색
    nsx, nsy = sx, sy

    for _ in range(3):
        nsx, nsy = nsx + dx[sd], nsy + dy[sd]

        if not (0 <= nsx < 4 and 0 <= nsy < 4 and arr[nsx][nsy] != 0): continue

        # 갈 수 있는 경우
        nfn, nsd = arr[nsx][nsy], flst[arr[nsx][nsy]][0]

        arr[nsx][nsy] = 0
        flst[nfn][1], flst[nfn][2] = -1, -1

        # 복사해서 넘기기
        new_arr = [r[:] for r in arr]
        nflst = [r[:] for r in flst]

        dfs(nsx, nsy, nsd, sm + nfn, new_arr, nflst)

        # 백트래킹
        arr[nsx][nsy] = nfn
        flst[nfn][1], flst[nfn][2] = nsx, nsy

    ans = max(ans, sm)

for TC in range(1, int(input()) + 1):
    board = [[0] * 4 for _ in range(4)]
    flst = [[] for _ in range(17)]  # 방향, x, y

    for i in range(4):
        lst = list(map(int, input().split()))
        for j in range(4):
            flst[lst[j * 2]] = [lst[j * 2 + 1] - 1, i, j]  # 방향, x, y
            board[i][j] = lst[j * 2]  # 물고기 번호 기록

    # 초기 상어 정보
    sx, sy = 0, 0
    sm, sd = board[sx][sy], flst[board[sx][sy]][0]

    flst[board[sx][sy]][1], flst[board[sx][sy]][2] = -1, -1
    board[sx][sy] = 0

    # 탐색
    ans = 0
    dfs(sx, sy, sd, sm, board, flst)

    print(f"#{TC}: {ans}")