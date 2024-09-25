import sys
sys.stdin = open("14890.txt", "r")

def is_path(arr):
    num = arr[0]
    slope = []

    for i in range(1, n):
        tlst = []

        # 동일 높이
        if arr[i] == num: continue
        
        # 이전보다 한 칸 낮을 때
        elif arr[i] - num == -1:
            for j in range(l):
                if not ((0 <= i+j < n) and (i+j not in slope)): continue
                if arr[i+j] == arr[i]: tlst.append(i+j)
            
            # 경사로 가능한 경우
            if len(tlst) == l:
                slope += tlst
                num -= 1
            
            else: return 0
        
        # 이전보다 한 칸 높을 때
        elif arr[i] - num == 1:
            for j in range(1, l+1):
                if not ((0 <= i-j < n) and (i-j not in slope)): continue
                if arr[i-j] == arr[i-1]: tlst.append(i-j)

            # 경사로 가능한 경우
            if len(tlst) == l:
                slope += tlst
                num += 1
            
            else: return 0
        
        # 이외의 경우
        else: return 0
    
    return 1
        
for t in range(1, int(input()) + 1):
    n, l = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for r in board:
        ans += is_path(r)

    for c in zip(*board):
        ans += is_path(c)
    
    print(f"#{t}: {ans}")
