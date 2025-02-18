import sys
sys.stdin = open("day22.txt", "r")
INF = int(1e9)

for T in range(1, int(input()) + 1):
    print(f"{T}: ")

    # 입력
    N = int(input())
    M = int(input())

    # 그래프 구성    
    dp = [[INF] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        dp[a][b] = min(dp[a][b], c)

    # 플로이드-워셜
    for k in range(1, N + 1):
        dp[k][k] = 0
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    
    # 출력
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dp[i][j] == INF: dp[i][j] = 0
        print(*dp[i][1:])
            
