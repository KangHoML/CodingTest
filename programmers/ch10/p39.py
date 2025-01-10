def sol(N, number):
    # 계산 결과를 저장할 배열
    dp = [set() for _ in range(9)]

    # i개로 만들 수 있는 조합
    for i in range(1, 9):
        # 1. 이어 붙인 수
        dp[i].add(int(str(N) * i))

        # 2. 이전 개수들로 사칙연산 조합
        for j in range(1, i):
            for v1 in dp[j]:
                for v2 in dp[i-j]:
                    dp[i].add(v1 + v2)
                    dp[i].add(v1 * v2)
                    if v1 - v2 >= 0: dp[i].add(v1 - v2)
                    if v1 != 0 and v2 != 0: dp[i].add(v1 // v2)

        # 3. 조건 확인
        if number in dp[i]: return i

    # 8개 안에서 못 만든 경우 -1 반환
    return -1

if __name__ == "__main__":
    N, number= 5, 12
    print(sol(N, number))