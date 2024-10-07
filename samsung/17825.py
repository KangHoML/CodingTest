import sys
sys.stdin = open("17825.txt", "r")

def dfs(cnt, sm):
    global ans

    # 종료 조건
    if cnt == 10:
        ans = max(ans, sm)
        return

    # 각 말 이동
    for i in range(4):
        # 현재 위치
        pos = piece[i]
        
        # 한 칸 먼저 이동
        nxt = path[pos][-1] 

        # 나머지 이동
        for _ in range(dice[cnt]-1): 
            nxt = path[nxt][0]

        # 백트래킹(다음 위치 이동 가능할 때)
        if nxt == LEN-1 or (nxt not in piece):
            piece[i] = nxt
            dfs(cnt+1, sm+board[nxt])
            piece[i] = pos

for TC in range(1, int(input()) + 1):
    dice = list(map(int, input().split()))
    #                                20  21  22  23  24  25  26  27  28  29  30  31  32
    board = list(range(0, 40, 2)) + [13, 16, 19, 22, 24, 28, 27, 26, 25, 30 ,35, 40, 0]
    LEN = len(board)

    # 경로 기록
    path = [[] for _ in range(LEN)]
    for i in range(LEN):
        if i == 19:
            path[i].append(LEN-2)
            continue
        elif i == 22 or i == 24:
            path[i].append(28)
            continue
        elif i == LEN-1:
            path[i].append(i)
            continue

        path[i].append(i+1)

        if i == 5: path[i].append(20)
        elif i == 10: path[i].append(23)
        elif i == 15: path[i].append(25)

    ans = 0
    piece = [0] * 4 # 각 말의 위치
    dfs(0, 0)
    
    print(f"{TC}: {ans}")