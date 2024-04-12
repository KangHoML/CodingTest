from collections import deque

# 입력
N, Q = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

# 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 부분 별로 돌리기
def turn(ice, step):
    size = 2 ** step
    temp = [[0] * 2**N for _ in range(2**N)]
    for i in range(0, 2 ** N, size):
        for j in range(0, 2 ** N, size):
            for k in range(size):
                for l in range(size):
                    temp[i + l][j + (size-1-k)] = ice[i + k][j + l]
    return temp

# 얼음 녹이기
def melt():
    melt_pos = []
    for x in range(2**N):
        for y in range(2**N):
            # 얼음 없으면 skip
            if ice[x][y] == 0:
                continue

            cnt = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx >= 0 and nx < 2**N and ny >= 0 and ny < 2**N and ice[nx][ny] > 0:
                    cnt += 1
                
            if cnt < 3:
                melt_pos.append((x, y)) # 얼음을 한번에 녹이기 위해
    
    for x, y in melt_pos:
        ice[x][y] -= 1 # 녹이기

def bfs():
    total, result = 0, 0
    visited = [[0] * 2**N for _ in range(2**N)]    
    for i in range(2**N):
        for j in range(2**N):
            lump = 0
            total += ice[i][j]

            # 이미 방문했거나 얼음이 없으면 다음 idx 탐색
            if visited[i][j] != 0 or ice[i][j] == 0:
                continue
            
            # 방문 처리
            queue = deque([(i, j)])
            visited[i][j] = 1

            while queue:
                x, y = queue.popleft()
                lump += 1

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx >= 0 and nx < 2**N and ny >= 0 and ny < 2**N and ice[nx][ny] > 0 and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        queue.append((nx, ny))

            result = max(result, lump)
    
    print(total)
    print(result)

'''
dfs로 풀경우 최대 깊이 오류로 인해 불가능 (런타임 에러)
'''
for step in L:
    ice = turn(ice, step) # 90도 회전
    melt() # 녹이기
bfs() # 전체 탐색
