def main():
    n, k = map(int, input().split())
    coin = list(int(input()) for i in range(n))
    count = 0

    for i in range(0, n):
        if k == 0:
            break

        if k >= coin[n - 1 - i]:
            count += k // coin[n - 1 - i]
            k = k % coin[n - 1 - i]
            
    print(count)

if __name__ == "__main__":
    main()
    