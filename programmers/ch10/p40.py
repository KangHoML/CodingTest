def sol(triangle):
    # 각 위치까지의 최대값을 기록할 배열
    dp = [[0] * len(r) for r in triangle]
    
    # 초기값
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # 맨 왼쪽
            if j == 0: dp[i][j] = dp[i-1][j] + triangle[i][j]
            
            # 맨 오른쪽
            elif j == len(triangle[i]) - 1: dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            
            # 중간
            else: dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    
    return max(dp[-1])

def sol2(triangle):
    # 양끝에 패딩을 추가
    dp = [[0] * (len(r) + 2) for r in triangle]

    # 초기값
    dp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    
    return max(dp[-1])

def sol3(triangle):
    height = len(triangle) - 1

    while height > 0:
        for i in range(height):
            triangle[height-1][i] += max(triangle[height][i], triangle[height][i+1])

    return triangle[0][0]

    