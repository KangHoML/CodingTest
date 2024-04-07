import sys
import copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 왼쪽
def move_left(board):
    for i in range(n):
        cursor = 0 # 시작 위치
        for j in range(1, n):
            # 옆 칸을 기준으로 비교
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0 # 옆 칸 비우기

                # 현재 칸이 비어있으면 한 칸 이동
                if board[i][cursor] == 0:
                    board[i][cursor] = tmp
                
                # 현재 칸과 같으면 합치기
                elif board[i][cursor] == tmp:
                    board[i][cursor] *= 2
                    cursor += 1
                
                # 현재 칸과 다른 값이면 옆으로 붙임
                else:
                    cursor += 1
                    board[i][cursor] = tmp
    
    return board


# 오른쪽
def move_right(board):
    for i in range(n):
        cursor = n-1 # 시작 위치
        for j in range(n-2, -1, -1):
            # 옆 칸을 기준으로 비교
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0 # 옆 칸 비우기

                # 현재 칸이 비어있으면 한 칸 이동
                if board[i][cursor] == 0:
                    board[i][cursor] = tmp
                
                # 현재 칸과 같으면 합치기
                elif board[i][cursor] == tmp:
                    board[i][cursor] *= 2
                    cursor -= 1
                
                # 현재 칸과 다른 값이면 옆으로 붙임
                else:
                    cursor -= 1
                    board[i][cursor] = tmp
    
    return board

# 위쪽
def move_up(board):
    for j in range(n):
        cursor = 0 # 시작 위치
        for i in range(1, n):
            # 옆 칸을 기준으로 비교
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0 # 옆 칸 비우기

                # 현재 칸이 비어있으면 한 칸 이동
                if board[cursor][j] == 0:
                    board[cursor][j] = tmp
                
                # 현재 칸과 같으면 합치기
                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor += 1
                
                # 현재 칸과 다른 값이면 옆으로 붙임
                else:
                    cursor += 1
                    board[cursor][j] = tmp
    
    return board


# 아래쪽
def move_down(board):
    for j in range(n):
        cursor = n-1 # 시작 위치
        for i in range(n-2, -1, -1):
            # 옆 칸을 기준으로 비교
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0 # 옆 칸 비우기

                # 현재 칸이 비어있으면 한 칸 이동
                if board[cursor][j] == 0:
                    board[cursor][j] = tmp
                
                # 현재 칸과 같으면 합치기
                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor -= 1
                
                # 현재 칸과 다른 값이면 옆으로 붙임
                else:
                    cursor -= 1
                    board[cursor][j] = tmp
    
    return board

# 한 번의 이동마다 상, 하, 좌, 우의 case를 고려하기 때문에 기존의 graph를 copy해서 이용
def dfs(cnt, board):
    global result
    
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                if board[i][j] > result:
                    result = board[i][j]
        return

    for i in range(4):
        copyed = copy.deepcopy(board)
        dfs(cnt + 1, move[i](copyed))

result = 0
move = [move_left, move_right, move_up, move_down]
dfs(0, graph)
print(result)
