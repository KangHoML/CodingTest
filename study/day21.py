def sol(board, skill):
    # 보드 크기
    N, M = len(board), len(board[0])
    
    # 누적 합 배열 초기화
    acc = [[0] * (M + 1) for _ in range(N + 1)]
    
    for t, r1, c1, r2, c2, d in skill:
        num = -d if t == 1 else d
        
        # 누적 합을 위한 값 입력
        acc[r1][c1] += num
        acc[r1][c2 + 1] += -num
        acc[r2 + 1][c1] += -num
        acc[r2 + 1][c2 + 1] += num
    
    # 누적 합(가로)
    for r in range(N + 1):
        for c in range(M):
            acc[r][c + 1] += acc[r][c]
    
    # 누적 합(세로)
    for c in range(M + 1):
        for r in range(N):
            acc[r + 1][c] += acc[r][c]
    
    # 보드 초기 상태와 누적으로 계산한 값을 통해 조건 비교
    ans = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] + acc[r][c] >= 1: ans += 1
    
    return ans

if __name__ == "__main__":
    board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
    skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
    print(sol(board, skill))