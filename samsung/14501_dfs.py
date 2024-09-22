import sys
sys.stdin = open("14501.txt", "r")

def dfs(idx, val):
    global ans

    # 종료 조건
    if idx >= n:
        ans = max(ans, val)
        return
    
    # 상담 O
    if idx + data[idx][0] <= n:
        dfs(idx + data[idx][0], val + data[idx][1])

    # 상담 X
    dfs(idx + 1, val)

for t in range(1, int(input()) + 1):
    n = int(input())
    data = []
    for i in range(n):
        ti, pi = map(int, input().split())
        data.append([ti, pi])

    ans = 0
    dfs(0, 0)
    
    print(f"#{t}: {ans}")