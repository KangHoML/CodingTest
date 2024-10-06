import sys
sys.stdin = open("17143.txt", "r")

# 상, 하, 우, 좌
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for TC in range(1, int(input()) + 1):
    R, C, M = map(int, input().split())
    slst = []
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        slst.append([r-1, c-1, s, d-1, z])
    
    # 낚시왕 움직임 구현
    ans = 0
    for fc in range(C):
        slst.sort(key=lambda x: (x[1], x[0]))
        
        # 상어 잡기
        for sidx in range(len(slst)):
            x, y, s, d, z = slst[sidx]
            if y == fc:
                ans += z
                slst.pop(sidx)
                break
        
        # 상어 이동 (x, y, s, d, z)
        for i in range(len(slst)):
            x, y, s, d, z = slst[i]

            # 가지치기
            if d == 0 or d == 1: s %= (2 * (R-1))
            else: s %= (2 * (C-1))

            nx, ny = x, y
            for _ in range(s):
                # 다음 이동할 곳이 범위를 넘치는 경우
                if not (0 <= nx + dx[d] < R and 0 <= ny + dy[d] < C):
                    if d == 0 or d == 2: d += 1
                    else: d -= 1

                # 한 칸 이동
                nx, ny = nx + dx[d], ny + dy[d]

            slst[i] = [nx, ny, s, d, z]
        
        # 정렬 후 더 큰 상어만 남기기
        slst.sort(key=lambda x: (x[1], x[0], -x[4]))
        for i in range(len(slst)-1, 0, -1): # 마지막 인덱스부터 비교
            if slst[i][:2] == slst[i-1][:2]:
                slst.pop(i)
    
    print(f"{TC}: {ans}")