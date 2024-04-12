# 입력
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
command = [tuple(map(int, input().split())) for _ in range(M)]

# 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 순서 (좌, 하, 우, 상)
mvx = [0, 1, 0, -1]
mvy = [-1, 0, 1, 0]

# 2차원 달팽이를 1차원 리스트로 변환 (달팽이 함수 기억해두기)
pos = []
cx, cy, dir = N//2, N//2, 0
cnt = 1

# 최종적으로 (0, 0)의 위치에 도달하게 되면 종료
while True:
    if cx == 0 and cy == 0:
        break
    for _ in range(cnt):
        cx += mvx[dir]
        cy += mvy[dir]
        pos.append((cx, cy))

    # 두번마다 한번씩 바뀌므로 cnt가 원하는 값이 될때까지 cnt 증가
    if dir % 2 == 1 and cnt != (N-1):
        cnt += 1
    dir = (dir + 1) % 4

# 폭발 후 점수 추가 나머지 반환
def explode(m_lst):
    global result
    temp = [] # 리턴 시 사용
    m_lst.append(-1) # 마지막 인덱스 체크를 위한 패딩
    
    i = 0
    while i < len(m_lst) - 1:
        j = i + 1

        while m_lst[i] == m_lst[j]:
            j += 1

        # 개수가 4보다 많다면
        if (j-i) >= 4:
            result += m_lst[i] * (j-i)

        # 적다면
        else:
            temp += [m_lst[i]] * (j-i) # 해당 개수만큼 반환할 리스트에 추가
        
        i = j
    
    m_lst.pop() # -1 패딩해준 것 제외
    return temp 

result = 0
for d, s in command:
    cx, cy = N//2, N//2

    # blizzard 마법 수행
    for _ in range(s):
        cx += dx[d-1]
        cy += dy[d-1]
        graph[cx][cy] = 0

    # 1 차원 list로 저장 (0이 아닌 실제 구슬만 담기)
    m_lst = []
    for i, j in pos:
        if graph[i][j] > 0:
            m_lst.append(graph[i][j])

    # 4개 이상 폭발 후 이동
    while True:
        temp = explode(m_lst)
        
        # 폭발 전후 list의 크기가 같다면 break
        if len(temp) == len(m_lst):
            break
        
        # 폭발 이후 list 최신화
        m_lst = temp
    
    # 변환 (1차원 리스트에서 연속된 것들의 개수 세는 알고리즘 기억)
    i = 0
    m_lst = []
    temp.append(-1) # 마지막 값을 확인하기 위해서
    while i < len(temp)-1:
        j = i + 1
        while temp[i] == temp[j]:
            j += 1

        m_lst += [j-i, temp[i]]
        i = j # 다음 번호 갱신 
    
    # 1차원 리스트를 다시 2차원으로 만들어주기
    graph = [[0] * N for _ in range(N)]
    
    # 둘 중 더 작은 값에
    for i in range(min(len(m_lst), len(pos))):
        graph[pos[i][0]][pos[i][1]] = m_lst[i]

print(result)
