def main():
    n, m, k = map(int, input().split())
    team = 0

    while True:
        n -= 2
        m -= 1
        if n < 0 or m < 0 or (n + m) < k:
            break
        team += 1

    print(team)

if __name__ == "__main__":
    main()