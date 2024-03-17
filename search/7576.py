import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_pos):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    n = len(graph)


    queue = deque([])
    for (x, y) in start_pos:
        queue.append((x, y))
        visited[x][y] = 0

    while(queue):
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if visited[nx][ny] == -1 and graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    graph[nx][ny] = 1
                    queue.append((nx, ny))

def main():
    global graph, visited, m, n
    m, n = map(int, input().split())
    graph = []
    visited = [[-1] * m for _ in range(n)]

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    
    start_pos = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                start_pos.append((i, j))
    bfs(start_pos)

    n_max = 0
    for i in range(n):
        if max(visited[i]) > n_max:
            n_max = max(visited[i])
        if 0 in graph[i]:
            n_max = -1
            break
    
    print(n_max)

if __name__ == "__main__":
    main()