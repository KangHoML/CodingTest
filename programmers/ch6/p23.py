import re

def permutation(arr, n):
    result = []
    if n == 0: return [[]]

    for i, num in enumerate(arr):
        for j in permutation(arr[:i] + arr[i+1:], n-1):
            result.append([num]+j)
    
    return result

def check(case, banned_id):
    for uid, bid in zip(case, banned_id):
        if not re.fullmatch(bid, uid): return False
    
    return True

def sol(user_id, banned_id):
    banned_id = [id.replace('*', '.') for id in banned_id]
    answer = []
    
    for c in permutation(user_id, len(banned_id)):
        # 1. user_id로부터 모든 경우의 수 찾아 가능한지 비교
        if not check(c, banned_id): continue

        # 2. 가능한 경우, set으로 바꾸어 answer에 겹치지 않도록 추가
        c = set(c)
        if c not in answer: answer.append(c)
    
    return len(answer)

def sol2(user_id, banned_id):
    # 빈 문자열을 추가하여 겹치는 부분에서 .으로 인한 오류를 방지
    ban = ' '.join(banned_id).replace('*', '.') 

    answer = set()
    for user_case in permutation(user_id, len(banned_id)):
        if re.fullmatch(ban, ' '.join(user_case)):
            # 정렬을 통해 순서로 인한 중복 방지
            answer.add(' '.join(sorted(user_case)))

    return len(answer)

def dfs(idx, v, answer, user_id, banned_id):
    # 종료 조건
    if idx == len(banned_id):
        answer.add(v)
        return
    
    for i in range(len(user_id)):
        # 이미 방문하거나 조건에 맞지 않는 경우
        if v & (1 << i) > 0 or not re.fullmatch(banned_id[idx], user_id[i]): continue
        
        # 백트래킹
        dfs(idx + 1, v | (1 << i), answer, user_id, banned_id)

def sol3(user_id, banned_id):
    answer = set()
    banned_id = [id.replace('*', '.') for id in banned_id]

    dfs(0, 0, answer, user_id, banned_id)
    return len(answer)
    
if __name__ == "__main__":
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "abc1**"]
    print(sol3(user_id, banned_id))
