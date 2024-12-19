def radixChange(num, radix):
    if num == 0: return '0'

    result = []
    while num:
        num, res = divmod(num, radix)
        result.append(str(res))
    
    return ''.join(reversed(result))

def sol(s):
    ans = [0, 0]
    while s != '1':
        zero_cnt = s.count('0')
        ans[0] += 1
        ans[1] += zero_cnt

        new_len = len(s) - zero_cnt
        s = radixChange(new_len, 2)
    
    return ans

if __name__ == '__main__':
    s = "01110"
    print(sol(s))