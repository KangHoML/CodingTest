# direction
dx = [1, 0, -1]
dy = [0, 1, -1]

def solution1(n):
    # 초기화
    board = [[0] * (i + 1) for i in range(n)]
    x, y, dir = -1, 0, 0
    val = 1
    cnt = n

    while cnt >= 1:
        for _ in range(cnt):
            x, y = x + dx[dir % 3], y + dy[dir % 3]
            board[x][y] = val
            val += 1
        dir += 1
        cnt -= 1

    return [i for j in board for i in j]

def solution2(n):
    board = [[0] * (i + 1) for i in range(n)]
    size = n * (n + 1) // 2 # 최대 반복 횟수
    x = y = dir = 0
    cnt = 1
    
    while(cnt <= size):
        board[x][y] = cnt
        nx, ny = x + dx[dir], y + dy[dir]
        cnt += 1

        # 범위 안일 때만 현재 좌표 업데이트
        if 0 <= nx < n and 0 <= ny <= nx and board[nx][ny] == 0:
            x, y = nx, ny
        else:
            dir = (dir + 1) % 3
            x, y = x + dx[dir], y + dy[dir]
    
    return [i for j in board for i in j]

if __name__ == "__main__":
    n = 4
    print(solution1(n))
    print(solution2(n))