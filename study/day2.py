from collections import defaultdict

def bisect_left(lst, key):
    l, r = 0, len(lst)

    while l < r:
        mid = (l + r) // 2

        if lst[mid] >= key:
            r = mid
        else:
            l = mid + 1
    
    return l

def bisect_right(lst, key):
    l, r = 0, len(lst)

    while l < r:
        mid = (l + r) // 2

        if lst[mid] <= key:
            l = mid + 1
        else:
            r = mid
    
    return l

def sol1(words, queries):
    answer = [0] * len(queries)

    # 1. words를 각 길이별로 딕셔너리 생성
    wDict, rwDict = defaultdict(list), defaultdict(list)
    for w in words:
        wDict[len(w)].append(w)
        rwDict[len(w)].append(w[::-1])
    
    # 2. 딕셔너리의 각 리스트 정렬
    for w in wDict.values(): w.sort()
    for w in rwDict.values(): w.sort()

    # 3. 각 query에 따라 lower bound와 upper bound를 활용해 계산
    for i, q in enumerate(queries):
        if q.startswith('?'):
            lower = bisect_left(rwDict[len(q)], q[::-1].replace('?', 'a'))
            upper = bisect_right(rwDict[len(q)], q[::-1].replace('?', 'z'))
        else:
            lower = bisect_left(wDict[len(q)], q.replace('?', 'a'))
            upper = bisect_right(wDict[len(q)], q.replace('?', 'z'))
        
        answer[i] = upper - lower

    return answer

class Trie:
    def __init__(self):
        self.child = dict() # a ~ z에 해당하는 자식 노드
        self.count = 0      # 문자열 길이

    def insert(self, s):
        # 현재 노드
        cur = self
        
        # 문자열의 문자를 하나씩 탐색
        for c in s:
            cur.count += 1

            if c not in cur.child:
                cur.child[c] = Trie() # 새로운 노드 생성
            cur = cur.child[c]
        
        # 마지막 문자
        cur.count += 1
    
    def search(self, s):
        # 현재 문자
        cur = self

        # 문자열의 문자를 하나씩 탐색
        for c in s:
            if c == '?': return cur.count

            elif c not in cur.child: return 0
            
            cur = cur.child[c]
        
        return cur.count
    
def sol2(words, queries):
    answer = [0] * len(queries)

    # 1. 문자열의 길이 별로 Tire 인스턴스 객체를 생성
    wDict, rwDict = defaultdict(Trie), defaultdict(Trie)
    
    # 2. 각 단어별로 Trie() 자료구조에 추가
    for w in words:
        wDict[len(w)].insert(w)
        rwDict[len(w)].insert(w[::-1])

    # 3. Trie() 자료구조에서 탐색 수행
    for i, q in enumerate(queries):
        if q.startswith('?'): answer[i] = rwDict[len(q)].search(q[::-1])
        else: answer[i] = wDict[len(q)].search(q)

    return answer

if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    print(sol2(words, queries))