def radixChange(num, radix):
    if num == 0: return '0'
    
    formatted_num = []
    while(num):
        num, digit = divmod(num, radix)
        formatted_num.append(str(digit))
    
    return ''.join(reversed(formatted_num))

def solution(n):
    return int(radixChange(n, 3)[::-1], 3)

if __name__ == "__main__":
    n = 45
    print(solution(n))    
