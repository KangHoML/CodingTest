import sys
sys.stdin = open("15686.txt", "r")

def calc(tlst):
    sm = 0
    for hy, hx in hlst:
        dst = 100
        for cy, cx in tlst:
            dst = min(dst, abs(hy-cy) + abs(hx-cx))
        sm += dst
    
    return sm

def dfs(cnt, tlst):
    global ans

    # 종료조건
    if cnt == len(clst):
        if len(tlst) == M:
            ans = min(ans, calc(tlst))
        return
    
    dfs(cnt+1, tlst+[clst[cnt]]) # 유지
    dfs(cnt+1, tlst)             # 폐업


for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    hlst, clst = [], []
    for y in range(N):
        for x in range(N):
            if board[y][x] == 1: hlst.append((y, x)) 
            elif board[y][x] == 2: clst.append((y, x))

    ans = 10000
    dfs(0, [])
    print(f"{T}: {ans}")