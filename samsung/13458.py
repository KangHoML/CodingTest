import sys
sys.stdin = open("13458.txt", "r")

def solution():
    cnt = 0
    
    for i in range(n):
        # [1] 총감독관에 의한 처리
        cnt += 1
        if b >= test[i]: continue

        # [2] 부감독관에 의한 처리
        else:
            res = test[i] - b
            cnt += (res // c)
            if (res % c) > 0: cnt += 1
    
    return cnt

for t in range(1, int(input()) + 1):
    n = int(input())
    test = list(map(int, input().split()))
    b, c = map(int, input().split())
    print(f"#{t}: {solution()}")