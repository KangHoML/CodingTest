import sys
from collections import deque
input = sys.stdin.readline
        
def bfs(start_pos):
    queue = deque([])
    for i in start_pos:
        queue.append(i)
    
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            degree[i-1] -= 1
            cnt[i-1] = cnt[node] + 1
            if degree[i-1] == 0:
                queue.append(i-1)
    
def main():
    global graph, degree, cnt
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    degree = [0] * n
    cnt = [1] * n
    start_pos = []

    for i in range(m):
        s, v = map(int, input().split())
        graph[s-1].append(v)
        degree[v-1] += 1
    
    for i in range(n):
        if degree[i] == 0:
            start_pos.append(i)

    bfs(start_pos)
    print(' '.join(str(i) for i in cnt))

if __name__ == "__main__":
    main()