import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i):
    global result
    visited[i] = True
    team.append(i+1)
    v = s[i]

    if visited[v-1] == False:
        dfs(v-1)
    else:
        # team 생성 확인
        if v in team:
            result += team[team.index(v):]

def sol():
    global team, visited
    visited = [False] * n

    for i in range(n):
        team = []
        # 한 번 검색한 부분은 다시 검색할 필요 없음!
        if visited[i] == False:
            dfs(i)

if __name__ == "__main__":
    global n, s
    for _ in range(int(input())):
        result = []
        n = int(input())
        s = list(map(int, input().split()))
        sol()

        print(n - len(result))
