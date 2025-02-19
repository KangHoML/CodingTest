import sys
sys.stdin = open("day23.txt", "r")

def palindrome(s):
    l, r = 0, len(s) - 1

    while l < r:
        
        # 둘이 같다면, 한 칸 이동
        if s[l] == s[r]: l, r = l + 1, r - 1

        # 아닌 경우, 한 문자 제거한 뒤 회문 판단
        else:
            # 오른쪽 제거 후 회문 검사
            if s[l:r] == s[l:r][::-1]: return 1

            # 왼쪽 제거 후 회문 검사
            if s[l+1:r+1] == s[l+1:r+1][::-1]: return 1
            
            # 유사 회문이 아닌 경우
            return 2
    
    # 회문인 경우
    return 0

# 입력
T = int(input())
slst = [input() for _ in range(T)]

for s in slst: print(palindrome(s))
