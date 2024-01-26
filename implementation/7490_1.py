import sys
from itertools import product

input = sys.stdin.readline

def main():
    result = []
    for _ in range(int(input())):
        n = int(input())
        
        equations = [] # 각 case에 대해 합이 0인 equation을 저장할 배열
        for op in product([' ', '+', '-'], repeat=n-1):
            num = 1
            expression = '1' # 문자열로 표현된 식
            for i in op:
                num += 1
                expression += i + str(num)

            if eval(expression.replace(' ', '')) == 0: # eval함수를 통해 문자열 식이 0인지 계산
                equations.append(expression)
    
        result.append(sorted(equations)) # ASCII 문자열 순을 위해 정렬 후 추가

    for eqs in result:
        for eq in eqs:
            print(eq)
        print()
        
if __name__ == "__main__":
    main()