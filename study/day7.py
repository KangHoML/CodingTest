import sys
sys.stdin = open("day7.txt", "r")

#                                21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32
score = list(range(0, 42, 2)) + [13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 0]
graph = [[] for _ in range(33)]

# 시작점 ~ 40
for i in range(0, 20): graph[i].append(i+1)

# 10에서 분기
graph[5].append(21)
graph[21].append(22)
graph[22].append(23)
graph[23].append(29)

# 20에서 분기
graph[10].append(24)
graph[24].append(25)
graph[25].append(29)

# 30에서 분기
graph[15].append(26)
graph[26].append(27)
graph[27].append(28)
graph[28].append(29)

# 25에서 도착
graph[29].append(30)
graph[30].append(31)
graph[31].append(20)
graph[20].append(32)

# 도착점은 자기 자신
graph[32].append(32)

def dfs(cnt, sm):
    global ans
    
    # 종료 조건
    if cnt == 10:
        ans = max(ans, sm)
        return
    
    # 4개의 말 중 하나 선택
    for i in range(4):
        # 현재 위치
        cur = piece[i]

        # 다음 위치
        nxt = graph[cur][-1] # 분기 지점 고려
        for _ in range(dice[cnt] - 1):
            nxt = graph[nxt][0]
    
        # 백트래킹
        if nxt == 32 or (nxt not in piece):
            piece[i] = nxt
            dfs(cnt + 1, sm + score[nxt])
            piece[i] = cur

for T in range(1, int(input()) + 1):
    print(f'{T}: ')
    dice = list(map(int, input().split()))

    ans = 0
    piece = [0] * 4
    dfs(0, 0)

    print(ans)
