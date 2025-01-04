def sol(numbers):
    numbers = [str(n) for n in numbers]
    numbers.sort(key=lambda x: x * 3, reverse=True)
    
    # 예외처리
    ans = ''.join(numbers)
    if '0' * len(numbers) == ans: return '0'
    
    return ans

if __name__ == '__main__':
    numbers = [3, 30, 34, 5, 9]
    print(sol(numbers))