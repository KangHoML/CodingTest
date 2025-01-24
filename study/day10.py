INF = int(1e9)

def isNegative():
    dis = [INF] * (N + 1)
    
    dis[1] = 0 # 시작점 1이라 가정
    for i in range(N):
        for s, e, d in graph:
            if dis[s] != INF and dis[e] > dis[s] + d:
                dis[e] = dis[s] + d
                if i == N - 1: return True
    
    return False

def isNegativeWrong():
    dis = [INF] * (N + 1)

    dis[1] = 0 # 시작점 1이라 가정
    for i in range(N - 1):
        for s, e, d in graph:
            if dis[s] != INF and dis[e] > dis[s] + d:
                dis[e] = dis[s] + d
                if i == N - 2: return True
    
    return False

# isNegativeWrong()의 반례
def testCase():
    N, M = 5, 4
    
    # 모든 경로가 최단 경로
    graph = []
    for i in range(N-1, 0, -1):
        graph.append((i, i + 1, -1))

    # 출력
    print(f'{N} {M}')
    for s, e, d in graph:
        print(f'{s} {e} {d}')

    return N, M, graph

N, M, graph = testCase()
ans = isNegative()
wrong = isNegativeWrong()

if not ans and wrong: print('AC')
else: print('WA')


