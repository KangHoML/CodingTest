# 입력
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 방향 (서, 남, 동, 북)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 초기값
pos_x, pos_y = n // 2, n // 2
left = [(-2, 0, 0.02), (2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01),
        (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, p) for x, y, p in left]
down = [(-y, x, p) for x, y, p in left]
up = [(-x, y, p) for x, y, p in down]
rate = [left, down, right, up]


# 퍼지는 모래
def spread(nx, ny, dir):
    global result
    l_sand = graph[nx][ny] # alpha에 담을 모래량

    for x, y, p in rate[dir]:
        nnx, nny = nx + x, ny + y

        # alpha 위치
        if p == 0:
            sand = l_sand

        # 나머지 퍼질 위치
        else:
            sand = int(graph[nx][ny] * p)
            l_sand -= sand

        # 범위 안이면
        if nnx >= 0 and nnx < n and nny >= 0 and nny < n:
            graph[nnx][nny] += sand

        # 범위 밖이면
        else:
            result += sand
    
    # 해당 칸에 모래 비워주기
    graph[nx][ny] = 0 

def sol():
    nx, ny = pos_x, pos_y
    dir = 0
    dis = 1

    
    while(1):
        for _ in range(dis):
            # 현재 위치가 0이라면 종료
            if nx == 0 and ny == 0:
                return
            
            # 다음 위치로 이동
            nx += dx[dir]
            ny += dy[dir]

            # 이동한 칸에 모래가 있다면
            if graph[nx][ny] != 0:
                spread(nx, ny, dir)

        # 다음 방향
        if dir % 2 == 1:
            if dis < n-1:
                dis += 1
        dir = (dir + 1) % 4        

result = 0
sol()
print(result)