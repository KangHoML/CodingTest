def solution(arr1, arr2):
    # (n, p) * (p, m) = (n, m)
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)): # n번 반복
        for j in range(len(arr2[0])): # m번 반복
            for k in range(len(arr1[0])): # p만큼 계산
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer

if __name__ == "__main__":
    arr1 = [[1, 4], [3, 2], [4, 1]]
    arr2 = [[3, 3], [3, 3]]
    print(solution(arr1, arr2))