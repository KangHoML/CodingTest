import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# p : 현재 인덱스 / i : 현재 탐색중인 인덱스
def dfs(p, i, visited):
    visited[p] = 0
    v = hope[p]

    if visited[v-1] == -1:
        dfs(v-1, i, visited)
    else:
        if v == (i+1):
            for i, times in enumerate(visited):
                if times == 0:
                    team.append(i) # 마지막 학생이 원하는 학생이 탐색중인 학생일 경우 팀 완성

def sol():
    global team
    team = []

    for i in range(n):
        visited = [-1] * n
        if i not in team: # 팀 멤버가 아닐 때만 탐색
            dfs(i, i, visited)
    
    return len(hope) - len(team)
    

if __name__ == "__main__":
    n_case = int(input())
    for _ in range(n_case):
        global n, hope
        
        n = int(input())
        hope = list(map(int, input().split()))

        print(sol())

