def find(result, cur):
    # 종료 조건
    if len(cur) == 6: return
    
    # 사전에 추가
    if cur != '': result.append(cur)

    # 재귀로 반복
    for c in ['A', 'E', 'I', 'O', 'U']:
        find(result, ''.join([cur, c]))

def sol(word):
    result = []
    find(result, '')

    return result.index(word) + 1

if __name__ == "__main__":
    word = "AAAAE"
    print(sol(word))