# 물고기 방향 순서 (왼쪽부터 시계)
fdx = [0, -1, -1, -1, 0, 1, 1, 1]
fdy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 상어 순서
sdx = [-1, 0, 1, 0]
sdy = [0, -1, 0, 1]

# [2] 물고기 이동: 새로운 fish_info 반환
def fish_move():
    for i in range(len(fish_info)):
        fx, fy, fd, cnt = fish_info[i]
        for j in range(8):
            fnx, fny = fx + fdx[(fd-j) % 8], fy + fdy[(fd-j) % 8]

            if 0 <= fnx < 4 and 0 <= fny < 4 and smell[fnx][fny] == 0 and (fnx, fny) != (shx, shy):
                fish_info[i] = [fnx, fny, (fd-j), cnt]
                break

# [3] 상어 이동
def shark():
    max_cnt = -1
    # [3-1] 상어 이동 위치 좌표
    for i in range(4):
        x1, y1 = shx + sdx[i], shy + sdy[i]
        if not (0 <= x1 < 4 and 0 <= y1 < 4): continue

        for j in range(4):
            x2, y2 = x1 + sdx[j], y1 + sdy[j]
            if not (0 <= x2 < 4 and 0 <= y2 < 4): continue

            for k in range(4):
                x3, y3 = x2 + sdx[k], y2 + sdy[k]
                if not (0 <= x3 < 4 and 0 <= y3 < 4): continue

                f_cnt = 0
                move_set = set(((x1, y1), (x2, y2), (x3, y3)))
                for x, y, d, cnt in fish_info:
                    if (x, y) in move_set:
                        f_cnt += cnt
                    if max_cnt < f_cnt:
                        max_cnt, snx, sny = f_cnt, x3, y3
                        del_set = move_set

    # [3-2] 물고기 삭제 및 냄새
    for i in range(len(fish_info)-1, -1, -1):
        if (fish_info[i][0], fish_info[i][1]) in del_set:
            smell[fish_info[i][0]][fish_info[i][1]] = 3
            fish_info.pop(i)

    return snx, sny

# 같은 좌표와 방향의 물고기 합쳐주기
def merge(fish_info):
    fish_info.sort(key=lambda x: (x[0], x[1], x[2]))

    i = 1
    while(i < len(fish_info)):
        if fish_info[i-1][:3] == fish_info[i][:3]:
            fish_info[i-1][3] += fish_info[i][3]
            fish_info.pop(i)
        else:
            i+=1

# 입력
M, S = map(int, input().split())
fish_info = []
for _ in range(M):
    fx, fy, fd = map(int, input().split())
    fish_info.append([fx - 1, fy - 1, fd - 1, 1])
shx, shy = map(int, input().split())

# 냄새 표시
smell = [[0] * 4 for _ in range(4)]

# 처음 상어 위치 표시
shx, shy = shx - 1, shy - 1

for _ in range(S):
    # [1] 복제
    copied_fish = [row[:] for row in fish_info]

    # [2] 물고기 이동
    fish_move()

    # [3] 상어 이동
    shx, shy = shark()

    # [4] 물고기 냄새
    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0:
                smell[i][j] -= 1

    # [5] 복제
    fish_info += copied_fish
    merge(fish_info)  # 같은 좌표와 방향의 물고기 합쳐주기

result = 0
for i in range(len(fish_info)):
    result += fish_info[i][3]
print(result)
