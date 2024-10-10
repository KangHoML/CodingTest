import sys
from collections import deque
sys.stdin = open("21609.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    v = [[0] * N for _ in range(N)]

    # 초기값
    mx_group = set()
    mx_rcnt = 0

    for x in range(N):
        for y in range(N):
            # 가능한 경우만 탐색
            if not (v[x][y] == 0 and board[x][y] > 0): continue

            # 큐 초기화
            q = deque([(x, y)])
            group = set()       # 무지개 좌표를 위해

            group.add((x, y))
            v[x][y] = 1         # 같은 색깔 중복 방문을 막기 위해
            rcnt = 0            # 무지개 개수

            while q:
                nx, ny = q.popleft()

                for dir in range(4):
                    nnx, nny = nx + dx[dir], ny + dy[dir]

                    # 범위 및 방문 체크
                    if not (0 <= nnx < N and 0 <= nny < N and v[nnx][nny] == 0): continue
                    
                    # 가능한 경우 체크
                    if not ((nnx, nny) not in group and (board[nnx][nny] == board[x][y] or board[nnx][nny] == 0)): continue

                    q.append((nnx, nny))
                    group.add((nnx, nny))
                    
                    if board[nnx][nny] == 0: rcnt += 1
                    else: v[nnx][nny] = 1

            # 그룹 개수 -> 무지개 개수 -> 행 -> 열 (큰 값)
            # 같은 경우, 행과 열이 큰 값으로 업데이트
            if len(mx_group) < len(group) or (len(mx_group) == len(group) and mx_rcnt <= rcnt):
                mx_group, mx_rcnt = group, rcnt
    
    return mx_group

def gravity():
    for y in range(N):
        for x in range(N-2, -1, -1):
            if board[x][y] < 0: continue

            nx = x + 1
            while nx < N:
                if board[nx][y] != -2: break
                nx += 1
            
            board[nx-1][y], board[x][y] = board[x][y], board[nx-1][y]

for TC in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    score = 0
    
    while True:
        # 1. group 찾기
        group = bfs()
        if len(group) < 2: break

        # 2. group 제거
        score += (len(group)) ** 2
        for x, y in group:
            board[x][y] = -2

        # 3. 중력
        gravity()
        
        # 4. 반시계 회전
        board = list(map(list, zip(*board)))[::-1]

        # 5. 중력
        gravity()

    print(f"#{TC}: {score}")