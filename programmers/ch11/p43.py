def sol1(prices):
    ans = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            ans[i] += 1
            if prices[j] < prices[i]: break
    
    return ans

def sol2(prices):
    stack = []
    ans = [0] * len(prices)

    # 하락하는 시간을 찾아서 현재 시간과의 차이 계산
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            idx = stack.pop()
            ans[idx] = i - idx
        stack.append(i)

    # 스택 비워주기
    while stack:
        idx = stack.pop()
        ans[idx] = len(prices) - 1 - idx

    return ans

if __name__ == '__main__':
    prices = [1, 2, 3, 2, 3]
    print(sol2(prices))