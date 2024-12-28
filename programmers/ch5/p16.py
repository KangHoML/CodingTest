def collatz(n):
    global cnt

    # 종료 조건
    if n == 1 or cnt >= 500: return

    cnt += 1
    if n % 2 == 0: collatz(n // 2)
    else: collatz(n * 3 + 1)

def sol(n):
    global cnt

    # 1인 경우, 0 반환
    if n == 1: return 0

    # 재귀
    cnt = 0
    collatz(n)

    if cnt >= 500: cnt = -1

    return cnt

def sol2(n):
    if n == 1: return 0

    cnt = 0
    
    while n > 1:
        if n % 2 == 0: n = n // 2
        else: n = n * 3 + 1
        cnt += 1

        if cnt >= 500: cnt = -1; break
    
    return cnt

if __name__ == "__main__":
    n = 6
    print(sol2(n))
    