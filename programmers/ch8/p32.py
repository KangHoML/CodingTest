def sol(stones, k):
    left, right = 1, max(stones)
    stones.append(right + 1)
    
    while left <= right:
        mid = (left + right) // 2
        
        # mid 명이기 위해 필요한 k
        prev, mx = 0, 0
        for i, s in enumerate(stones):
            # 건널 수 없는 돌 건너뛰기
            if s < mid: continue
            
            # 가지치기
            mx = i + 1 - prev
            if mx > k: break
            
            # 건널 수 있는 이전 돌 갱신
            prev = i + 1
        
        # 이분 탐색
        if mx > k: right = mid - 1
        else: ans = mid; left = mid + 1
    
    return ans

def check(stones, mid, k):
    skip = 0 # 건널 수 없는 돌의 개수
    
    for s in stones:
        if s < mid: skip += 1
        else: skip = 0
        
        # 가지치기
        if skip >= k: return False
    
    return True

def sol2(stones, k):
    left, right = 1, max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        
        # "mid 명일 때, 건널 수 있는가?" 에 대한 이분탐색
        if check(stones, mid, k):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return ans

if __name__ == "__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    print(sol(stones, k))