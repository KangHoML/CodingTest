import sys
sys.stdin = open("19237.txt", "r")

# 상, 하, 좌, 우
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

for TC in range(1, int(input()) + 1):
    N, M, k = map(int, input().split())

    # 상어에 대한 정보 저장 (번호: 위치, 방향)
    slst = {i: [0] * 3 for i in range(1, M + 1)}

    # 위치별 (번호, 냄새) 저장
    sm = [[[0, 0] for _ in range(N)] for _ in range(N)]

    # 상어 위치 정보 입력
    for i in range(N):
        lst = list(map(int, input().split()))
        for j in range(N):
            if lst[j] == 0: continue
            slst[lst[j]][0], slst[lst[j]][1] = i, j
            sm[i][j][:] = [lst[j], k]

    # 각 상어별 방향
    lst = list(map(int, input().split()))
    for i in range(1, M + 1):
        slst[i][2] = lst[i - 1]

    # 각 상어별 우선순위
    prior = {}
    for i in range(1, M + 1):
        prior[i] = []
        for _ in range(4):
            prior[i].append(list(map(int, input().split())))

    ans = 0
    while ans <= 1000:
        # 상어 한 마리 남은 경우 종료
        if len(slst) == 1: break
        ans += 1

        # 1. 우선 순위에 따라 각 상어의 이동 방향 결정
        for key, val in slst.items():
            x, y, cd = val

            # 1-1. 아무 냄새가 없는가?
            flag = 0
            for dir in prior[key][cd - 1]:
                nx, ny = x + dx[dir], y + dy[dir]
                if 0 <= nx < N and 0 <= ny < N and sm[nx][ny][0] == 0:
                    flag = 1
                    slst[key] = [nx, ny, dir]
                    break

            if flag == 1: continue

            # 1-2. 자신의 냄새가 있는 방향
            for dir in prior[key][cd - 1]:
                nx, ny = x + dx[dir], y + dy[dir]

                if not (0 <= nx < N and 0 <= ny < N): continue

                flag = 0
                if sm[nx][ny][0] == key:
                    slst[key] = [nx, ny, dir]
                    flag = 1
                    break

                if flag == 1: break

        # 2. 이동한 상어 중 겹치는 구간 삭제
        # 2-1. 위치와 상어 번호를 오름차순으로 정렬
        sslst = sorted(slst.items(), key=lambda x: (x[1][0], x[1][1], x[0]))

        # 2-2. 삭제할 상어 번호 찾기
        dlst = []
        for i in range(len(sslst) - 1, 0, -1):
            ck, cv = sslst[i]
            pk, pv = sslst[i - 1]

            # 둘의 좌표가 동일한 경우 해당 key값 append
            if pv[0] == cv[0] and pv[1] == cv[1]: dlst.append(ck)

        # 2-3. 삭제
        for v in dlst:
            slst.pop(v)

        # 3. sm의 각 위치에 있는 냄새 하나씩 줄이기
        for i in range(N):
            for j in range(N):
                if sm[i][j][0] == 0: continue
                
                # 하나 줄이기
                if sm[i][j][1] > 0: sm[i][j][1] -= 1
                
                # 0인 경우 삭제
                if sm[i][j][1] == 0: sm[i][j][0] = 0

        # 4. 현재 자신의 위치에 자신의 냄새 남기기
        for key, val in slst.items():
            sm[val[0]][val[1]][:] = [key, k] # 냄새 남기기

    ans = ans if ans <= 1000 else -1
    print(f"{TC}: {ans}")