import sys
sys.stdin = open("14503.txt", "r")

# 방향(북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    x, y, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    ans = 0
    while True:
        # 1. 청소되지 않은 경우 현재 칸 청소
        if board[x][y] == 0:
            board[x][y] = 2
            ans += 1

        # 4방향 탐색
        is_clean = True
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            
            if board[nx][ny] == 0:
                is_clean = False
                break

        # 2. 청소되지 않은 빈칸 없는 경우        
        if is_clean:
            nx, ny = x - dx[d], y - dy[d]

            # 2-1. 후진 불가 시 정시
            if board[nx][ny] == 1: break

            # 2-2. 후진 가능 시 후진 후 1번
            else:
                x, y = nx, ny
                continue
        
        # 3. 청소되지 않은 빈칸 있는 경우
        else:
            for i in range(4):
                d = (d-1) % 4
                nx, ny = x + dx[d], y + dy[d]

                # 3-1. 반시계 방향 회전 후 청소되지 않은 경우 전진
                if board[nx][ny] == 0:
                    x, y = nx, ny
                    break

    print(f"#{t}: {ans}")