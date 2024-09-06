def permutation(arr, n):
    result = []
    if n == 0: return [[]]

    for i, val in enumerate(arr):
        for j in permutation(arr[:i] + arr[i + 1:], n - 1):
            result.append([val] + j)
    
    return result

def postfix(tokens, priority):
    stack, result = [], []
    
    for token in tokens:
        if token.isdigit(): result.append(token) # 숫자인 경우
        else:
            if not stack: stack.append(token) # 스택이 비어있는 경우 추가
            else:
                while stack:
                    # 우선순위에 따라 스택 비우기
                    if priority[token] <= priority[stack[-1]]:
                        result.append(stack.pop())
                    else:
                        break
                    
                # stack에 추가
                stack.append(token)
    
    # 남은 연산자 결과에 추가
    while stack:
        result.append(stack.pop())

    return result

def calc(tokens):
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
            continue
        
        num1 = stack.pop()
        num2 = stack.pop() # 기존에 더 먼저 있던 숫자

        if token == '+':
            stack.append(num2 + num1)
        elif token == '-':
            stack.append(num2 - num1)
        else:
            stack.append(num2 * num1)
        
    return stack.pop()

def solution(expression):
    tokens = expression.replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').split()
    result = 0
    
    for ops in permutation(['+', '-', '*'], 3):
        priority = {o: p for p, o in enumerate(ops)}
        exp_postfix = postfix(tokens, priority)
        result = max(result, abs(calc(exp_postfix)))

    return result

def calculation(tokens):
    num1, exp, num2 = tokens
    if exp == '+':
        return int(num1) + int(num2)
    elif exp == '-':
        return int(num1) - int(num2)
    else:
        return int(num1) * int(num2)

def solution2(expression):
    result = []
    
    for operator in permutation(['+', '-', '*'], 3):
        tokens = expression.replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').split()
        for exp in operator:
            while exp in tokens:
                idx = tokens.index(exp)
                tokens[idx-1] = str(calculation(tokens[idx-1:idx+2])) # 숫자 + 연산자 + 숫자
                tokens[idx] = tokens[idx+1] = ''
                tokens = [c for c in tokens if c] # 빈 문자 제거
        result.append(abs(int(tokens[0])))

    return max(result)

if __name__ == "__main__":
    print(solution2("100-200*300-500+20"))