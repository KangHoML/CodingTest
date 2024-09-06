def permutation(arr, n):
    result = []

    if n == 0: return [[]]

    for i, num in enumerate(arr):
        for j in permutation(arr[:i] + arr[i+1:], n - 1):
            result.append([num] + j)
    
    return result

def is_prime(num):
    if num < 2: return False

    # 나눠지는 수만 계산
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: return False
    
    return True
    
def solution(numbers):
    answer = 0
    available, answer = [], []

    for i in range(1, len(numbers) + 1):
        available.extend(permutation(list(numbers), i))

    for elem in available:
        num = int(''.join(elem), 10)
        if num not in answer and is_prime(num):
            answer.append(num)

    return len(answer)

if __name__ == "__main__":
    print(solution("011"))