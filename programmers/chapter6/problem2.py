def solution(brown, yellow):
    div = []
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            div.append([i, yellow // i])

    for x, y in div:
        if (x + 2) * (y + 2) == (brown + yellow) and x >= y:
            return [x+2, y+2]

if __name__ == "__main__":
    print(solution(8, 1))
            
