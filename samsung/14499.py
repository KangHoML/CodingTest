import sys
sys.stdin = open("14499.txt", "r")

# 방향(동, 서, 북, 남)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move_dice(c):
    if c == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif c == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]

    elif c == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

for t in range(1, int(input()) + 1):
    print(f"#{t}:")
    
    # 입력
    n, m, x, y, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    command = list(map(int, input().split()))

    # dice 각 면 초기화
    dice = [0] * 6

    for c in command:
        # [1] 주사위 이동
        nx, ny = x + dx[c-1], y + dy[c-1]
        if not (0 <= nx < n and 0 <= ny < m): continue
        x, y = nx, ny
        
        # [2] 주사위 배열 업데이트
        move_dice(c)

        # [3] 지도와 주사위 변경
        if board[x][y] == 0:
            board[x][y] = dice[5]
        else:
            dice[5] = board[x][y]
            board[x][y] = 0
        
        # [4] 맨 윗면 출력
        print(dice[0])