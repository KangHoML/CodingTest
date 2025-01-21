from collections import deque

def sol1(m, n, puddles):
    # 초기화
    dp= [[0] * m for _ in range(n)]
    dp[0][0] = 1
    
    # bfs
    queue = deque([(0, 0)])
    while queue:
        r, c = queue.popleft()
        
        for nr, nc in [(r + 1, c), (r, c + 1)]:
            if not (0 <= nr < n and 0 <= nc < m): continue
            
            if [nc + 1, nr + 1] in puddles: continue
            
            # 방문하지 않은 경우에만 추가
            if dp[nr][nc] == 0: queue.append((nr, nc))
            
            dp[nr][nc] += dp[r][c]
    
    # 최솟값 개수 반환
    return dp[n-1][m-1] % 1000000007

def dfs(x, y, dp, puddles):
    n, m = len(dp), len(dp[0])

    # 종료 조건
    if x == n-1 and y == m-1: return 1

    # 방문 여부 확인
    if dp[x][y] != 0: return dp[x][y]

    for nx, ny in [(x + 1, y), (x, y + 1)]:
        if not (0 <= nx < n and 0 <= ny < m): continue
        if [ny + 1, nx + 1] in puddles: continue

        dp[x][y] += dfs(nx, ny, dp, puddles)

    return dp[x][y]

def sol2(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    return dfs(0, 0, dp, puddles) % 1000000007

def sol3(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if ([y, x] in puddles) or ((x, y) == (1, 1)): continue

            # 위와 왼쪽을 더한 값
            dp[x][y] = dp[x-1][y] + dp[x][y-1]
    
    return dp[n][m] % 1000000007

if __name__ == "__main__":
    m, n = 4, 3
    puddles = [[2, 2]]
    print(sol2(m, n, puddles))