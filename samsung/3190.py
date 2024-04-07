import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[0]*n for _ in range(n)]

k = int(input())
for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 'a'

# {시간: 방향}의 dictionary로 저장
l = int(input())
turn = dict()
for _ in range(l):
    x, c = input().split()
    turn[int(x)] = c

# 방향 정의 (동, 남, 서, 북) -> 시계방향 순
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 초기값 설정
pos_x, pos_y = 0, 0
graph[pos_x][pos_y] = 's'
cnt = 0
dir = 0
queue = deque([(pos_x, pos_y)]) # 꼬리의 위치를 이동시키기 위해 queue를 활용

while(True):
    cnt += 1
    pos_x += dx[dir]
    pos_y += dy[dir]

    if pos_x < 0 or pos_x >= n or pos_y < 0 or pos_y >= n or graph[pos_x][pos_y] == 's':
        break
    
    # 현재 위치에 사과가 있을 때
    if graph[pos_x][pos_y] == 'a':
        graph[pos_x][pos_y] = 's' # 뱀의 머리 최신화
        queue.append((pos_x, pos_y)) # 뱀인 곳을 큐에 추가
        
    # 현재 위치에 사과가 없을 때
    else:
        graph[pos_x][pos_y] = 's' # 뱀의 머리 최신화
        queue.append((pos_x, pos_y)) # 뱀인 곳을 큐에 추가
        tail_x, tail_y = queue.popleft() # 뱀의 꼬리
        graph[tail_x][tail_y] = 0
        
    # 회전 구현
    if cnt in turn:
        if turn[cnt] == 'L':
            dir = (dir - 1) % 4 # 음수여도 출력은 양수로 조정됨
        else:
            dir = (dir + 1) % 4

print(cnt)