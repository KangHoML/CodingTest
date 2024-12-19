def radixChange(num, radix):
    # 예외처리
    if num == 0: return '0'

    result = []
    while num:
        num, res = divmod(num, radix)
        result.append(str(res))

    return ''.join(reversed(result))

def sol(n):
    return int(radixChange(n, 3)[::-1], 3)

if __name__ == "__main__":
    n = 125
    print(sol(n))