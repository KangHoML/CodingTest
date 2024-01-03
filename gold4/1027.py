"""
백준 1027. 고층 건물
가까운 건물부터 기울기를 계산했을 때 이전까지의 최대 기울기보다 크면 count 증가
이때, 주의할 점은 i를 기준으로 i보다 작은 idx와 큰 idx로 나누어 생각
"""

import math

def slope(x1, y1, x2, y2):
    return (y1-y2) / (x1-x2)

def main():
    N = int(input())
    layers = list(map(int, input().split()))
    buildings = []

    for i in range(N):
        count = 0
        
        min_slope = math.inf
        for j in range(i, 0, -1):
            slope_ij = slope(i, layers[i], j-1, layers[j-1])
            if min_slope > slope_ij:
                count += 1
                min_slope = slope_ij

        max_slope = -math.inf
        for j in range(i+1, N):
            slope_ij = slope(i, layers[i], j, layers[j])
            if max_slope < slope_ij:
                count += 1
                max_slope = slope_ij

        buildings.append(count)
    print(max(buildings))
        
if __name__ == "__main__":
    main()