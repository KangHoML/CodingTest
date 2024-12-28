def sol(answers):
    result = [0, 0, 0]
    pattern = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    for i, num in enumerate(answers):
        if num == pattern[0][i%5]: result[0] += 1
        if num == pattern[1][i%8]: result[1] += 1
        if num == pattern[2][i%10]: result[2] += 1
    
    mx = max(result)
    ans = []
    for i, num in enumerate(result):
        if num == mx: ans.append(i+1)
    
    return ans

if __name__ == "__main__":
    answers = [1,2,3,4,5]
    print(sol(answers))