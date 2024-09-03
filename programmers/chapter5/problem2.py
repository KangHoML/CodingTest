# 작은 문제로 쪼개서 풀기
def hanoi(n, start, mid, end, ans):
    # 종료 조건
    if n == 1: return ans.append([start, end])

    hanoi(n-1, start, end, mid, ans) # start의 n-1개를 mid로 옮기기
    ans.append([start, end]) # 가장 큰 원판 옮기기
    hanoi(n-1, mid, start, end, ans) # mid의 n-1개를 end로 옮기기

def solution(n):
    ans = []
    hanoi(n, 1, 2, 3, ans)
    return ans

if __name__ == "__main__":
    print(solution(3))