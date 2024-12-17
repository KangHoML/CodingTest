# 방향
dx = [1, 0, -1]
dy = [0, 1, -1]

def sol(n):
    board = [[0]] + [[0] * (i+1) for i in range(n)]
    x, y, dir = 0, 0, 0
    board[x][y] = 0
    cnt, dis = 1, n
    while dis > 0:
        for _ in range(dis):
            x, y = x + dx[dir], y + dy[dir]
            board[x][y] = cnt
            cnt += 1
            
        dis -= 1
        dir = (dir + 1) % 3

    result = []
    for r in board[1:]:
        result.extend(r)
        
    return result

def sol2(n):
    board = [[0] * (r + 1) for r in range(n)]
    x, y, dir, cnt = -1, 0, 0, 1
    for dis in range(n, 0, -1):
        for _ in range(dis):
            x, y = x + dx[dir % 3], y + dy[dir % 3]
            board[x][y] = cnt
            cnt += 1
        
        dir += 1
    
    return [c for r in board for c in r]

if __name__ == "__main__":
    n = 4
    print(sol2(n))