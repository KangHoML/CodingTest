def sol(matrix):
    n, m = len(matrix), len(matrix[0])
    ans = 0

    height = [0] * (m + 1)
    for r in matrix:
        # 현재 행에서 가능한 높이 기록
        for i in range(m):
            if r[i] == '0': height[i] = 0
            else: height[i] += 1
        
        # 스택이 비었는지 판단하기 위해 -1로 초기화
        stack = [-1] 

        # height를 순회하며 최댓값 갱신
        for i, h in enumerate(height):
            while stack[-1] != -1 and height[stack[-1]] > h:
                curH = height[stack.pop()]
                curW = i - stack[-1] - 1 # 가장 최근 인덱스보다 하나 뒤
                ans = max(ans, curH * curW)
            stack.append(i)

    return ans

if __name__ == "__main__":
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(sol(matrix))