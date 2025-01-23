import sys
from collections import defaultdict
sys.stdin = open("day9.txt", "r")

for T in range(1, int(input()) + 1):
    print(f'{T}: ')

    # 입력
    N = int(input())
    slst = list(input() for _ in range(N))

    # 딕셔너리화
    wDict = defaultdict(list)
    for s in slst:
        for i in range(len(s)):
            prefix = ''.join(s[:i + 1])
            wDict[prefix].append(s)
    
    # 정렬
    lst = sorted(wDict.items(), key=lambda x: (-len(x[0]), -len(x[1])))
    for key, value in lst:
        if len(value) < 2: continue

        s, t = value[0], value[1]
        break

    print(f'{s}\n{t}')

        
    