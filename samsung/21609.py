from collections import deque

# 입력
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 블록 그룹 찾기 위한 bfs
def bfs(i, j, visited):
    queue = deque([(i, j)])
    block = [(i, j)]
    rainbow = []
    while(queue):
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if nx >= 0 and nx < N and ny >= 0 and ny < N and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    rainbow.append((nx, ny))
                    queue.append((nx, ny))

                elif graph[nx][ny] == graph[i][j]:
                    visited[nx][ny] = 1
                    block.append((nx, ny))
                    queue.append((nx, ny))

    
    for x, y in rainbow:
        visited[x][y] = 0 # 0인 부분은 다시 탐색할 수 있도록

    return (len(block) + len(rainbow), len(rainbow), block+rainbow)

# 가장 큰 블록 그룹 찾기
def find_block():
    temp = []
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0 and visited[i][j] == 0:
                visited[i][j] = 1
                block_size, rainbow_size, to_be_removed = bfs(i, j, visited)
                
                if block_size >= 2:
                    temp.append((block_size, rainbow_size, i, j, to_be_removed))

    # block_size -> rainbow_size -> i -> j 순으로 내림차순 정렬
    temp.sort(key = lambda x: (-x[0], -x[1], -x[2], -x[3]))
    
    # 해당 그룹 반환 (가장 나중 인덱스부터 찾기)
    if temp != []:
        return temp[0]
    else:
        return -1

# 중력 (해당 경우마다 새로운 배열 만들면 런타임 에러 -> 직접 고치기)
def move_down():
    for i in range(N-2, -1, -1):
        for j in range(N):
            if graph[i][j] > -1:
                cursor = i

                while(cursor + 1 < N and graph[cursor + 1][j] == -2):
                    graph[cursor + 1][j] = graph[cursor][j]
                    graph[cursor][j] = -2
                    cursor += 1

# 반시계방향 돌리기
def rotate_reverse_clk(arr):
    temp = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            temp[N-1-j][i] = arr[i][j]
    
    return temp

result = 0
while(1):
    # 더 이상 그룹이 없으면 출력 및 break
    info = find_block()
    if info == -1:
        print(result)
        break
    
    block_size, _, x, y, to_be_removed = info
    result += block_size ** 2

    # 제거
    for i, j in to_be_removed:
        graph[i][j] = -2

    move_down()
    graph = rotate_reverse_clk(graph)
    move_down()