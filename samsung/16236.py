import sys
from collections import deque
sys.stdin = open("16236.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(shx, shy, shz):
    queue = deque([(shx, shy)])
    visited = [[-1] * N for _ in range(N)]
    visited[shx][shy] = 0
    flst = []
    
    while(queue):
        x, y = queue.popleft()

        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            
            # 예외조건 처리
            if not (0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1): continue

            # 상어크기 < 물고기 크기인 경우 못지나감
            if board[nx][ny] > shz: continue

            # 지나갈 수 있는 경우
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny)) 
            
            # 먹을 수 있는 물고기인 경우
            if 0 < board[nx][ny] < shz:
                flst.append((visited[nx][ny], nx, ny))
    
    return flst

for T in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 상어 정보
    for x in range(N):
        for y in range(N):
            if board[x][y] == 9:
                shx, shy, shz = x, y, 2
                board[x][y] = 0
    
    ans, eat = 0, 0
    while True:
        # 1. 먹을 수 있는 물고기 위치 탐색
        flst = bfs(shx, shy, shz)

        # 2. 종료 조건
        if len(flst) == 0: break

        # 3. 순서 고려하여 먹기
        flst.sort(key=lambda x: (x[0], x[1], x[2]))
        dst, shx, shy = flst[0]
        ans += dst
        board[shx][shy] = 0

        # 4. 상어 크기 업데이트
        eat += 1
        if eat == shz:
            shz += 1
            eat = 0

    print(f"{T}: {ans}")