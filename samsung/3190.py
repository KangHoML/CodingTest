import sys
from collections import deque

sys.stdin = open("3190.txt", "r")

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution():
    # 초기화
    queue = deque([(0, 0)])
    dir = 0  # 초기 방향
    cnt = 0  # 시간

    
    while True:
        cnt += 1

        # [1] 머리 이동
        hx, hy = queue[-1]
        nx, ny = hx + dx[dir], hy + dy[dir]

        # [2] 게임 종료 검사
        if not (0 <= nx < n and 0 <= ny < n): return cnt
        if (nx, ny) in queue: return cnt
        queue.append((nx, ny))

        # [3] 꼬리 이동
        if (nx, ny) not in apple_list:
            queue.popleft()
        else:
            apple_list.remove((nx, ny)) # 먹은 사과는 제거해주어야 함

        # [4] 방향 전환
        if cnt in dir_list:
            if dir_list[cnt] == 'D':
                dir = (dir + 1) % 4
            else:
                dir = (dir - 1) % 4

T = int(input())
for t in range(1, T + 1):
    # 입력
    n = int(input())

    apple_list = []
    for _ in range(int(input())):
        x, y = map(int, input().split())
        apple_list.append((x-1, y-1))

    dir_list = {}
    for _ in range(int(input())):
        cnt, dir = input().split()
        dir_list[int(cnt)] = dir

    # 해결
    print(f"#{t}: {solution()}")