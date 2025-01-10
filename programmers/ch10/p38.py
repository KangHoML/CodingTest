def sol(n):
    fibo = [0] * n
    fibo[0] = fibo[1] = 1
    
    for i in range(2, n):
        fibo[i] = fibo[i-1] + fibo[i-2]
    
    return fibo[-1] % 1234567

def sol2(n):
    prev, curr = 0, 1

    for _ in range(n):
        prev, curr = curr, prev + curr
    
    return prev % 1234567

if __name__ == "__main__":
    n = 5
    print(sol(n))