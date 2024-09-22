import sys
sys.stdin = open("14500.txt", "r")

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# path: 지나온 모든 경로에 대해서 dfs를 진행하기 위해서 (ㅗ 모양을 만들기 위해)
def dfs(cnt, val, path):
    global ans

    # 가지치기
    if (val + max_num * (4 - cnt)) <= ans:
        return
    
    # 종료조건
    if cnt == 4:
        ans = max(ans, val)
        return
    
    for x, y in path:
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            
            if not (0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0): continue

            # 백트래킹
            visited[nx][ny] = 1
            dfs(cnt + 1, val + board[nx][ny], path + [(nx, ny)])
            visited[nx][ny] = 0

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    ans = 0
    max_num = max(map(max, board))

    # 완전 탐색
    for x in range(n):
        for y in range(m):
            visited[x][y] = 1
            dfs(1, board[x][y], [(x, y)])
    
    print(f"#{t}: {ans}")