import sys
from heapq import heappop, heappush
sys.stdin = open("day20.txt", "r")

INF = 10000
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
op = {0: [2, 3], 1: [2, 3], 2: [0, 1], 3: [0, 1]}

for T in range(1, int(input()) + 1):
    print(f'{T}: ')

    # 입력
    N = int(input())
    board = [input() for _ in range(N)]

    # 문 위치
    door = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == '#': door.append((i, j))
    sx, sy = door[0]
    ex, ey = door[1]

    # 초기화
    nMir = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
    q = []
    for sd in range(4):
        heappush(q, (0, (sx, sy, sd)))
        nMir[sx][sy][sd] = 0
    
    # 다익스트라
    while q:
        mir, (x, y, d) = heappop(q)

        # 이미 갱신한 경우
        if nMir[x][y][d] < mir: continue
        
        # 그래프
        lst = []
        lst.append((mir, (x + dx[d], y + dy[d], d)))
        if board[x][y] == '!':            
            lst.append((mir + 1, (x + dx[op[d][0]], y + dy[op[d][0]], op[d][0])))
            lst.append((mir + 1, (x + dx[op[d][1]], y + dy[op[d][1]], op[d][1])))

        # 그래프 탐색
        for nm, (nx, ny, nd) in lst:
            # 이동 불가능한 경우
            if not (0 <= nx < N and 0 <= ny < N and board[nx][ny] != '*'): continue    

            # 갱신
            if nMir[nx][ny][nd] > nm:
                nMir[nx][ny][nd] = nm
                heappush(q, (nm, (nx, ny, nd)))
    
    # 최종 도착 위치의 거울 개수
    print(min(nMir[ex][ey]))
