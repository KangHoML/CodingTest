def radixChange(num: int, radix: int) -> str:
    formatted_num =[]
    while(num):
        num, digit = divmod(num, radix)
        formatted_num.append(str(digit))

    return ''.join(reversed(formatted_num))
    
def solution(s: str) -> list:
    cnt_time, cnt_zero = 0, 0
    x = s

    while x != '1':
        removed_0 = [c for c in x if c != '0'] # '0' 제거
        cnt_zero += (len(x) - len(removed_0)) # 제거된 0 개수
        x = radixChange(len(removed_0), 2) # 이진 변환
        cnt_time += 1
        
    return [cnt_time, cnt_zero]

def solution2(s: str) -> list:
    cnt_time, cnt_zero = 0, 0

    while(len(s) > 1):
        cnt_time += 1

        num = s.count('1') # 0이 제거된 문자열의 길이
        cnt_zero += len(s) - num # 제거된 0 개수

        s = bin(num)[2:] # 0b로 반환되기 때문에 앞의 두 개 문자 제외
    
    return [cnt_time, cnt_zero]

if __name__ == "__main__":
    s = "1111111"
    print(solution2(s))
