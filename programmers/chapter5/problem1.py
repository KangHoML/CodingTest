def collatz(n, ans):
    # 종료 조건
    if n == 1: return ans
    if ans >= 500: return -1

    if n % 2 == 0: n //= 2
    else: n = n * 3 + 1

    # 반복 호출
    return collatz(n, ans+1)
    
def solution(num):
    return collatz(num, 0)
    
if __name__ == "__main__":
    print(solution(6))