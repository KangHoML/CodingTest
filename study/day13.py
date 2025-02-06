from collections import Counter

def sol(a):    
    # 모든 원소의 등장 개수
    elems = Counter(a)
    
    ans = 0
    for elem in elems.keys():
        # 최대 길이가 갱신되지 않는 경우 
        if elems[elem] * 2 <= ans: continue
        
        # 스타 수열의 길이
        i, cnt = 0, 0
        while i < len(a) - 1:
            # 조건에 만족하지 않는 경우, 한 칸 이동
            if (a[i] != elem and a[i+1] != elem) or (a[i] == a[i+1]):
                i += 1
                continue
                
            # 조건에 만족하는 경우, 두 칸 이동
            cnt += 2
            i += 2
        
        # 최대값 갱신
        ans = max(ans, cnt)
    
    return ans