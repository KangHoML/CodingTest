# 입력
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
command = [tuple(map(int, input().split())) for _ in range(M)]

# 방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 처음 구름 위치
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

def move(i):
    dir, dis = command[i]
    
    for i in range(len(cloud)):
        nx = (N + cloud[i][0] + dx[dir-1] * dis) % N
        ny = (N + cloud[i][1] + dy[dir-1] * dis) % N

        graph[nx][ny] += 1
        visited[nx][ny] = True
        cloud[i] = (nx, ny)

def water_copy():
    for x, y in cloud:
        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i*2-1], y + dy[i*2-1] # 대각선 방향만 고려

            # 범위 안에 있는 경우만 고려
            if nx >= 0 and nx < N and ny >= 0 and ny < N and graph[nx][ny] > 0:
                cnt += 1

        graph[x][y] += cnt

def make_cloud():
    result = 0
    temp = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and not visited[i][j]:
                temp.append((i, j))
                graph[i][j] -= 2
            result += graph[i][j]
    return temp, result

# 최대한 직접 조정하기!
result = 0
for i in range(M):
    visited = [[False] * N for _ in range(N)]
    move(i) # 증가한 물의 위치 반환
    water_copy()
    cloud, result = make_cloud()
print(result)
        