N, M, K = map(int, input().split())
graph = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    graph[r-1][c-1].append([m, s, d])

# 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    # 새로 만들지 않으면 이동한 값이 다시 영향을 주게 됨
    board = [[[] for _ in range(N)] for _ in range(N)]

    # 파이어볼 이동
    for i in range(N):
        for j in range(N):
            if graph[i][j] != []:
                for m, s, d in graph[i][j]:
                    x = (i + dx[d] * s) % N
                    y = (j + dy[d] * s) % N
                    board[x][y].append([m, s, d])
    
    # 이동한 파이어볼 체크
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) >= 2:
                new_m, new_s, new_d = 0, 0, [0, 2, 4, 6] # 초기값
                prev_d = board[i][j][0][2] # 처음 방향

                for m, s, d in board[i][j]:
                    new_m += m
                    new_s += s

                    # 이전의 방향과 나머지가 다르면
                    if (d % 2) != (prev_d % 2):
                        new_d = [1, 3, 5, 7]

                    prev_d = d
                
                # 질량 최신화
                new_m = new_m // 5
                if new_m == 0:
                    board[i][j] = [] # 해당 위치 초기화
                    continue

                # 속력 최신화
                new_s = new_s // len(board[i][j])

                # 방향 및 board 상태 최산화
                board[i][j] = []
                for d in new_d:
                    board[i][j].append([new_m, new_s, d])
    
    # 이동한 보드 복사하기 (deepcopy)
    graph = [row[:] for row in board]

result = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] != []:
            for m, s, d in graph[i][j]:
                result += m
print(result)