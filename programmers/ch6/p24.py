import re

def permutation(arr, n):
    result = []
    if n == 0: return [[]]

    for i, num in enumerate(arr):
        for j in permutation(arr[:i] + arr[i+1:], n-1):
            result.append([num] + j)
    
    return result

def toPostfix(exp, priority):
    # 연산자 스택 & 출력할 문자열
    stack, postfix = [], [] 

    for c in exp:
        # 피연산자
        if c.isdigit(): postfix.append(c)

        # 연산자
        else:
            while stack:
                # 현재보다 우선인 연산자 먼저 추가
                if priority[stack[-1]] >= priority[c]: postfix.append(stack.pop())
                else: break
            stack.append(c) # 현재 연산자 스택에 추가
    
    # 연산자 스택 비워주기
    while stack: postfix.append(stack.pop())

    return postfix

def calc(postfix):
    stack = [] # 연산 결과를 담을 스택
    
    for c in postfix:
        if c.isdigit(): stack.append(int(c))
        else:
            right, left = stack.pop(), stack.pop()
            
            if c == '+': stack.append(left + right)
            elif c == '-': stack.append(left - right)
            else: stack.append(left * right)

    return stack.pop()

def sol(expression):
    answer = 0

    # 1. 문자열 분할 -> 정규표현식에서 ()를 활용해 구분자 포함
    exp = re.split(r'([+*-])', expression)
    
    # 2. 순열을 통해 가능한 모든 조합에서 탐색
    for comb in permutation(['+', '-', '*'], 3):
        priority = {p: i for i, p in enumerate(comb)}
        postfix = toPostfix(exp, priority)
        answer = max(answer, abs(calc(postfix)))
    
    return answer

def calc2(tokens):
    left, op, right = tokens

    if op == '+': return str(int(left) + int(right))
    elif op == '-': return str(int(left) - int(right))
    else: return str(int(left) * int(right))

def sol2(expression):
    answer = 0

    exp = re.split(r'([+*-])', expression)

    for comb in permutation(['+', '-', '*'], 3):
        tmp = [i for i in exp] # 복사
        for op in comb:
            # 우선순위 연산자부터 먼저 계산
            while op in tmp:
                idx = tmp.index(op)
                tmp[idx-1] = calc2(tmp[idx-1:idx+2]) # 계산하여 앞에다가 넣기
                tmp[idx] = tmp[idx + 1] = '' # 빈 문자열로 대체
                tmp = [i for i in tmp if i] # 빈 문자열 제거
        answer = max(answer, abs(int(tmp[0])))

    return answer

if __name__ == "__main__":
    expression = "100-200*300-500+20"
    print(sol2(expression))