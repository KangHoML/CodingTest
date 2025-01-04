from functools import cmp_to_key

def sol(numbers):
    numbers = [str(n) for n in numbers]
    numbers.sort(key=lambda x: x * 3, reverse=True)
    
    # 예외처리
    ans = ''.join(numbers)
    if '0' * len(numbers) == ans: return '0'
    
    return ans

def sol2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key= cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True)
    return str(int(''.join(numbers)))

if __name__ == '__main__':
    numbers = [3, 30, 34, 5, 9]
    print(sol(numbers))