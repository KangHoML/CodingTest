def permutation(arr, n):
    result = []
    if n == 0:
        return [0]

    for i, num in enumerate(arr):
        for j in permutation(arr[:i] + arr[i+1:], n-1):
            result.append(num * (10 ** (n-1)) + j)
    
    return result

def is_prime(num):
    if num < 2: return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: return False
    
    return True

def sol(numbers):
    lst = [int(c) for c in numbers]

    cases = set()
    for i in range(1, len(lst) + 1):
        for num in permutation(lst, i):
            cases.add(num)
    
    cnt = 0
    for num in cases:
        if is_prime(num): cnt += 1
    
    return cnt

if __name__ == "__main__":
    numbers = "011"
    print(sol(numbers))