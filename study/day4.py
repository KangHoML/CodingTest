import sys
sys.stdin = open("day4.txt", "r")

for T in range(1, int(input()) + 1):
    print(f"{T}: ")

    # 입력
    N = int(input())
    lst = list(map(int, input().split()))

    # 투 포인터를 활용한 탐색
    lst.sort()
    
    ans = 0
    for i in range(N):
        # 자기 자신 제외
        tlst = lst[:i] + lst[i+1:]
        l, r = 0, len(tlst) - 1
        
        while l < r:
            # 요구하는 값인 경우
            if tlst[l] + tlst[r] == lst[i]:
                ans += 1
                break
            
            # 더 작은 경우
            elif tlst[l] + tlst[r] < lst[i]:
                l += 1
            
            # 더 큰 경우
            else:
                r -= 1

    print(ans)