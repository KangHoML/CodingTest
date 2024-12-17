def sol(s):
    ln = len(s)
    mn_ln = ln

    for l in range(1, ln//2 + 1):
        idx, cnt = 0, 1
        ln_new = 0

        while(idx < ln - l):
            if s[idx:idx+l] == s[idx+l:idx+2*l]:
                cnt += 1
            else:
                if cnt > 1: ln_new += l + len(str(cnt))
                else: ln_new += l
                cnt = 1
            idx += l

        if cnt > 1: ln_new += l + len(str(cnt))
        else: ln_new += len(s[idx:idx+l])
        
        mn_ln = min(mn_ln, ln_new)
        
    return mn_ln

def sol2(s):
    ans = len_s = len(s)
    
    for l in range(1, len_s//2 + 1):
        prev = ''
        new_len, cnt = 0, 1

        # 마지막 남은 부분까지 비교해주기 위해 len(s)까지 진행
        for i in range(0, len_s + 1, l):
            cur = s[i:i+l]
            
            if cur == prev:
                cnt += 1
            else:
                new_len += len(cur) # 마지막 남은 문자열이 l이 아닐수도 있으므로
                if cnt > 1: new_len += len(str(cnt))
                cnt = 1
                prev = cur
        
        ans = min(ans, new_len)
    
    return ans    

if __name__ == "__main__":
    s = "aabbaccc"
    print(sol2(s))