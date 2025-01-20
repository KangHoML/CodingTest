import sys
import heapq
sys.stdin = open("day6.txt", "r")
INF = int(1e9)

def dijkstra(idx):
    dp = [INF] * (N + 1)
    dp[idx] = 0

    queue = []
    heapq.heappush(queue, (0, idx))
    while queue:
        dist, cur = heapq.heappop(queue)

        if dp[cur] < dist: continue

        for nxt, cost in graph[cur]:
            if dist + cost < dp[nxt]:
                dp[nxt] = dist + cost
                heapq.heappush(queue, (dist + cost, nxt))
    
    return dp

for T in range(1, int(input()) + 1):
    print(f'{T}:')

    # 입력
    N, E = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(E)]
    v1, v2 = map(int, input().split())
    
    # 초기화
    graph = [[] for _ in range(N + 1)]
    for a, b, c in info:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    # 다익스트라
    dp1 = dijkstra(1)
    dp2 = dijkstra(v1)
    dp3 = dijkstra(v2)

    # 두 정점을 지나는 최소 거리
    mn_dist = min(dp1[v1] + dp2[v2] + dp3[N], dp1[v2] + dp3[v1] + dp2[N])
    ans = mn_dist if mn_dist < INF else -1
    print(ans)