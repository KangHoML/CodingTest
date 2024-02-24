import sys
sys.setrecursionlimit(1000000) # 재귀 함수 사용 시 설정
input = sys.stdin.readline

def dfs(x, y, graph, visited):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(graph)

    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 현재 위치에서 이동 가능한 모든 방향 탐색
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            # 방문하지 않은 노드 중 같은 색상일 때만 이동
            if visited[nx][ny] == False and graph[x][y] == graph[nx][ny]:
                dfs(nx, ny, graph, visited)
    
def main():
    n = int(input())
    graph = list(list(input().strip()) for _ in range(n)) # 공백 문자 제거
    graph_blind = [[0] * n for _ in range(n)]

    # 적록색약을 위한 graph
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'G':
                graph_blind[i][j] = 'R'
            else:
                graph_blind[i][j] = graph[i][j]
    
    visited = [[False] * n for _ in range(n)]
    visited_blind = [[False] * n for _ in range(n)]
    num_area, num_area_blind = 0, 0
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                dfs(i, j, graph, visited)
                num_area += 1
            if visited_blind[i][j] == False:
                dfs(i, j, graph_blind, visited_blind)
                num_area_blind += 1
    
    print(f'{num_area} {num_area_blind}')

if __name__ == "__main__":
    main()