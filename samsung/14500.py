import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 방향 (서, 동, 남, 북)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[False] * m for _ in range(n)]

# dfs를 통해 테크로미노 구현 ('ㅗ' 제외 구현)
def dfs(x, y, cnt, total):
    # 종료 조건
    global result
    if cnt == 3:
        result = max(result, total)
        return

    # 4 방향 이동 고려
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m and visited[nx][ny] == False:
            # 이동한 곳 방문처리 (커서 이동안할 때도 방문처리를 위해 안에서도 진행)
            visited[nx][ny] = True
                        
            # 2번째 이외에서는 이동
            dfs(nx, ny, cnt+1, total + graph[nx][ny])

            # 이동한 곳 방문처리 취소
            visited[nx][ny] = False

def fu(x, y):
    global result

    for i in range(4):
        total = graph[x][y]

        for j in range(3):
            dir = (i + j) % 4 # 'ㅜ'(012), 'ㅏ'(123), 'ㅓ'(230), 'ㅗ'(301)
            nx = x + dx[dir]
            ny = y + dy[dir]

            # 범위 밖이면
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                total = 0
                break

            # 범위 안이면
            total += graph[nx][ny]

        result = max(result, total)

def sol1():
    for i in range(n):
        for j in range(m):
            visited[i][j] = True # 현재 위치 방문 처리
            dfs(i, j, 0, graph[i][j])
            visited[i][j] = False # 다음 search를 통해 방문 처리 취소
            fu(i, j)

        
# dfs 한번에 구현
def dfs_2(x, y, cnt, total):
    global result, max_val

    # 지금 있는 값에 전체 graph의 최댓값을 남은 횟수만큼 더해도 result보다 작은 경우 return
    if result >= total + max_val * (4-cnt):
        return

    # 종료 조건
    if cnt == 3:
        result = max(result, total)
        return

    # 4 방향 이동 고려
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m and visited[nx][ny] == False:
            # 이동한 곳 방문처리 (커서 이동안할 때도 방문처리를 위해 안에서도 진행)
            visited[nx][ny] = True
            
            # 2번째에서는 고정 ('ㅗ' 계산을 위해서)            
            if cnt == 1:
                dfs(x, y, cnt+1, total + graph[nx][ny])

            # 2번째 이외에서는 이동
            dfs_2(nx, ny, cnt+1, total + graph[nx][ny])

            # 이동한 곳 방문처리 취소
            visited[nx][ny] = False

def sol2():
    for i in range(n):
        for j in range(m):
            visited[i][j] = True # 현재 위치 방문 처리
            dfs_2(i, j, 0, graph[i][j])
            visited[i][j] = False # 다음 search를 통해 방문 처리 취소


result = 0
max_val = max(map(max, graph)) # 최대값 (2번 solution을 위해서)
# sol1()
sol2()
print(result)
