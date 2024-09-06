import re

def permutation(arr, n):
    result = []
    if n == 0: return [[]]

    for i, val in enumerate(arr):
        for j in permutation(arr[:i] + arr[i + 1:], n - 1):
            result.append([val] + j)
    
    return result

def compare(usr, ban):
    if len(usr) != len(ban): return False
    
    for i in range(len(usr)):
        if ban[i] == usr[i] or ban[i] == '*': continue
        return False

    return True
    
def solution(user_id, banned_id):
    all_combinations = permutation(user_id, len(banned_id))
    
    result = set()
    for comb in all_combinations:
        if all(compare(usr, ban) for usr, ban in zip(comb, banned_id)):
            result.add(tuple(sorted(comb)))
            
    return len(result)

def search(idx, visit, usr, result, ban):
    # 모든 ban 조건을 만족한 경우 종료
    if idx == len(ban):
        result.add(format(visit, f'0{len(usr)}b'))
        return
    
    for i in range(len(usr)):
        # 이미 방문했거나 조건에 맞지 않은 경우
        if (visit & (1 << i)) > 0 or not re.fullmatch(ban[idx], usr[i]): continue
        search(idx + 1, visit | (1 << i), usr, result, ban) # 방문 표시

def solution2(user_id, banned_id):
    result = set() # 중복 데이터를 배제하기 위해
    banned_id = [s.replace('*', '.') for s in banned_id] # '.': \n 을 제회한 모든 단일 문자를 의미
    search(0, 0, user_id, result, banned_id) # 비트 마스킹 활용

    return len(result)
    
if __name__ == "__main__":
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["*rodo", "*rodo", "******"]
    print(solution2(user_id, banned_id))