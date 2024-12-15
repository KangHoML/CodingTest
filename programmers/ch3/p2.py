def sol(rows, columns, queries):
    board = [list(range(r * columns + 1, columns * (r + 1) + 1)) for r in range(rows)]
    result = []

    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        st = board[x1][y1]
        min_elem = st

        # left
        for x in range(x1, x2):
            board[x][y1] = board[x+1][y1]
            min_elem = min(board[x][y1], min_elem)
        
        # down
        for y in range(y1, y2):
            board[x2][y] = board[x2][y+1]
            min_elem = min(board[x2][y], min_elem)
        
        # right
        for x in range(x2, x1, -1):
            board[x][y2] = board[x-1][y2]
            min_elem = min(board[x][y2], min_elem)
        
        # up
        for y in range(y2, y1, -1):
            board[x1][y] = board[x1][y-1]
            min_elem = min(board[x1][y], min_elem)

        board[x1][y1+1] = st
        result.append(min_elem)

    return result

# slicing
def sol2(rows, columns, queries):
    board = [[c + 1 + r * columns for c in range(columns)] for r in range(rows)]
    result = []

    for query in queries:
        x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1

        row_up, row_down = board[x1][y1:y2], board[x2][y1+1:y2+1]
        min_value = min(row_up + row_down)

        for x in range(x2, x1, -1):
            board[x][y2] = board[x-1][y2]
            min_value = min(min_value, board[x][y2])
        
        for x in range(x1, x2):
            board[x][y1] = board[x+1][y1]
            min_value = min(min_value, board[x][y1])
        
        board[x1][y1+1:y2+1], board[x2][y1:y2] = row_up, row_down
        result.append(min_value)

    return result

if __name__ == "__main__":
    rows, columns = 6, 6
    queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
    print(sol2(rows, columns, queries))
