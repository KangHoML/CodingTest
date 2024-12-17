from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(room):
    v = [[0] * 5 for _ in range(5)]
    for x in range(5):
        for y in range(5):
            if room[x][y] != 'P': continue

            v[x][y] = 1
            for dir1 in range(4):
                nx, ny = x + dx[dir1], y + dy[dir1]

                # 예외 상황
                if not (0 <= nx < 5 and 0 <= ny < 5 and v[nx][ny] == 0): continue

                if room[nx][ny] == 'X': continue
                elif room[nx][ny] == 'P': return 0 
                else:
                    for dir2 in range(4):
                        nnx, nny = nx + dx[dir2], ny + dy[dir2]
                        
                        # 예외상황
                        if not (0 <= nnx < 5 and 0 <= nny < 5 and v[nnx][nny] == 0): continue

                        if room[nnx][nny] == 'P': return 0
                        
    return 1

def bfs(room):
    v = [[0] * 5 for _ in range(5)]
    
    for x in range(5):
        for y in range(5):
            if room[x][y] != 'P': continue
            v[x][y] = 1

            queue = deque([(x, y, 0)])
            while(queue):
                qx, qy, dis = queue.popleft()
                
                for d in range(4):
                    nqx, nqy = qx + dx[d], qy + dy[d]
                
                    # 예외처리
                    if not (0 <= nqx < 5 and 0 <= nqy < 5 and v[nqx][nqy] == 0 and dis < 2): continue

                    # 경우에 따른 처리
                    if room[nqx][nqy] == 'X': continue
                    elif room[nqx][nqy] == 'P': return 0
                    else: queue.append((nqx, nqy, dis + 1))
    
    return 1

def sol(places):
    ans = []
    for room in places:
        # ans.append(check(room))
        ans.append(bfs(room))
    return ans

if __name__ == "__main__":
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(sol(places))