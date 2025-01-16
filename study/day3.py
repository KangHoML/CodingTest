import sys
import heapq
sys.stdin = open("day3.txt", "r")
INF = int(1e9)

def getSmallestIndex(v):
    mn, idx = INF, 0

    for i in range(1, N+1):
        # 방문 or 최소가 아닌 경우
        if not (distance[i] < mn and v[i] == 0): continue
        
        mn, idx = distance[i], i
    
    return idx

def dijkstra_seq(start):
    # 방문 배열
    v = [0] * (N + 1)
    
    # 시작 노드 처리
    distance[start], v[start] = 0, 1
    for nxt, cost in net[start]:
        distance[nxt] = cost
        connect[nxt] = start
    
    # 순차 탐색
    for _ in range(N - 1):
        cur = getSmallestIndex(v)
        v[cur] = 1

        for nxt, cost in net[cur]:
            if distance[cur] + cost < distance[nxt]:
                distance[nxt] = distance[cur] + cost
                connect[nxt] = cur

def dijkstra_heap(start):
    # 초기화
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 우선순위 큐를 활용해 최소 거리 먼저 탐색
        dist, cur = heapq.heappop(q)

        # 순차 탐색의 방문 처리와 동일 (이미 더 작은 경로로 업데이트되어 있으므로)
        if distance[cur] < dist: continue

        # 현재 노드와 연결된 노드 탐색
        for nxt, cost in net[cur]:
            if dist + cost < distance[nxt]:
                connect[nxt] = cur
                distance[nxt] = dist + cost
                heapq.heappush(q, (dist + cost, nxt))

for T in range(1, int(input()) + 1):
    print(f"{T}: ")
    
    # 입력
    N, M = map(int, input().split())
    
    net = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        net[a].append((b, c)) # a -> b
        net[b].append((a, c)) # b -> a

    # 초기화
    distance = [INF] * (N + 1) # 거리
    connect = [0] * (N + 1) # 연결할 노드

    # 다익스트라
    # dijkstra_heap(1)
    dijkstra_seq(1)
    
    # 출력
    print(N - 1)
    for i in range(2, N + 1):
        print(i, connect[i])