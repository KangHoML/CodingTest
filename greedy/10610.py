def main():
    num = list(input())
    num = sorted(num, reverse=True) # 내림차순으로 정렬

    if '0' not in num:
        print(-1)

    else:
        sum = 0
        for i in num:
            sum += int(i)
        
        if sum % 3 != 0:
            print(-1)
        else:
            print("".join(num)) # 리스트를 하나의 문자열로 합쳐서 반환
    
if __name__ == "__main__":
    main()