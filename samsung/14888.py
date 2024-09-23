import sys
sys.stdin = open("14888.txt", "r")

def dfs(cnt, val):
    global min_val, max_val

    # 종료조건
    if cnt == n - 1:
        min_val = min(min_val, val)
        max_val = max(max_val, val)
        return
    
    for i in range(4): 
        if ops[i] <= 0: continue
        ops[i] -= 1
        
        # 계산
        if i == 0:
            dfs(cnt + 1, val + arr[cnt + 1])
        elif i == 1:
            dfs(cnt + 1, val - arr[cnt + 1])
        elif i == 2:
            dfs(cnt + 1, val * arr[cnt + 1])
        else:
            if val >= 0: dfs(cnt + 1, val // arr[cnt + 1])
            else: dfs(cnt + 1, -(abs(val) // arr[cnt + 1]))

        # 백트래킹    
        ops[i] += 1

for t in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split())) # 숫자
    ops = list(map(int, input().split())) # +, -, x, /
    
    max_val, min_val = -1e10, 1e10
    dfs(0, arr[0])
    print(f"{t}:\n  {max_val}\n  {min_val}")