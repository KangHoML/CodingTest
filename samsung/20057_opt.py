import sys
sys.stdin = open("20057.txt", "r")

# 방향(왼쪽부터 반시계방향)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 테이블 (중앙 기준으로)
left = [(-2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01), (0, -2, 0.05), (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (2, 0, 0.02)]
down = [(-y, x, p) for x, y, p in left] 
right = [(-y, x, p) for x, y, p in down]
up = [(-y, x, p) for x, y, p in right]

table = [left, down, right, up]

def sol():
    global ans

    x, y = N//2, (N+1)//2
    dir = 0

    for i in range(1, N+1):
        for _ in range(2):
            for _ in range(i):
                # 다음 인덱스
                nx, ny = x + dx[dir], y + dy[dir]

                send = board[nx][ny]
                for j, k, p in table[dir]:
                    # 범위 밖일 경우
                    if not (0 <= nx + j < N and 1 <= ny + k <= N):
                        ans += int(board[nx][ny] * p)
                    # 범위 안일 경우
                    else:
                        board[nx+j][ny+k] += int(board[nx][ny] * p)

                    # 남은 send 양
                    send -= int(board[nx][ny] * p)

                # 남은 모래양 처리
                if not (0 <= nx + dx[dir] < N and 1 <= ny + dy[dir] <= N):
                    ans += send
                else:
                    board[nx + dx[dir]][ny + dy[dir]] += send

                # 현재 위치 모래 비우기
                board[nx][ny] = 0

                # 현재 인덱스 업데이트
                x, y = nx, ny

                # 종료 조건
                if x == 0 and y == 1: return

            dir = (dir + 1) % 4

for TC in range(1, int(input()) + 1):
    N = int(input())
    board = [[0] + list(map(int, input().split())) for _ in range(N)]

    ans = 0
    sol()

    print(f"#{TC}: {ans}")