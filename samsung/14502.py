import copy
from collections import deque
from itertools import combinations

# 입력
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 방향 / 결과
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = 0

# 안전지대 개수 세기
def count_zero(board):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1
    
    return cnt

# bfs를 통해 바이러스 퍼짐
def bfs(start_pos, board):
    global result

    queue = deque([])
    for pos in start_pos:
        queue.append(pos)
    
    while(queue):
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m and board[nx][ny] == 0:
                board[nx][ny] = 2
                queue.append((nx, ny))
    
    result = max(count_zero(board), result)

# 초기 위치 찾기
start_pos = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_pos.append((i, j))

# dfs를 이용하여 3개의 벽 놓는 모든 경우의 수에 대해 완전 탐색
def dfs(cnt):
    if cnt == 3:
        board = copy.deepcopy(graph)
        bfs(start_pos, board)
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(cnt + 1)
                graph[i][j] = 0 # 다시 탐색을 위해 0으로 만들어주기

# dfs를 통해 3개의 벽 조합 완전 탐색
def sol1():
    dfs(0)

# 조합을 이용해 3개의 벽 조합 완전탐색
# combination 직접 구현하기
def sol2():
    wall = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                wall.append((i, j))

    # 3개의 벽을 만들 수 있는 모든 조합에 대해
    for c in combinations(wall, 3):
        board = copy.deepcopy(graph)
        for x, y in c:
            board[x][y] = 1
        bfs(start_pos, board)

# sol1() # 시간 초과
sol2()
print(result)
