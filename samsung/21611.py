import sys
sys.stdin = open("21611.txt", "r")

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
sdir = [2, 1, 3, 0]

def snail(sx, sy):
    nsx, nsy, dir = sx, sy, 0
    lst = []

    for dis in range(1, N + 1):
        for _ in range(2):
            for _ in range(dis):
                nsx, nsy = nsx + dx[sdir[dir]], nsy + dy[sdir[dir]]
                if board[nsx][nsy] != 0: lst.append(board[nsx][nsy])
                if (nsx == 0 and nsy == 1): return lst
            dir = (dir + 1) % 4

    return lst

def move_group(sx, sy, nlst):
    new_board = [[0] * (N+1) for _ in range(N)]
    nsx, nsy, dir = sx, sy, 0
    idx = 0

    for dis in range(1, N + 1):
        for _ in range(2):
            for _ in range(dis):
                if idx == len(nlst) or (nsx == 0 and nsy == 1): return new_board
                nsx, nsy = nsx + dx[sdir[dir]], nsy + dy[sdir[dir]]
                new_board[nsx][nsy] = nlst[idx]
                idx += 1

            dir = (dir + 1) % 4

    return new_board

for TC in range(1, int(input()) + 1):
    # 입력
    N, M = map(int, input().split())
    board = [[0] + list(map(int, input().split())) for _ in range(N)]
    clst = []
    for _ in range(M):
        d, s = map(int, input().split())
        clst.append((d - 1, s))

    # 점수 기록
    score = [0] * 3
    sx, sy = N // 2, N // 2 + 1

    for d, s in clst:
        # 1. 삭제
        nsx, nsy = sx, sy
        for _ in range(s):
            nsx, nsy = nsx + dx[d], nsy + dy[d]
            if not (0 <= nsx < N and 1 <= nsy <= N): continue
            board[nsx][nsy] = 0

        # 2. 달팽이 이동 하며 lst에 담기
        lst = snail(sx, sy)

        # 3. 4칸 이상인 구슬 폭발 (더 이상 없을 때까지)
        while True:
            dlst = []

            i = len(lst) - 1
            while i > 0:
                cnt = 1

                for j in range(i - 1, -1, -1):
                    if lst[i] != lst[j]: break
                    cnt += 1

                # 4개 이상인 경우 삭제 리스트에 추가 (시작 인덱스, 삭제할 개수)
                if cnt >= 4: dlst.append((i - cnt + 1, cnt))

                i = j

            # 삭제 리스트가 없는 경우 break
            if len(dlst) == 0: break

            # 삭제
            for s, cnt in dlst:
                score[lst[s] - 1] += cnt
                for _ in range(cnt):
                    lst.pop(s)

        # 4. 그룹으로 묶기
        nlst = []
        i = 0
        while i < len(lst):
            cnt = 1

            j = i + 1
            while j < len(lst):
                if lst[i] != lst[j]: break
                cnt += 1
                j += 1

            nlst.append(cnt)
            nlst.append(lst[i])

            i = j

        # 5. 묶은 그룹을 옮겨주기
        board = move_group(sx, sy, nlst)

    ans = score[0] + 2 * score[1] + 3 * score[2]
    print(f"#{TC}: {ans}")