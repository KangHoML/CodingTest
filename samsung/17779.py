import sys
sys.stdin = open("17779.txt", "r")

def calc(x, y, d1, d2):
    lst = [0] * 5 # 합을 기록
    visited = [[0] * N for _ in range(N)] # 방문 여부 (5번 구역)

    # 5번 구역
    visited[x][y] = 1
    lst[4] += board[x][y]

    i = j = y
    for d in range(1, d1+d2+1):
        if d <= d1: i -= 1  # 왼쪽 한칸
        else: i += 1        # 오른쪽 한칸

        if d <= d2: j += 1  # 오른쪽 한칸
        else: j -= 1        # 왼쪽 한칸

        visited[x+d][i:j+1] = [1] * (j - i + 1)
        lst[4] += sum(board[x+d][i:j+1])
    
    # 나머지 구역
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1: continue
            
            if i < x + d1 and j <= y: lst[0] += board[i][j]
            elif i <= x + d2 and j > y: lst[1] += board[i][j]
            elif i >= x + d1 and j < y - d1 + d2: lst[2] += board[i][j]
            elif i > x + d2 and j >= y - d1 + d2: lst[3] += board[i][j]
    
    return max(lst) - min(lst)

for TC in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    ans = 100 * N * N
    # 모든 기준점
    for x in range(N-2):
        for y in range(1, N-1):
            # 가능한 모든 d1, d2
            for d1 in range(1, N-1):
                for d2 in range(1, N-1):
                    # 범위 체크
                    if not (0 <= x + d1 + d2 < N and 0 <= y-d1 < y + d2 < N): continue
                    ans = min(ans, calc(x, y, d1, d2))

    print(f"{TC}: {ans}")