import sys
sys.stdin = open("20056.txt", "r")

# 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for TC in range(1, int(input()) + 1):
    # 입력
    N, M, K = map(int, input().split())
    flst = []
    for _ in range(M):
        r, c, m, s, d = map(int, input().split())
        flst.append([r - 1, c - 1, m, s, d])
    
    # k번 명령 진행
    for _ in range(K):
        LEN = len(flst)

        # k번 끝나기 전에 이미 파이어볼이 없어진 경우
        if LEN == 0: break
        
        # 1. 이동 (0: 행, 1: 열, 2: 질량, 3: 거리, 4: 방향)
        for i in range(LEN):
            # 행, 열 이동
            flst[i][0] = (flst[i][0] + dx[flst[i][4]] * flst[i][3]) % N
            flst[i][1] = (flst[i][1] + dy[flst[i][4]] * flst[i][3]) % N

        # 2. 파이어볼 합치기
        tdic = {}
        for _ in range(LEN):
            r, c, m, s, d = flst.pop(0)
            if (r, c) not in tdic: tdic[(r, c)] = [(m, s, d)]
            else: tdic[(r, c)].append((m, s, d))

        for k, v in tdic.items():
            cnt = len(v)

            # 1개인 경우
            if cnt == 1:
                flst.append([k[0], k[1], v[0][0], v[0][1], v[0][2]])
                continue

            # 2개 이상인 경우
            s, m = 0, 0
            prev_d = v[0][2]
            flag = 0
            for i in range(cnt):
                m += v[i][0]
                s += v[i][1]

                if v[i][2] % 2 != prev_d % 2: flag = 1
                prev_d = v[i][2]

            m = m // 5
            s = s // cnt

            if m > 0:
                for i in range(0, 8, 2):
                    flst.append([k[0], k[1], m, s, i+flag])

    ans = 0
    for i in range(len(flst)):
        ans += flst[i][2]

    print(f"{TC}: {ans}")