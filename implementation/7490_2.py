import sys
input = sys.stdin.readline

# n : 최대 길이 / idx : 현재 인덱스 / equation은 operator를 포함한 문자열
def dfs(n, idx, equation):
    if idx == n:
        if eval(equation.replace(' ', '')) == 0:
            result.append(equation)
        return
    
    dfs(n, idx+1, equation + ' ' + str(idx+1))
    dfs(n, idx+1, equation + '+' + str(idx+1))
    dfs(n, idx+1, equation + '-' + str(idx+1))

def main():
    for _ in range(int(input())):
        n = int(input())
        global result
        result = []
        dfs(n, 1, '1')

        for eq in result:
            print(eq)
        print()

if __name__ == '__main__':
    main()
