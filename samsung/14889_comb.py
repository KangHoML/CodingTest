import sys
sys.stdin = open("14889.txt", "r")

def combination(arr, k):
    result = []
    if k == 0: return [[]]

    for i, num in enumerate(arr):
        for j in combination(arr[i+1:], k-1):
            result.append([num] + j)
    
    return result

def calc(team1, team2):
    st1 = st2 = 0
    
    for i in range(n//2):
        for j in range(n//2):
            st1 += score[team1[i]][team1[j]]
            st2 += score[team2[i]][team2[j]] 

    return abs(st1 - st2)

for t in range(1, int(input()) + 1):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(n)]
    tlst = list(range(n))

    ans = 1e8
    for c in combination(tlst, n//2):
        team1 = c
        team2 = [p for p in tlst if p not in team1]
        ans = min(ans, calc(team1, team2))
        
    print(f"{t}: {ans}")