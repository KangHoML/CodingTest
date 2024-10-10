import sys
sys.stdin = open("21608.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
score = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}

for TC in range(1, int(input()) + 1):
    # 입력
    N = int(input())
    like = {}
    for _ in range(N**2):
        s, s1, s2, s3, s4 = map(int, input().split())
        like[s] = [s1, s2, s3, s4]

    # 1. 자리 배치
    board = [[0] * N for _ in range(N)]
    for key, val in like.items():
        lst = []
        for x in range(N):
            for y in range(N):
                # 이미 있는 경우 배치 불가
                if board[x][y] != 0: continue

                lcnt, ecnt = 0, 0
                
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]

                    # 범위 밖
                    if not (0 <= nx < N and 0 <= ny < N): continue

                    if board[nx][ny] == 0: ecnt += 1
                    elif board[nx][ny] in like[key]: lcnt += 1
                
                lst.append((lcnt, ecnt, x, y))
        
        lst.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
        board[lst[0][2]][lst[0][3]] = key
        
    # 2. 만족도
    ans = 0
    for x in range(N):
        for y in range(N):
            lcnt = 0
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                # 범위 밖
                if not (0 <= nx < N and 0 <= ny < N): continue

                if board[nx][ny] in like[board[x][y]]: lcnt += 1

            ans += score[lcnt]

    print(f"{TC}: {ans}")