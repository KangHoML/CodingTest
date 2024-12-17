def sol(arr1, arr2):
    result = []
    
    for r in arr1:
        new_r = []
        for c in zip(*arr2):
            v = 0
            for elem1, elem2 in zip(r, c):
                v += elem1 * elem2
            new_r.append(v)
        result.append(new_r)

    return result

def sol2(arr1, arr2):
    # 크기먼저 배정
    result = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    # 값 배정
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                result[i][j] += (arr1[i][k] * arr2[k][j])

    return result

if __name__ == "__main__":
    arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
    arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
    print(sol2(arr1, arr2))
