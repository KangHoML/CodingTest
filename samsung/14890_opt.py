import sys
sys.stdin = open("14890.txt", "r")

def is_path(arr, visited):
    cnt = 1

    for i in range(1, n):
        # 동일 높이인 경우
        if arr[i] == arr[i-1]: cnt += 1
        
        # 하나 높은 경우
        elif (arr[i] - arr[i-1] == 1) and cnt >= l and (visited[i-l:i] == [0] * l):
            cnt = 1
            visited[i-l:i] = [1] * l

        # 하나 낮은 경우
        elif arr[i] - arr[i-1] == -1:
            cnt = 1

        # 그외의 경우
        else:
            return False

    return True

for t in range(1, int(input()) + 1):
    n, l = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for _ in range(2):
        for arr in board:
            # 겹침 방지를 위한 배열
            visited = [0] * n

            # 가능한 길인지 체크 (양방향 체크)
            if is_path(arr, visited) and is_path(arr[::-1], visited[::-1]): ans += 1
        
        # 전치 행렬로 전환
        board = list(map(list, zip(*board)))
    
    print(f"#{t}: {ans}")
