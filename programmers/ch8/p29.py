def check(k, times):
    # 임의의 시간 k에 통과한 명수
    cnt = 0
    for t in times: cnt += k // t
    return cnt

def sol(n, times):
    left, right = 1, max(times) * n

    while left < right:
        mid = (left + right) // 2

        # n명 이상을 통과한 시간 찾기
        if n > check(mid, times): left = mid + 1
        else: right = mid

    return left