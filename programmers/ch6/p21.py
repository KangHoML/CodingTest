def sol(brown, yellow):
    tot = brown + yellow

    for y in range(3, int(tot ** 0.5) + 1):
        if tot % y != 0: continue
        x = tot // y
        if (x - 2) * (y - 2) == yellow: return [x, y]

    return

if __name__ == "__main__":
    brown, yellow = 10, 2
    print(sol(brown, yellow))
