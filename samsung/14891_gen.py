import sys
sys.stdin = open("14891.txt", "r")

def rotate(idx, dir):
    if dir == 1:
        tmp = board[idx][7]
        board[idx][1:8] = board[idx][0:7]
        board[idx][0] = tmp
    elif dir == -1:
        tmp = board[idx][0]
        board[idx][0:7] = board[idx][1:8]
        board[idx][7] = tmp

for t in range(1, int(input()) + 1):
    board = [list(input()) for _ in range(4)] # '0': N / '1': S
    k = int(input())
    lst = [list(map(int, input().split())) for _ in range(k)]

    for idx, dir in lst:
        idx -= 1
        tlst = [(idx, dir)]

        # 왼쪽 처리
        ndir = dir
        for i in range(idx-1, -1, -1):
            if board[i][2] != board[i+1][6]:
                ndir = -ndir
                tlst.append((i, ndir))
            else:
                break
        
        # 오른쪽 처리
        ndir = dir
        for i in range(idx+1, 4):
            if board[i-1][2] != board[i][6]:
                ndir = -ndir
                tlst.append((i, ndir))
            else:
                break
        
        # 회전
        for num, d in tlst:
            rotate(num, d)

    # 점수 계산
    ans, score = 0, 1
    for arr in board:
        if arr[0] == '1': ans += score
        score *= 2

    print(f"#{t}: {ans}")