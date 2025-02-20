import sys
from heapq import heappush, heappop
sys.stdin = open("day24.txt", "r")

INF = int(1e8)

def dijkstra():
    # 그래프 구성
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 다익스트라를 활용한 경로 갱신
    path = [[-1] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        dist = [INF] * (N + 1)
        parents = [-1] * (N + 1)
        
        q = []
        heappush(q, (0, i))
        dist[i] = 0

        while q:
            d, cur = heappop(q)

            if dist[cur] < d: continue

            for nxt, cost in graph[cur]:
                if d + cost < dist[nxt]:
                    parents[nxt] = cur
                    dist[nxt] = d + cost
                    heappush(q, (d + cost, nxt))

        # 갱신된 부모 노드를 따라 경로 갱신
        path[i][i] = '-'
        for j in range(1, N + 1):
            if j == i: continue

            cur, prev = j, parents[j]
            while prev != i:
                cur = prev
                prev = parents[cur]
            
            path[i][j] = cur
        
    return path

def floyd():
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    path = [[-1] * (N + 1) for _ in range(N + 1)]

    # 그래프 구성
    for _ in range(M):
        a, b, c = map(int, input().split())
        path[a][b], path[b][a] = b, a
        dist[a][b] = min(dist[a][b], c)
        dist[b][a] = min(dist[b][a], c)

    for k in range(1, N + 1):
        dist[k][k], path[k][k] = 0, '-'
        
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i == j: continue

                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[i][k]
    
    return path

for T in range(1, int(input()) + 1):
    print(f"{T}: ")

    # 입력
    N, M = map(int, input().split())

    # 경로표
    # path = dijkstra()
    path = floyd()

    for r in path[1:]: print(*r[1:])

        