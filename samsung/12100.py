import sys
sys.stdin = open("12100.txt", "r")

def move(new_board):
    for x in range(n):
        num = 0
        t_list = []

        for y in range(n):
            # 0인 경우 처리 X
            if new_board[x][y] == 0: continue

            # 기준과 현재 수가 동일한 경우
            if new_board[x][y] == num:
                t_list.append(num * 2)
                num = 0
            
            else:
                # 기준이 없는 경우
                if num == 0: num = new_board[x][y]

                # 기준과 현재가 다른 경우
                else:
                    t_list.append(num)
                    num = new_board[x][y]
        
        # 마지막 부분 처리
        if num > 0: t_list.append(num)
        new_board[x] = t_list + [0] * (n - len(t_list)) # 남은 부분을 0으로 채워 추가

def dfs(cnt, board):
    global ans

    # 종료 조건
    if cnt == 5:
        ans = max(ans, max(map(max, board))) # 2차원 배열의 최댓값
        return
    
    for dir in range(4): # 좌, 우, 상, 하
        transposed_board = list(map(list, zip(*board))) # 전치 배열

        if dir == 0:
            copied_board = [r[:] for r in board] # 기준
        elif dir == 1:
            copied_board = [r[::-1] for r in board] # 기준의 역
        elif dir == 2:
            copied_board = [r[:] for r in transposed_board]
        else:
            copied_board = [r[::-1] for r in transposed_board]

        move(copied_board)
        dfs(cnt+1, copied_board)

T = int(input())
for t in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    
    dfs(0, board)
    print(f'#{t}: {ans}')