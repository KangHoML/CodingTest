def dfs(cur, visited, s, w):
    global ans, graph, animal 
    
    # 종료 조건
    if s <= w: return
    
    # 최댓값 갱신
    ans = max(s, ans)
    
    # 방문한 노드의 연결된 모든 노드 탐색
    for v in visited:
        for nxt in graph[v]:
            if nxt in visited: continue
            if animal[nxt] == 0: dfs(nxt, visited | {nxt}, s + 1, w)
            else: dfs(nxt, visited | {nxt}, s, w + 1)
    
def sol(info, edges):
    global animal, graph, ans
    
    # 1. 그래프 연결
    animal = info
    graph = [[] for _ in range(len(info))]
    for p, c in edges:
        graph[p].append(c)
    
    # 2. dfs 탐색
    ans = 0
    dfs(0, {0}, 1, 0)
    
    return ans

if __name__ == "__main__":
    info = [0,0,1,1,1,0,1,0,1,0,1,1]
    edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
    print(sol(info, edges))

