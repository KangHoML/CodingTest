# 입력
N = int(input())
graph = {}
for _ in range(N ** 2):
    data = list(map(int, input().split()))
    graph[data[0]] = data[1:]

# 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

seats = [[0] * N for _ in range(N)]
for student, like_arr in graph.items():
    # 선호도 판단
    info = []
    for x in range(N):
        for y in range(N):
            # 자리가 비어있을 때만 진행
            if seats[x][y] != 0:
                continue

            cnt_likes, cnt_empty = 0, 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < N and ny >= 0 and ny < N:
                    if seats[nx][ny] in like_arr:
                        cnt_likes += 1
                    if seats[nx][ny] == 0:
                        cnt_empty += 1

            info.append((x, y, cnt_likes, cnt_empty))

    # 선호도, 빈 좌석, 위치 순으로 정렬
    info.sort(key = lambda x: (-x[2], -x[3], x[0], x[1])) 
    r, c, _, _ = info[0]
    seats[r][c] = student

def get_score(likes):
    score = 0    
    if likes == 1:
        score += 1
    elif likes == 2:
        score += 10
    elif likes == 3:
        score += 100
    elif likes == 4:
        score += 1000
    
    return score

result = 0
for x in range(N):
    for y in range(N):
        likes = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if seats[nx][ny] in graph[seats[x][y]]:
                    likes += 1
        result += get_score(likes)
            
print(result)