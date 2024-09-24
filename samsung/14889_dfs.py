import sys
sys.stdin = open("14889.txt", "r")

def calc(team1, team2):
    st1 = st2 = 0
    
    for i in range(n//2):
        for j in range(n//2):
            st1 += score[team1[i]][team1[j]]
            st2 += score[team2[i]][team2[j]] 

    return abs(st1 - st2)

def dfs(cnt, team1, team2):
    global ans

    # 종료조건
    if cnt == n:
        if len(team1) == len(team2):
            ans = min(ans, calc(team1, team2))
        return
    
    dfs(cnt + 1, team1 + [cnt], team2)
    dfs(cnt + 1, team1, team2 + [cnt])

for t in range(1, int(input()) + 1):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(n)]

    ans = 1e8
    dfs(0, [], [])
    print(f"#{t}: {ans}")
    