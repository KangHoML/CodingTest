import sys
sys.stdin = open("16235.txt", "r")

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for T in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tree = [[[] for _ in range(N)] for _ in range(N)]
    board = [[5] * N for _ in range(N)]

    # 나무 입력
    for _ in range(M):
        r, c, age = map(int, input().split())
        tree[r-1][c-1].append(age)
    
    for _ in range(K):
        # 봄 & 여름
        for i in range(N):
            for j in range(N):
                tree[i][j].sort() # 나이적은 순으로 처리

                for k in range(len(tree[i][j])):
                    # 양분이 더 많은 경우
                    if board[i][j] >= tree[i][j][k]:
                        board[i][j] -= tree[i][j][k]
                        tree[i][j][k] += 1
                    
                    # 양분이 더 적은 경우 (sort 했기 때문에 뒤에 있는 모든 나무 불가능)
                    else:
                        while k < len(tree[i][j]):
                            board[i][j] += (tree[i][j].pop() // 2)
                        break

        # 가을 & 겨울
        for i in range(N):
            for j in range(N):
                # 가을
                for k in range(len(tree[i][j])):
                    if tree[i][j][k] % 5 != 0: continue

                    for dir in range(8):
                        ni, nj = i + dx[dir], j + dy[dir]
                        if not (0 <= ni < N and 0 <= nj < N): continue
                        tree[ni][nj].append(1)
                
                # 겨울
                board[i][j] += arr[i][j]
    
    ans = 0
    for i in range(N):
        for j in range(N):
            ans += len(tree[i][j])
        
    print(f"#{T}: {ans}")