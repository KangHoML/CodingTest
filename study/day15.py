import heapq
INF = int(1e9)

def sol(n, paths, gates, summits):
    # 그래프 구성
    graph = [[] for _ in range(n + 1)]
    for s, e, d in paths:
        graph[s].append((e, d))
        graph[e].append((s, d))
    
    # 산봉우리
    v = [0] * (n + 1)
    for s in summits: v[s] = 1
    
    # 모든 시작 위치를 한 번에 입력
    intensity = [INF] * (n + 1)
    queue = []
    for g in gates: heapq.heappush(queue, (0, g))
    
    # 다익스트라
    while queue:
        i, cur = heapq.heappop(queue)
        
        # 탐색 필요 없는 노드
        if v[cur] == 1 or intensity[cur] < i: continue
        
        for nxt, cost in graph[cur]:
            value = max(i, cost)
            
            if intensity[nxt] > value:
                intensity[nxt] = value
                heapq.heappush(queue, (value, nxt))
    
    # 산봉우리에 따라 갱신 (같을 경우, 인덱스 작은 것 출력)
    idx, mn = 0, INF
    for s in sorted(summits):
        if intensity[s] < mn:
            idx = s
            mn = intensity[s]
    
    return [idx, mn]