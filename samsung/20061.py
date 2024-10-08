import sys
sys.stdin = open("20061.txt", "r")

opp = {1: 1, 2: 3, 3: 2}
def play(t, x):
    # 이동
    idx = board[x].index(1) if 1 in board[x] else 10
    if t == 1:
        board[x][idx-1] = 1
    elif t == 2:
        board[x][idx-2] = board[x][idx-1] = 1
    else:
        idx2 = board[x+1].index(1) if 1 in board[x+1] else 10
        idx = min(idx, idx2)
        board[x][idx-1] = board[x+1][idx-1] = 1

    score = 0
    while 1:
        lst = []

        # 가득찬 열 확인
        for j in range(4, 10):
            if board[0][j] == board[1][j] == board[2][j] == board[3][j] == 1:
                lst.append(j)
                board[0][j] = board[1][j]
            
        # 가득찬 열 삭제 및 점수 획득
        for j in lst:
            for i in range(4):
                board[i][5:j+1], board[i][4] = board[i][4:j], 0
            score += 1
        
        # 특수 칸 처리
        cnt = 0
        for j in range(4, 6):
            for i in range(4):
                if board[i][j] == 1:
                    cnt += 1
                    break
        
        # 아무것도 없을 때 종료
        if cnt == 0 and len(lst) == 0: break
        
        # 옮기기
        if cnt != 0:
            for i in range(4):
                board[i][4+cnt:10], board[i][4:4+cnt] = board[i][4:10-cnt], [0] * cnt
    
    return score

for TC in range(1, int(input()) + 1):
    N = int(input())
    board = [[0] * 10 for _ in range(10)]

    ans = 0
    for _ in range(N):
        t, x, y = map(int, input().split())

        # 파란색 부분
        ans += play(t, x)

        # 초록색 부분
        board = list(map(list, zip(*board)))
        ans += play(opp[t], y)
        board = list(map(list, zip(*board)))
    
    cnt = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1: cnt += 1
    
    print(f"#{TC}:\n{ans}\n{cnt}")
    

            