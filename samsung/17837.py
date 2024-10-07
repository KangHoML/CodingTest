import sys
sys.stdin = open("17837.txt", "r")

# 방향
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
opp = {0: 1, 1: 0, 2: 3, 3: 2}

for TC in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    state = [[[] for _ in range(N)] for _ in range(N)]
    piece = []

    for i in range(K):
        r, c, d = map(int, input().split())
        state[r-1][c-1].append(i) 
        piece.append([r-1, c-1, d-1])

    ans = 0
    while ans <= 1000:
        ans += 1
        flag = 0

        # 각 piece 이동
        for i in range(len(piece)):
            r, c, d = piece[i]
            nr, nc = r + dx[d], c + dy[d] # 이동
            idx = state[r][c].index(i) # 인덱스 위치 찾기

            # 범위 밖 or 파란색
            if (not (0 <= nr < N and 0 <= nc < N)) or board[nr][nc] == 2:
                d = opp[d] # 반대 방향
                nr, nc = r + dx[d], c + dy[d] # 반대로 이동
                piece[i][2] = d

                # 여전히 파란색인 경우 이동 X
                if (not (0 <= nr < N and 0 <= nc < N)) or board[nr][nc] == 2: continue 

            # 흰색
            if board[nr][nc] == 0:
                for v in state[r][c][idx:]:
                    state[nr][nc].append(v) # 올려져있는 것 함께 이동
            
            # 빨간색
            if board[nr][nc] == 1:
                for v in state[r][c][idx:][::-1]:
                    state[nr][nc].append(v) # 거꾸로 한 뒤 이동
            
            # 업데이트
            for p in state[r][c][idx:]:
                piece[p][0] = nr
                piece[p][1] = nc
            del(state[r][c][idx:])

            if len(state[nr][nc]) >= 4:
                flag = 1
                break
        
        # 종료
        if flag == 1: break

    ans = ans if ans <= 1000 else -1
    print(f"{TC}: {ans}")