def sol(line):
    cross_points = set()
    min_cx = min_cy = 1e10
    max_cx = max_cy = -1e10

    for i in range(len(line)-1):
        a, b, c = line[i]
        for j in range(i+1, len(line)):
            d, e, f = line[j]
            
            div = b * d - a * e
            if div == 0: continue
            
            cx = (e * c - b * f) / div
            cy = (a * f - c * d) / div
            if int(cx) != cx or int(cy) != cy: continue
            
            cx, cy = int(cx), int(cy)        
            cross_points.add((cx, cy))
            min_cx, max_cx = min(cx, min_cx), max(cx, max_cx)
            min_cy, max_cy = min(cy, min_cy), max(cy, max_cy)
    
    board = [['.'] * (max_cx - min_cx + 1) for _ in range(max_cy - min_cy + 1)]
    for cx, cy in cross_points:
        board[max_cy - cy][cx - min_cx] = '*'

    return [''.join(r) for r in board]

if __name__ == '__main__':
    line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
    print(sol(line))