import re
from collections import defaultdict

table = [
    {"cpp": '0', "java": '1', "python": '2', '-': '.'},
    {"backend": '0', "frontend": '1', '-': '.'},
    {"junior": '0', "senior": '1', '-': '.'},
    {"pizza": '0', "chicken": '1', '-': '.'}
]

def bisect(arr, score):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < score: left = mid + 1
        else: right = mid
    
    return left

def sol(info, query):
    info_table = defaultdict(list)
    for i in info:
        line = i.split()
        condition = ''.join([table[0][line[0]], table[1][line[1]], table[2][line[2]], table[3][line[3]]])
        info_table[condition].append(int(line[4]))
    
    # 정렬
    for i in info_table: info_table[i].sort()  
    
    ans = [0] * len(query)
    for i, q in enumerate(query):
        line = q.split()
        qc = ''.join([table[0][line[0]], table[1][line[2]], table[2][line[4]], table[3][line[6]]])
        qs = int(line[7])

        # key와 비교하여 해결
        for key in info_table:
            if re.fullmatch(qc, key):
                ans[i] += (len(info_table[key]) - bisect(info_table[key], qs))
                
    return ans

def combination(arr, n):
    result = []
    if n == 0: return [[]]
    
    for i, num in enumerate(arr):
        for j in combination(arr[i+1:], n-1):
            result.append([num] + j)
        
    return result

def sol2(info, query):
    # 딕셔너리 형태로 각 조건에 맞는 점수 리스트 생성
    info_table = defaultdict(list)
    for i in info:
        ci = i.split()
        si = int(ci.pop())
        info_table[''.join(ci)].append(si)

        for j in range(4):
            cases = combination(ci, j)
            for c in cases:
                info_table[''.join(c)].append(si)
    
    # 정렬
    for i in info_table: info_table[i].sort()

    # query와 비교하며 개수 추가
    ans = []
    for q in query:
        cq = q.split()
        sq = int(cq.pop())
        cq = ''.join(cq)
        cq = cq.replace('and', '').replace(' ', '').replace('-','')
        ans.append(len(info_table[cq]) - bisect(info_table[cq], sq))
    
    return ans
    
if __name__ == "__main__":
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(sol2(info, query)) 
