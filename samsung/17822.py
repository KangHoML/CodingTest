import sys
sys.stdin = open("17822.txt", "r")

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def rot(x, d, k):
    # 회전
    for i in range(1, N+1):
        # 배수에 해당하지 않는 경우
        if i % x != 0: continue

        if d == 0:
            board[i][k:M], board[i][0:k] = board[i][0:M-k], board[i][M-k:M]
        else:
            board[i][0:M-k], board[i][M-k:M] = board[i][k:M], board[i][0:k]

    # 인접하면서 같은 수 찾기
    lst = []
    for i in range(1, N+1):
        for j in range(M):
            if board[i][j] == 0: continue

            for dir in range(4):
                ni = i + di[dir]
                if not (1 <= ni <= N): continue

                nj = (j + dj[dir]) % M
                if board[ni][nj] == board[i][j]: lst.append((ni, nj))
        
    # 삭제 or 처리
    if len(lst) == 0:
        avg, cnt = 0, 0
        for i in range(1, N+1):
            avg += sum(board[i])
            cnt += (M - board[i].count(0))
        
        # 보드가 전체 다 0인 경우 종료
        if cnt == 0: return
        
        avg /= cnt
        for i in range(1, N+1):
            for j in range(M):
                if board[i][j] == 0: continue

                if board[i][j] > avg: board[i][j] -= 1
                elif board[i][j] < avg: board[i][j] += 1
    else:
        for i, j in lst: board[i][j] = 0

for TC in range(1, int(input()) + 1):
    N, M, T = map(int, input().split())
    board = [[0] * M] + [list(map(int, input().split())) for _ in range(N)]

    for _ in range(T):
        x, d, k = map(int, input().split())
        rot(x, d, k)
    
    ans = sum(map(sum, board))
    print(f"{TC}: {ans}")
