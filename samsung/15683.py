import sys
sys.stdin = open("15683.txt", "r")

# 방향 (동쪽부터 시계방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 각 카메라 방향
cam_dir = [(0), (0, 2), (0, 3), (0, 2, 3), (0, 1, 2, 3)]


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    dfs()

    print(f"{t}: ")