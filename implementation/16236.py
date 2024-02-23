import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, shork_state, visited):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n = len(graph)
    min_distance = 1e9

    size, pos_x, pos_y = shork_state
    queue = deque([(pos_x, pos_y)])
    visited[pos_x][pos_y] = 0
    
    while queue:
        x, y = queue.popleft()

        # 방향 (동, 서, 남, 북)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위 만족하는가?
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                # 방문하지 않았는가? + 이동 가능한가?
                if visited[nx][ny] == -1 and size >= graph[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))    
    
    for i in range(n):
        for j in range(n):
            # 이동할 수 있는 경로 중 먹을 수 있는 물고기까지의 최단 경로
            if visited[i][j] != -1 and graph[i][j] >= 1 and graph[i][j] < size:
                if visited[i][j] < min_distance:
                    min_distance = visited[i][j]
                    x, y = i, j

    # 먹을 수 있는 물고기 없음
    if min_distance == 1e9:
        return False
    # 먹을 수 있는 물고기 위치 및 최단 경로
    else:
        return x, y, min_distance

def main():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[-1]*n for _ in range(n)]
    size = 2

    # 초기 상어의 위치
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                pos_x, pos_y = i, j
                graph[i][j] = 0 # 탐색했으므로 0

    distance = 0 # 최단 거리의 합
    fish = 0 # 현재까지 먹은 물고기 개수
    while True:
        # 현재 상어의 위치 및 크기
        shork_state = (pos_x, pos_y, size)
        
        # 각 물고기까지의 최단 경로 및 상어 위치 최신화
        state = bfs(graph, shork_state, visited)

        if not state:
            print(distance)
            break
        else:
            pos_x, pos_y = state[0], state[1]
            distance += state[2]
            graph[pos_x][pos_y] = 0 # 업데이트
            fish += 1
        
        # 먹은 물고기 수가 현재 크기만큼 되었을 때 size 업데이트
        if fish >= size:
            size += 1
            fish = 0

if __name__ == "__main__":
    main()
