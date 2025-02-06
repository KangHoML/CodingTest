import sys
sys.stdin = open("day12.txt", "r")
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def is_skip(x, y, dir, dis, cnt):
    if min(x, x + dx[dir] * dis) > r2 + cnt or max(x, x + dx[dir] * dis) < r1 + cnt: return True
    if min(y, y + dy[dir] * dis) > c2 + cnt or max(y, y + dy[dir] * dis) < c1 + cnt: return True

    return False

for T in range(1, int(input()) + 1):
    print(f"{T}: ")
    
    # 입력
    r1, c1, r2, c2 = map(int, input().split())

    # 필요한 메모리
    lst = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]

    # 최대 개수5
    cnt = max(map(abs, [r1, c1, r2, c2]))

    # 초기값
    x, y = cnt, cnt
    num, dis, dir = 1, 1, 0

    # 달팽이 구현
    for dis in range(1, 2 * (cnt + 1)):
        for _ in range(2):
            # 한번에 이동해도 되는가?
            if is_skip(x, y, dir, dis, cnt):
                x, y = x + dx[dir] * dis, y + dy[dir] * dis
                num += dis
            
            else:
                for _ in range(dis):
                    if r1 + cnt <= x <= r2 + cnt and c1 + cnt <= y <= c2 + cnt:
                        lst[x - (r1 + cnt)][y - (c1 + cnt)] = num
                    x, y = x + dx[dir], y + dy[dir]
                    num += 1
            
            # 방향 전환
            dir = (dir + 1) % 4

    # 출력
    mxlen = len(str(max(map(max, lst))))
    for r in lst:
        print(' '.join([str(c).rjust(mxlen) for c in r]))