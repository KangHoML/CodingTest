import sys
sys.setrecursionlimit(1000000)
input= sys.stdin.readline

def sol1():
    line_1 = [i+1 for i in range(n)]
    count = 1

    while (count != 0):
        count = 0
        i = 0
        while(i < len(line_1)):
            if line_1[i] not in line_2:
                line_1.pop(i)
                line_2.pop(i)
                count += 1
            i += 1
    
    for i in line_1:
        result.append(i)

# p : 현재 인덱스 / i : 탐색 중인 인덱스 번호
def dfs(p, i, visited):
    visited[p] = 0
    v = line_2[p] # 현재 인덱스에 해당하는 값

    # 인접 노드가 방문하지 않은 노드라면
    if visited[v-1] == -1:
        dfs(v-1, i, visited) # 탐색
    
    # 방문한 노드라면
    else:
        if v == (i + 1): # 현재 값과 같을 때만
            result.append(v)

def sol2():
    for i in range(n):
        visited = [-1] * n
        dfs(i, i, visited)

if __name__ == "__main__":
    global n, line_2, result
    n = int(input())
    line_2 = [int(input()) for _ in range(n)]
    result = []
    
    # sol1()
    sol2()

    print(len(result))
    for i in result:
        print(i)