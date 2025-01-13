import sys
sys.stdin = open("day1.txt", "r")

INF = int(1e9)

def bellman_ford(start):
    dist[start] = 0

    # 최대 N-1개의 간선 + 음의 사이클 검증
    for i in range(N):
        # 모든 간선에 대해 확인
        for cur, next, cost in graph:
            if dist[cur] != INF and dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost

                if i == N-1: return True 
    
    return False

for T in range(1, int(input()) + 1):
    # 입력
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(M)]

    # 최단 거리 초기화
    dist = [INF] * (N + 1)

    # 벨만 포드를 통한 거리 갱신
    is_cycle = bellman_ford(1)

    # 출력
    print(f"{T}: ")
    if is_cycle:
        print(-1)
    else:
        for i in range(2, N + 1):
            if dist[i] == INF: print(-1)
            else: print(dist[i])
