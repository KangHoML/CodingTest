import sys
sys.stdin = open("21610.txt", "r")

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0 ,-1]

for TC in range(1, int(input()) + 1):
    # 입력
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    lst = []
    for _ in range(M):
        d, s = map(int, input().split())
        lst.append((d-1, s))

    cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
    for d, s in lst:
        # 각 구름 이동 및 물 증가
        LENC = len(cloud)
        for i in range(LENC):
            cx, cy = cloud[i]
            ncx, ncy = (cx + dx[d] * s) % N, (cy + dy[d] * s) % N

            # 물 증가 및 새로운 구름 위치 추가
            cloud[i] = (ncx, ncy)
            board[ncx][ncy] += 1
    
        #  물복사 버그
        v = [[0] * N for _ in range(N)] 
        for cx, cy in cloud:
            v[cx][cy] = 1
            for dir in range(1, 8, 2):
                ncx, ncy = cx + dx[dir], cy + dy[dir]
                if not (0 <= ncx < N and 0 <= ncy < N and board[ncx][ncy] > 0): continue
                board[cx][cy] += 1

        # 구름 생성
        cloud = []
        for x in range(N):
            for y in range(N):
                if not (v[x][y] == 0 and board[x][y] >= 2): continue
                board[x][y] -= 2
                cloud.append((x, y))
    
    # 남은 양
    ans = sum(map(sum, board))
    print(f"{TC}: {ans}")