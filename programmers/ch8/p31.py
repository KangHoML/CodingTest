def check(rocks, mid):
    # mid가 최소가 되기 위해서 필요한 n 계산
    cnt, prev = 0, 0
    
    for rock in rocks:
        if rock - prev < mid: cnt += 1
        else: prev = rock
        
    return cnt

def sol(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    
    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2
        
        # 조건 만족하지 않는 경우
        if check(rocks, mid) > n: right = mid - 1
        # 조건을 만족하는 경우
        else: ans = mid; left = mid + 1

    return ans