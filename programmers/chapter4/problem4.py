# 스택 활용
def solution(s):
    stack = []

    for c in s:
        if stack and (stack[-1] == c): stack.pop()
        else: stack.append(c)
    
    return 1 if stack else 0

if __name__ == "__main__":
    s = "baabaa"
    print(solution(s))