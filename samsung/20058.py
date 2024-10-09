import sys
from collections import deque
sys.stdin = open("20058.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global ice, group

    queue = deque([(x, y)])
    v[x][y] = 1
    cnt = 1
    while queue:
        r, c = queue.popleft()
        ice += board[r][c]

        for d in range(4):
            nr, nc = r + dx[d], c + dy[d]

            if not (0 <= nr < LENB and 0 <= nc < LENB and v[nr][nc] == 0 and board[nr][nc] != 0): continue

            queue.append((nr, nc))
            v[nr][nc] = 1
            cnt += 1

    group = max(cnt, group)
    return

for TC in range(1, int(input()) + 1):
    # 입력
    N, Q = map(int, input().split())
    LENB = 2 ** N
    board = [list(map(int, input().split())) for _ in range(LENB)]
    clst = list(map(int, input().split()))

    for L in clst:
        # 보드 복사
        new_board = [[0] * LENB for _ in range(LENB)]

        # 1. 부분 격자 회전
        LENP = 2 ** L
        for x in range(0, LENB, LENP):
            for y in range(0, LENB, LENP):
                for px in range(0, LENP):
                    for py in range(0, LENP):
                        new_board[x+px][y+py] = board[x+LENP-1-py][y+px]

        # 2. 얼음 삭제
        lst = []
        for x in range(LENB):
            for y in range(LENB):
                if new_board[x][y] == 0: continue

                cnt = 0
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if (0 <= nx < LENB and 0 <= ny < LENB and new_board[nx][ny] > 0):
                        cnt += 1

                if cnt < 3: lst.append((x, y))

        for x, y in lst:
            new_board[x][y] -= 1

        board = new_board

    # 남은 얼음 합 및 가장 큰 덩어리
    ice, group = 0, 0
    v = [[0] * LENB for _ in range(LENB)]
    for x in range(LENB):
        for y in range(LENB):
            if v[x][y] == 0 and board[x][y] != 0: bfs(x, y)
            
    print(f"#{TC}:\n{ice}\n{group}")