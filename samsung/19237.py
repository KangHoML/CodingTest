# 입력
N, M, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
directions = list(map(int, input().split()))
prior = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]

# 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상어 상황판
smell = [[(0, 0)] * N for _ in range(N)] # (상어, 시간)

# 냄새 정보 업데이트
def update_smell():
    for i in range(N):
        for j in range(N):
            s, t = smell[i][j]
            
            # 냄새가 남아있는 경우
            if t > 0:
                t -= 1
            
            if board[i][j] != 0:
                s = board[i][j]
                t = k
            
            smell[i][j] = (s, t)

def move():
    new_board = [[0] * N for _ in range(N)] # 새로운 보드를 사용해야만 같은 상어를 여러 번 탐색하지 않음
    for x in range(N):
        for y in range(N):
            # 상어인 경우
            if board[x][y] != 0:
                dir = directions[board[x][y]-1]
                cnt = 0

                for d in prior[board[x][y]-1][dir-1]:
                    nx, ny = x + dx[d-1], y + dy[d-1]
                    
                    # 주변에 아무 냄새가 없는 곳이 있는 경우
                    if nx >= 0 and nx < N and ny >= 0 and ny < N and smell[nx][ny][1] == 0:                        
                        # 방향 갱신
                        directions[board[x][y]-1] = d

                        # 빈 칸 또는 자신보다 큰 상어 (new_board로 체크해야 함!)
                        if new_board[nx][ny] == 0 or new_board[nx][ny] > board[x][y]:
                            new_board[nx][ny] = board[x][y]

                        break
                    
                    cnt += 1
                
                # 주변에 아무 냄새가 없는 곳이 없는 경우
                if cnt == 4:
                    for d in prior[board[x][y]-1][dir-1]:
                        nx, ny = x + dx[d-1], y + dy[d-1]

                        if nx >= 0 and nx < N and ny >= 0 and ny < N:
                            s, _ = smell[nx][ny]

                            if s == board[x][y]:
                                directions[board[x][y]-1] = d
                                new_board[nx][ny] = board[x][y]
                                break
    
    return new_board

result = 0
while True:
    result += 1
    update_smell()
    board = move()

    check = 1
    for i in range(N):
        for j in range(N):
            if board[i][j] > 1:
                check = 0
    
    if check == 1:
        print(result)
        break

    if result >= 1000:
        print(-1)
        break
