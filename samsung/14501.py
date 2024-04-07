import sys
from collections import deque
input = sys.stdin.readline

# 입력
n = int(input())
time = []
pay = []
for i in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

# 다이나믹 프로그래밍
dp = [0] * (n+1)

# bottom-up: i번째 날까지 일했을 때 얻을 수 있는 최대 수익
def bottom_up():
    for i in range(n):
        # i번째 날에 상담을 진행했을 때 상담이 가능한 모든 날짜
        for j in range(i + time[i], n+1):
            if dp[j] < dp[i] + pay[i]:
                dp[j] = dp[i] + pay[i]

    print(dp[-1])

def top_down():
    for i in range(n-1, -1, -1):
        # i일에 상담을 했을 때 퇴사일을 넘기면 상담 X
        if i + time[i] > n:
            dp[i] = dp[i+1]
        else:
            # 상담을 할 수 있으면 상담을 하는 것과 안하는 것 중 큰 것 선택
            dp[i] = max(dp[i+1], pay[i] + dp[i+time[i]])
    
    print(dp[0])

# bottom_up()
top_down()
