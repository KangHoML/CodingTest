import sys
from collections import deque
sys.stdin = open("21609.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    new_v = [[0] * N for _ in range(N)]

    q = deque([(x, y)])
    lst = [(x, y)]

    v[x][y] = 1
    new_v[x][y] = 1
    gcnt, rcnt = 1, 0
    while(q):
        nx, ny = q.popleft()

        for dir in range(4):
            nnx, nny = nx + dx[dir], ny + dy[dir]

            if not (0 <= nnx < N and 0 <= nny < N and new_v[nnx][nny] == 0 and board[nnx][nny] >= 0): continue
            new_v[nnx][nny] = 1

            # 같은 색상일 때
            if board[nnx][nny] == board[x][y]:
                v[nnx][nny] = 1
                q.append((nnx, nny))
                lst.append((nnx, nny))
                gcnt += 1
            
            # 무지개 색일 때
            elif board[nnx][nny] == 0:
                q.append((nnx, nny))
                lst.append((nnx, nny))
                gcnt += 1
                rcnt += 1

    return lst, gcnt, rcnt

for TC in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    score = 0
    while True:
        v = [[0] * N for _ in range(N)]

        # 1. group 찾기
        group = []
        for x in range(N):
            for y in range(N):
                if not (v[x][y] == 0 and board[x][y] > 0): continue

                lst, gcnt, rcnt = bfs(x, y)
                if gcnt < 2: continue

                group.append((lst, gcnt, rcnt))

        if len(group) == 0: break

        # 2. group 제거
        group.sort(key=lambda x: (-x[1], -x[2], -x[0][0][0], -x[0][0][1]))
        score += group[0][1] ** 2
        for x, y in group[0][0]:
            board[x][y] = -2

        # 3. 중력
        for y in range(N):
            for x in range(N - 2, -1, -1):
                if board[x][y] < 0: continue

                nx = x + 1
                while nx < N:
                    if board[nx][y] != -2: break
                    nx += 1

                board[nx - 1][y], board[x][y] = board[x][y], board[nx-1][y]

        # 4. 반시계 회전
        new_board = [[0] * N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                new_board[x][y] = board[y][N-1-x]
        board = new_board

        # 5. 중력
        for y in range(N):
            for x in range(N - 2, -1, -1):
                if board[x][y] < 0: continue

                nx = x + 1
                while nx < N:
                    if board[nx][y] != -2: break
                    nx += 1

                board[nx - 1][y], board[x][y] = board[x][y], board[nx-1][y]

    print(f"#{TC}: {score}")

