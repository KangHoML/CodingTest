# 입력
graph = []
for i in range(4):
    data = list(map(int, input().split()))
    temp = []
    for j in range(4):
       f, d = data[j*2], data[j*2+1] - 1
       temp.append((f, d)) # 물고기 번호와 방향
    graph.append(temp)

# 방향 (반시계 순)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 해당 물고기 번호를 가진 좌표 찾기
def find_fish(graph, fish):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == fish:
                return i, j
    return -1, -1

# 모든 물고기 이동
def fish_move(graph):
    for f in range(1, 17):
        # 위치 찾기
        x, y = find_fish(graph, f)

        # 해당 물고기가 존재하면
        if x != -1 and y != -1:
            num, dir = graph[x][y]

            for _ in range(8):
                nx, ny = x + dx[dir], y + dy[dir]

                # 이동 가능할 경우
                if nx >= 0 and nx < 4 and ny >= 0 and ny < 4 and graph[nx][ny][0] != 's':
                    if graph[nx][ny] == 0:
                        graph[x][y] = (0, 0) # 현재 칸 비우고
                        graph[nx][ny] = (num, dir) # 이동
                    else:
                        graph[x][y], graph[nx][ny] = graph[nx][ny], (num, dir)
                    break
                
                # 이동 불가능할 경우
                dir = (dir + 1) % 8

# 이동가능한 상어 위치 찾기
def shark_pos(x, y, graph):
    _, dir = graph[x][y] # 상어 위치
    pos = []

    for _ in range(3):
        x, y = x + dx[dir], y + dy[dir]

        if x >= 0 and x < 4 and y >= 0 and y < 4 and graph[x][y][0] != 0:
            pos.append((x, y))

    return pos

# 상어의 최댓값을 찾기위한 dfs
def dfs(x, y, eat, graph):
    global max_num
    graph = [row[:] for row in graph] # deepcopy

    # 현재 위치 먹기
    num, dir = graph[x][y]
    eat += num
    graph[x][y] = ('s', dir) # 상어 위치

    # 물고기 이동하기
    fish_move(graph)

    # 상어 이동하기
    pos = shark_pos(x, y, graph)
    if pos:
        for nx, ny in pos:
            graph[x][y] = (0, 0) # 먹은 것 빈칸 처리
            dfs(nx, ny, eat, graph)
    else:
        max_num = max(eat, max_num)
        return
    
max_num = 0
dfs(0, 0, 0, graph)
print(max_num)