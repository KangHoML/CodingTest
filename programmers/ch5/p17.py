def hanoi(n, start, mid, end):
    global ans

    # 종료 조건
    if n < 1: return

    hanoi(n-1, start, end, mid) # n-1개 원판 옮기기
    ans.append([start, end]) # 제일 큰 원판 옮기기
    hanoi(n-1, mid, start, end) # 옮겨졌던 n-1개 원판 다시 옮기기

def sol(n):
    global ans
    
    ans = []
    hanoi(n, 1, 2, 3)

    return ans

if __name__ == "__main__":
    n = 3
    print(sol(n))