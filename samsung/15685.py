import sys
sys.stdin = open("15685.txt", "r")

# 방향
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

for t in range(1, int(input()) + 1):
    N = int(input())
    lst = [tuple(map(int, input().split())) for _ in range(N)]
    board = [[0] * 101 for _ in range(101)]

    # 1. 드래곤 커브 구현하기
    for x, y, d, g in lst:
        tlst = [(y, x), (y+dy[d], x+dx[d])] # 현재까지 경로
        for _ in range(g):
            ey, ex = tlst[-1]
            tlst_size = len(tlst)

            for i in range(tlst_size-2, -1, -1):
                ny, nx = tlst[i]
                oy, ox = ny - ey, nx - ex # 중심으로 이동
                ry, rx = ey + ox, ex - oy # 회전 (oy, ox) -> (ox, -oy)
                tlst.append((ry, rx))

        for ty, tx in tlst:
            board[ty][tx] = 1

    # 2. 사각형이 둘러쌓여있는지 확인
    ans = 0
    for r in range(100):
        for c in range(100):
            if board[r][c] == 1 and board[r+1][c] == 1 and board[r][c+1] == 1 and board[r+1][c+1] == 1: ans += 1

    print(f"{t}: {ans}")