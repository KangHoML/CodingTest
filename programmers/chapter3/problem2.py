def rotate(x1, y1, x2, y2, board):
    first = board[x1][y1]
    min_value = first

    # 왼쪽
    for i in range(x1, x2):
        board[i][y1] = board[i + 1][y1]
        min_value = min(min_value, board[i + 1][y1])
    
    # 아래쪽
    for i in range(y1, y2):
        board[x2][i] = board[x2][i + 1]
        min_value = min(min_value, board[x2][i + 1])

    # 오른쪽
    for i in range(x2, x1, -1):
        board[i][y2] = board[i - 1][y2]
        min_value = min(min_value, board[i - 1][y2])

    # 위쪽
    for i in range(y2, y1, -1):
        board[x1][i] = board[x1][i - 1]
        min_value = min(min_value, board[x1][i - 1])

    board[x1][y1 + 1] = first
    return min_value

def rotate_slicing(x1, y1, x2, y2, board):
    row1, row2 = board[x1][y1 : y2], board[x2][y1 + 1 : y2 + 1]
    min_value = min(row1 + row2)

    # 왼쪽
    for i in range(x1, x2, 1):
        board[i][y1] = board[i + 1][y1]
        min_value = min(min_value, board[i + 1][y1])
    
    # 오른쪽
    for i in range(x2, x1, -1):
        board[i][y2] = board[i - 1][y2]
        min_value = min(min_value, board[i - 1][y2])
    
    # 위, 아래
    board[x1][y1 + 1 : y2 + 1], board[x2][y1 : y2] = row1, row2

    return min_value

def solution(rows, columns, queries):
    answer = []

    # board 초기화
    board = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]

    for x1, y1, x2, y2 in queries:
        # min_value = rotate(x1 - 1, y1 - 1, x2 - 1, y2 - 1, board)
        min_value = rotate_slicing(x1 - 1, y1 - 1, x2 - 1, y2 - 1, board)
        answer.append(min_value)

    return answer

if __name__ == "__main__":
    rows, columns = 6, 6
    queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]

    print(solution(rows, columns, queries))