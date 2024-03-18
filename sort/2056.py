import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_pos):
    queue = deque([])
    total_time = [0] * n

    for i in start_pos:
        queue.append(i)
        total_time[i] = time[i]

    while(queue):
        node = queue.popleft()
        for i in graph[node]:
            degree[i] -= 1
            total_time[i] = max(total_time[i], total_time[node] + time[i])
            if degree[i] == 0:
                queue.append(i)

    return total_time

def main():
    global n, time, graph, degree
    n = int(input())
    task = [list(map(int, input().split())) for _ in range(n)]
    
    time = []
    graph = [[] for _ in range(n)]
    degree = [0] * n
    start_pos = []
    for i in range(n):
        time.append(task[i][0])
        if task[i][1] != 0:
            for j in range(2, len(task[i])):
                graph[task[i][j] - 1].append(i)
            degree[i] = task[i][1]
        if degree[i] == 0:
            start_pos.append(i)
    
    result = bfs(start_pos)
    print(max(result))

if __name__ == "__main__":
    main()