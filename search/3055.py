import sys
from collections import deque
input = sys.stdin.readline

def water_bfs(w_start):
    queue_1 = deque([])
    for (w_x, w_y) in w_start:
        queue_1.append((w_x, w_y))
        w_visited[w_x][w_y] = 0

    while(queue_1):
        w_x, w_y = queue_1.popleft()
        for i in range(4):
            nx = w_x + dx[i]
            ny = w_y + dy[i]

            if nx >= 0 and nx < r and ny >= 0 and ny < c:
                if graph[nx][ny] == '.' and w_visited[nx][ny] == 1e9:
                    # water pass
                    w_visited[nx][ny] = w_visited[w_x][w_y] + 1
                    queue_1.append((nx, ny))

def animal_bfs(a_x, a_y):
    queue_2 = deque([(a_x, a_y)])
    a_visited[a_x][a_y] = 0
    while(queue_2):
        a_x, a_y = queue_2.popleft()
        for i in range(4):
            nx = a_x + dx[i]
            ny = a_y + dy[i]

            if nx >= 0 and nx < r and ny >= 0 and ny < c:
                if graph[nx][ny] != 'X' and a_visited[nx][ny] == -1:
                    # animal pass
                    if a_visited[a_x][a_y] + 1 < w_visited[nx][ny]:
                        a_visited[nx][ny] = a_visited[a_x][a_y] + 1
                        queue_2.append((nx, ny))

def main():
    global r, c, dx, dy, graph, w_visited, a_visited, dx, dy
    r, c = map(int, input().split())
    graph = [list(input().strip()) for _ in range(r)]
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    w_visited = [[1e9] * c for _ in range(r)]
    a_visited = [[-1] * c for _ in range(r)]
    w_start = []

    for i in range(r):
        for j in range(c):
            if graph[i][j] == '*':
                w_start.append((i, j))
            elif graph[i][j] == 'S':
                a_x, a_y = i, j
            elif graph[i][j] == 'D':
                d_x, d_y = i, j
    
    if w_start is not None:
        water_bfs(w_start)
    animal_bfs(a_x, a_y)
        
    if a_visited[d_x][d_y] == -1:
        print("KAKTUS")
    else:
        print(a_visited[d_x][d_y])

if __name__ == "__main__":
    main()