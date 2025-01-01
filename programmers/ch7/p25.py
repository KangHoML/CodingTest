def combination(arr, n):
    result = []
    if n == 0: return [0]
    
    for i, num in enumerate(arr):
        for j in combination(arr[i+1:], n-1):
            result.append(num + j)
            
    return result
    
def sol(numbers):
    return sorted(list(set(combination(numbers, 2))))

if __name__ == "__main__":
    numbers = [2,1,3,4,1]
    print(sol(numbers))