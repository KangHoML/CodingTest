import sys
sys.stdin = open("day11.txt", "r")

def check(row, col, queen):
    for r, c in enumerate(queen):
        if row - r == abs(col - c): return False
    return True

def dfs(row, queen):
    global ans

    # 종료 조건
    if row == N:
        ans += 1
        return

    for col in range(N):
        # 이미 방문한 곳
        if v[col] != 0: continue

        # 대각선 체크
        if not check(row, col, queen): continue

        v[col] = 1
        dfs(row + 1, queen + [col])
        v[col] = 0

for T in range(1, int(input()) + 1):
    print(f'{T}: ')

    # 입력
    N = int(input())

    # 각 행 및 열 당 하나씩만 존재
    ans = 0
    v = [0] * N
    dfs(0, [])

    print(ans)