def solution(answers):
    preset = [[1, 2, 3, 4, 5],
              [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer = []
    count = {}
    
    for i in range(3):
        count[i+1] = 0
        for j in range(len(answers)):
            if answers[j] == preset[i][j%len(preset[i])]: count[i+1] += 1
    
    for idx, score in count.items():
        if score == max(count.values()):
            answer.append(idx)
    
    return sorted(answer)

if __name__ == "__main__":
    print(solution([1,3,2,4,2]))