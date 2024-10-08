import sys
from collections import deque
sys.stdin = open("19238.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_pass(x, y):
    for key, val in dic.items():
        if (x, y) == val[0]:
            return key
    return -1

def move_pass(bx, by):
    # 방문 표시
    v = [[-1] * N for _ in range(N)]
    queue = deque([(bx, by)])
    v[bx][by] = 0
    
    # 시작 위치에 승객 있을 경우
    p = find_pass(bx, by)
    if p != -1:
        return p, 0, bx, by

    lst = []
    while(queue):
        x, y = queue.popleft()

        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            
            # 범위 및 조건 체크
            if not (0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1 and v[nx][ny] == -1): continue

            queue.append((nx, ny))
            v[nx][ny] = v[x][y] + 1

            p = find_pass(nx, ny)
            if p != -1:
                lst.append((p, v[nx][ny], nx, ny))
    
    # 이동할 수 있는 곳이 없는 경우
    if len(lst) == 0:
        return -1, -1, -1, -1

    lst.sort(key=lambda x: (x[1], x[2], x[3]))
    return lst[0]

def move_taxi(p):
    # 찾은 승객의 종착지 찾기
    px, py = dic[p][0]
    ex, ey = dic[p][1]
    
    # 종착지까지 최단거리
    queue = deque([(px, py)])
    v = [[-1] * N for _ in range(N)]
    v[px][py] = 0

    while(queue):
        x, y = queue.popleft()

        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]

            # 범위 및 조건 체크
            if not (0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1 and v[nx][ny] == -1): continue

            queue.append((nx, ny))
            v[nx][ny] = v[x][y] + 1

            if nx == ex and ny == ey:
                return v[nx][ny], nx, ny
    
    return -1, -1, -1

for TC in range(1, int(input()) + 1):
    # 입력 및 초기값
    N, M, gas = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    bx, by = map(int, input().split())
    bx, by = bx - 1, by - 1

    dic = {}
    for i in range(1, M+1):
        sx, sy, ex, ey = map(int, input().split())
        dic[i] = [(sx-1, sy-1), (ex-1, ey-1)]

    for _ in range(M):
        # 가장 가까운 승객 찾기
        p, need_p, _, _ = move_pass(bx, by)

        # 이동할 수 없는 경우
        if p == -1:
            gas = -1
            break
            
        # 최단 경로로 이동
        need_t, bx, by = move_taxi(p)
        
        # 부족한 경우
        if gas < need_p + need_t:
            gas = -1
            break
        else:
            gas = gas - need_p + need_t
            dic.pop(p)

    print(f"{TC}: {gas}")