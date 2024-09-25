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

    # 회전
    for idx, dir in lst:
        is_rotate = [0] * 4
        if idx == 1:
            is_rotate[0] = dir

            if board[0][2] != board[1][6]:
                is_rotate[1] = -dir

                if board[1][2] != board[2][6]:
                    is_rotate[2] = dir

                    if board[2][2] != board[3][6]:
                        is_rotate[3] = -dir
        
        elif idx == 2:
            is_rotate[1] = dir

            if board[0][2] != board[1][6]:
                is_rotate[0] = -dir
            
            if board[1][2] != board[2][6]:
                is_rotate[2] = -dir

                if board[2][2] != board[3][6]:
                    is_rotate[3] = dir

        elif idx == 3:
            is_rotate[2] = dir

            if board[2][2] != board[3][6]:
                is_rotate[3] = -dir
            
            if board[1][2] != board[2][6]:
                is_rotate[1] = -dir

                if board[0][2] != board[1][6]:
                    is_rotate[0] = dir

        else:
            is_rotate[3] = dir

            if board[2][2] != board[3][6]:
                is_rotate[2] = -dir

                if board[1][2] != board[2][6]:
                    is_rotate[1] = dir

                    if board[0][2] != board[1][6]:
                        is_rotate[0] = -dir

        for i, val in enumerate(is_rotate):
            rotate(i, val)

    # 점수 계산
    ans, score = 0, 1
    for arr in board:
        if arr[0] == '1': ans += score
        score *= 2

    print(f"#{t}: {ans}")