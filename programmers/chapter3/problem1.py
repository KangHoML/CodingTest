def solution(line):
    answer, meet = [], []
    
    x_min = y_min = int(10e9)
    x_max = y_max = -int(10e9)

    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]

            div = a * d - b * c
            if div == 0: continue
            x = (b * f - e * d) / div
            y = (e * c - a * f) / div

            if x.is_integer() and y.is_integer():
                x, y = int(x), int(y)
                meet.append([x, y])

                if x_min > x : x_min = x
                if y_min > y : y_min = y
                if x_max < x : x_max = x
                if y_max < y : y_max = y

    board = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]
    for x, y in meet:
        board[y_max - y][x - x_min] = '*'

    for r in board:
        answer.append(''.join(r)) # + 연산자를 사용하는 경우, 추가 비용 발생

    return answer

if __name__ == "__main__":
    line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
    answer = solution(line)

    for line in answer:
        print(line)

