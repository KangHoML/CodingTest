from heapq import heappush, heappop

def sol1(food_times, k):
    # 다 먹는 경우
    if sum(food_times) <= k: return -1

    # 우선순위 큐
    q = []
    for i, v in enumerate(food_times):
        heappush(q, (v, i + 1))
    
    # 초기값
    prev = 0
    n_foods = len(food_times)
    
    # 현재 음식을 다 못 먹는 경우까지
    while (q[0][0] - prev) * n_foods <= k:
        # 현재 음식 시간
        cur, _ = heappop(q)
            
        # 현재 음식 다 먹기
        k -= (cur - prev) * n_foods
        n_foods -= 1
        
        # 이전 음식 먹는데 필요한 시간 업데이트
        prev = cur
        
    # 남은 시간 소모
    lst = sorted(q, key=lambda x: x[1])
    return lst[k % n_foods][1]

def sol2(food_times, k):
    lst = [[i+1, v] for i, v in enumerate(food_times)]
    lst.sort(key=lambda x: x[1])
    
    prev = 0
    n_foods = len(lst)
    
    for i, (_, v) in enumerate(lst):
        # 현재 음식 먹을 수 있는가
        if k < (v - prev) * n_foods:
            lst = lst[i:]
            break
        
        # 현재 음식 먹기
        k -= (v - prev) * n_foods
        n_foods -= 1
        
        # 이전 소요시간 갱신
        prev = v
        
    # 남은 음식 없는 경우
    if n_foods == 0: return -1
    
    # 남은 음식 있는 경우
    lst.sort(key=lambda x: x[0])
    return lst[k % n_foods][0]
    