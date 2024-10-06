import sys
sys.stdin = open("17140.txt", "r")

def op(board):
    new_lst = []
    for r in board:
        tdic = {}
        for c in range(len(r)):
            if r[c] == 0: continue

            if r[c] not in tdic:
                tdic[r[c]] = 1
            else:
                tdic[r[c]] += 1

        # value(cnt) -> key 순 오름차순
        tdic = sorted(tdic.items(), key=lambda x: (x[1], x[0]))
        tlst = []
        for k, v in tdic: tlst += [k, v]

        new_lst.append(tlst)
    
    # 최대 길이만큼 new_board 초기화
    max_len = max(len(r) for r in new_lst)
    max_len = max_len if max_len <= 100 else 100
    new_board = [[0] * max_len for _ in range(len(new_lst))]

    # 갱신
    for r in range(len(new_lst)):
        for c in range(len(new_lst[r])):
            if c >= 100: break
            new_board[r][c] = new_lst[r][c]
            
    return new_board

for TC in range(1, int(input()) + 1):
    R, C, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(3)]
    
    ans = 0
    while ans <= 100:
        # 종료 조건
        if 0 <= R-1 < len(board) and 0 <= C-1 < len(board[0]):
            if board[R-1][C-1] == K:
                break
        
        if len(board) >= len(board[0]):
            new_board = op(board)
        else:
            board = list(map(list, zip(*board))) # 전치
            new_board = op(board)
            new_board = list(map(list, zip(*new_board))) # 다시 전치
        
        ans += 1
        board = new_board

    if ans == 101: ans = -1
    print(f"{TC}: {ans}")