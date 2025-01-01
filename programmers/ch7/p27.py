def sol(strings, n):
    # n번째 문자 비교 후, 사전 순 비교
    return sorted(strings, key=lambda x: (x[n], x))

if __name__ == "__main__":
    strings = ["abce", "abcd", "cdx"]
    print(sol(strings, 2))