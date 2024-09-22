import sys
sys.stdin = open("14501.txt", "r")


for t in range(1, int(input()) + 1):
    n = int(input())
    data = []
    for i in range(n):
        ti, pi = map(int, input().split())
        data.append([ti, pi])

    dp = [0] * (n+1)
    for i in range(n-1, -1, -1):
        # 상담 가능한 경우 (해당 일의 pay + 현재 pay)
        if i + data[i][0] <= n:
            dp[i] = max(dp[i+1], dp[i+data[i][0]] + data[i][1])
        else:
            dp[i] = dp[i+1]

    print(f"#{t}: {dp[0]}")