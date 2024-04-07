import sys
input = sys.stdin.readline

# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 입력
n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))

# 주사위 값 갱신 함수
def move_dice(dir):
    # 동쪽
    if dir == 0:
        dice[2], dice[5], dice[3], dice[0] = dice[0], dice[2], dice[5], dice[3]
    # 서쪽
    elif dir == 1:
        dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
    # 북쪽
    elif dir == 2:
        dice[4], dice[0], dice[1], dice[5] = dice[5], dice[4], dice[0], dice[1]
    # 남쪽
    else:
        dice[5], dice[4], dice[0], dice[1] = dice[4], dice[0], dice[1], dice[5]

# 초기값
dice = [0] * 6 # 주사위 (idx 0: 윗면 / idx 6: 바닥)
cnt = 0 # 횟수
while(1):
    # 정해진 명령 횟수가 끝나면
    if cnt == k:
        break

    # 주사위 방향 및 횟수 증가 
    dir = command[cnt] - 1
    cnt += 1

    # 범위 밖
    if (x + dx[dir] < 0 or x + dx[dir] >= n or y + dy[dir] < 0 or y + dy[dir] >= m):
        continue
    
    # 범위 안
    x += dx[dir]
    y += dy[dir]
    move_dice(dir) # 주사위 값 갱신

    # 지도의 값이 0이면 주사위값 복사
    if graph[x][y] == 0:
        graph[x][y] = dice[5]

    # 0이 아니면 주사위에 지도값 복사
    else:
        dice[5] = graph[x][y]
        graph[x][y] = 0
    
    print(dice[0])
