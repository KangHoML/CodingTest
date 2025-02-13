import sys
sys.stdin = open("day18.txt", "r")

INF = int(1e9)

for T in range(1, int(input()) + 1):
    print(f"{T}: ")

    # 입력
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 초기값
    dp = [[0] * M for _ in range(N)]
    dp[0][0] = board[0][0]
    for j in range(1, M):
        dp[0][j] = dp[0][j-1] + board[0][j]
    
    # 2번쩨 행부터 갱신
    for i in range(1, N):
        l, r = [0] * M, [0] * M

        # 왼쪽에서 오른쪽
        l[0] = dp[i-1][0] + board[i][0]
        for j in range(1, M):
            l[j] = max(l[j-1], dp[i-1][j]) + board[i][j]
        
        # 오른쪽에서 왼쪽
        r[M-1] = dp[i-1][M-1] + board[i][M-1]
        for j in range(M-2, -1, -1):
            r[j] = max(r[j+1], dp[i-1][j]) + board[i][j]

        # 갱신
        for j in range(M):    
            dp[i][j] = max(l[j], r[j])
        
    print(dp[N-1][M-1])
