import re
from itertools import permutations

def dfs(cnt, v, user_id, banned_id):
    global ans

    # 종료 조건
    if cnt == len(banned_id):
        ans.add(v)
        return
    
    # user_id 탐색
    for i in range(len(user_id)):
        print(f'{i}, {cnt}, {bin(v)}')

        # 방문했거나 조건 만족 X
        if v & (1 << i) or not re.fullmatch(banned_id[cnt], user_id[i]): continue

        # 만족하는 경우, 방문처리(비트 마스킹을 통해 백트래킹)
        dfs(cnt + 1, v | (1 << i), user_id, banned_id)

def sol(user_id, banned_id):
    global ans

    # 정규 표현식
    banned_id = [bid.replace('*', '.') for bid in banned_id]
    
    # dfs 방식으로 탐색
    ans = set()
    dfs(0, 0, user_id, banned_id)

    return len(ans)

def sol2(user_id, banned_id):
    ban = ' '.join(banned_id).replace('*', '.')

    # 가능한 모든 user_case에 대해 검사
    ans = set()
    for user_case in permutations(user_id, len(banned_id)):
        if re.fullmatch(ban, ' '.join(user_case)):
            ans.add(' '.join(sorted(user_case)))
    
    return len(ans)

if __name__ == "__main__":
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "abc1**"]
    print(sol2(user_id, banned_id))