import sys
import heapq
sys.stdin = open("day5.txt", "r")
INF = int(1e9)

def dijkstra(dp, graph, start):
    dp[start] = 0
    
    queue = []
    heapq.heappush(queue, (start, 0))

    while queue:
        dist, cur = heapq.heappop(queue)
        if dp[cur] < dist: continue

        for nxt, cost in graph[cur]:
            if dist + cost < dp[nxt]:
                dp[nxt] = dist + cost
                heapq.heappush(queue, (dist + cost, nxt))

def sol1():
    # 그래프 구성
    graph = [[] for _ in range(V + 1)]
    for cur, nxt, cost in info:
        graph[cur].append((nxt, cost))
        graph[nxt].append((cur, cost))

    # 다익스트라를 통한 최단 거리
    dpj, dps = [INF] * (V + 1), [INF] * (V + 1)
    dijkstra(dpj, graph, J)
    dijkstra(dps, graph, S)
    
    return dpj, dps

def floyd(dp):
    for k in range(1, V + 1):
        dp[k][k] = 0
        
        for i in range(1, V + 1):
            for j in range(1, V + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

def sol2():
    # 그래프 생성
    dp = [[INF] * (V + 1) for _ in range(V + 1)]
    for cur, nxt, cost in info:
        if cost < dp[cur][nxt]: dp[cur][nxt] = cost
        if cost < dp[nxt][cur]: dp[nxt][cur] = cost

    # floyd를 통해 모든 노드 간 최단 거리
    floyd(dp)

    return dp[J], dp[S]

for T in range(1, int(input()) + 1):
    print(f'{T}: ')

    # 입력
    V, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(M)]
    J, S = map(int, input().split())

    # 최단 거리
    # dpj, dps = sol1()
    dpj, dps = sol2()

    # 거리 합 최소
    mn_dist = INF
    for i in range(1, V + 1):
        if i in [J, S]: continue
        if dpj[i] + dps[i] < mn_dist: mn_dist = dpj[i] + dps[i]

    # 조건 확인
    lst = []
    for i in range(1, V + 1):
        # 시작점 제외
        if i in [J, S]: continue

        # 최소 합
        if dpj[i] + dps[i] != mn_dist: continue

        # 지헌이가 더 늦게 도착하는 경우 제외
        if dpj[i] > dps[i]: continue

        lst.append((i, dpj[i])) # 번호, 거리

    # 출력
    lst.sort(key=lambda x: (x[1], x[0]))
    print(lst[0][0]) if lst else print(-1)