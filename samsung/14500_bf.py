import sys
sys.stdin = open("14500.txt", "r")

cases = [
    # 1
    [(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)],

    # 2
    [(0, 1), (-1, 1), (-1, 2)], [(0, 1), (1, 1), (1, 2)], 
    [(1, 0), (1, 1), (2, 1)], [(-1, 0), (-1, 1), (-2, 1)],

    # 3
    [(0, 1), (0, 2), (-1, 2)], [(0, 1), (0, 2), (1, 2)],
    [(-1, 0), (-1, 1), (-1, 2)], [(1, 0), (1, 1), (1, 2)],
    [(0, 1), (-1, 1), (-2, 1)], [(-1, 0), (-2, 0), (-2, 1)],
    [(1, 0), (2, 0), (2, 1)], [(0, 1), (1, 1), (2, 1)],

    # 4
    [(1, 0), (0, 1), (1, 1)],

    # 5
    [(0, 1), (-1, 1), (0, 2)], [(0, 1), (1, 1), (0, 2)],
    [(1, 0), (1, 1), (2, 0)], [(1, 0), (1, -1), (2, 0)]
]

def tetro(x, y):
    max_val = 0

    for c in cases:
        val = board[x][y]

        for nx, ny in c:
            # 불가능한 경우 처리
            if not (0 <= x + nx < n and 0 <= y + ny < m): val = 0; break

            val += board[x + nx][y + ny]

        max_val = max(val, max_val)
    
    return max_val

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    ans  = 0

    # 완전 탐색
    for x in range(n):
        for y in range(m):
            ans = max(ans, tetro(x, y))

    print(f"#{t}: {ans}")