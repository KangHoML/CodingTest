# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(place):
    visited = [[0] * 5 for _ in range(5)]

    for x in range(5):
        for y in range(5):
            # 'P'일 때만 체크
            if not place[x][y] == 'P': continue

            # 방문 체크
            if visited[x][y] == 1: continue
            else: visited[x][y] = 1

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                # 범위 밖인지 체크
                if not (0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0): continue
                visited[nx][ny] = 1
                
                # 이동한 위치에서 체크
                if place[nx][ny] == 'P': return 0

                for j in range(4):
                    nnx, nny = nx + dx[j], ny + dy[j]

                    # 범위 밖인지 체크
                    if not (0 <= nnx < 5 and 0 <= nny < 5 and visited[nnx][nny] == 0): continue

                    # 이동한 위치에서 체크
                    if place[nnx][nny] == 'P':
                        if place[nx][ny] != 'X': return 0
    
    return 1

def solution(places):
    return [check(place) for place in places]

if __name__ == "__main__":
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
              ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
              ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
              ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
              ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(places))