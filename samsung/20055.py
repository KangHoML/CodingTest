import sys
sys.stdin = open("20055.txt", "r")

for TC in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    life = list(map(int, input().split()))
    robot = [0] * N
    LEN = 2 * N

    ans = 0
    while True:
        ans += 1

        # 1. 내구도 한칸씩 회전
        life[1:LEN], life[0] = life[0:LEN - 1], life[LEN - 1]
        robot[1: N-1], robot[0] = robot[0: N-2], 0

        # 2. 로봇 이동
        for i in range(N-2, -1, -1):
            if robot[i] == 1 and robot[i+1] == 0 and life[i+1] > 0:
                robot[i] = 0
                robot[i+1] = 1 if i+1 != N-1 else 0
                life[i+1] -= 1

        # 새로운 로봇 올리기
        if life[0] > 0:
            robot[0] = 1
            life[0] -= 1
        
        # K개 이상인 경우 종료
        if life.count(0) >= K: break

    print(f"{TC}: {ans}")