import sys
sys.stdin = open("15686.txt", "r")

def combination(arr, n):
    result = []
    if n == 0: return [[]]

    for i, num in enumerate(arr):
        for j in combination(arr[i+1:], n-1):
            result.append([num] + j)
    
    return result

for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    hlst, clst = [], []
    for y in range(N):
        for x in range(N):
            if board[y][x] == 1: hlst.append((y, x)) 
            elif board[y][x] == 2: clst.append((y, x))

    ans = 10000
    for comb in combination(clst, M):
        dst_sum = 0
        for hy, hx in hlst:
            dst = 1000
            for cy, cx in comb:
                dst = min(dst, abs(hy-cy) + abs(hx-cx))
            
            dst_sum += dst
        
        ans = min(ans, dst_sum)
    
    print(f"{T}: {ans}")