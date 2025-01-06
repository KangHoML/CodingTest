def sol(clothes):
    # 각 카테고리 별 선택하지 않는 옵션 추가
    tbl = {}
    for _, t in clothes: tbl[t] = tbl.get(t, 1) + 1
    
    cnt = 1
    for v in tbl.values(): cnt *= v
    
    return cnt - 1

if __name__ == "__main__":
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(sol(clothes))