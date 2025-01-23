def sol(money):
    # 1. 첫번째 집부터 터는 경우
    dp1 = [0] * len(money)
    dp1[0] = dp1[1] = money[0]
    
    # 마지막 집을 털 수 없음
    for i in range(2, len(dp1) - 1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    
    # 2. 두번째 집부터 터는 경우
    dp2 = [0] * len(money)
    dp2[0], dp2[1] = 0, money[1]
    
    # 마지막 집 털 수 있음
    for i in range(2, len(dp2)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    
    return max(dp1[-2], dp2[-1])

if __name__ == '__main__':
    money = [1, 2, 3, 1]
    print(sol(money))