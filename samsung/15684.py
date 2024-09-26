import sys
sys.stdin = open("15684.txt", "r")

def check():
    for i in range(1, N+1):
        c = i
        
        for r in range(H):
            # 현재 위치에 사다리 존재
            if board[r][c] == 1:
                c += 1

            # 왼쪽에 사다리 존재
            elif board[r][c-1] == 1:
                c -= 1

        if c != i: return False
    
    return True

def dfs(n, idx):
    global flag

    # 종료조건
    if n == cnt:
        if check():
            flag = 1
            return
    
    for j in range(idx, len(pos)):
        x, y = pos[j]
        if board[x][y-1] == 0 and board[x][y+1] == 0: 
            board[x][y] = 1
            dfs(n+1, j+1) # 남은 후보들중 선택
            board[x][y] = 0
    

for t in range(1, int(input()) + 1):
    N, M, H = map(int, input().split())
    lst = []
    for _ in range(M):
        a, b = map(int, input().split())
        lst.append((a-1, b))

    # 1. 이미 사다리인 영역 표시
    board = [[0] * (N+2) for _ in range(H)]
    for a, b in lst: board[a][b] = 1
    
    # 2. 사다리 놓을 수 있는 위치 표시
    pos = []
    for i in range(H):
        for j in range(1, N):
            if board[i][j] == 0 and board[i][j-1] == 0 and board[i][j+1] == 0: pos.append((i, j))

    
    # 3. 0 ~ 3개까지 조건을 만족하는지 확인
    ans = -1
    for cnt in range(4):
        flag = 0
        dfs(0, 0)
        if flag == 1:
            ans = cnt
            break

    print(f"{t}: {ans}")