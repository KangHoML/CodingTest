import sys
sys.stdin = open("day14.txt", "r")

INF = int(1e6)

def bellman_ford(start):
    # 거리 초기화
    dist[start] = 0

    for i in range(N):
        for cur in range(1, N + 1):
            # 초기값인 경우 갱신 필요 X
            if dist[cur] == -INF: continue

            for nxt, cost in graph[cur]:
                # 갱신하지 않아도 될때
                if dist[nxt] >= dist[cur] + cost: continue

                # 다음 경로 업데이트
                path[nxt] = cur
                dist[nxt] = dist[cur] + cost

                # 순환이 존재하는 경우, 다음 목적지를 INF로 만들기 
                if i == N - 1: dist[nxt] = INF

for T in range(1, int(input()) + 1):
    print(f'{T}: ')
    
    # 입력
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        cur, nxt, cost = map(int, input().split())
        graph[cur].append((nxt, cost))
        
    # 초기화
    dist = [-INF] * (N + 1)
    path = [0] * (N + 1)

    # 벨만 포드 알고리즘
    bellman_ford(1)

    # 가능한 경우
    ans = []
    if dist[N] != INF:
        cur = N
        while cur != 1:
            ans.append(cur)
            cur = path[cur]
        ans.append(cur)

    print(*ans[::-1]) if ans else print(-1)
