def sol(s):
    s = list(s)
    prev = 0
    
    for i in range(1, len(s)):
        if s[i] == s[prev]:
            s[i], s[prev] = '', ''
            prev = prev - 1 if prev > 0 else 0
        else:
            prev = i

    new_s = ''.join(s)
    return 1 if len(new_s) == 0 else 0

def sol2(s):
    stack = []
    
    for i in range(len(s)):
        if len(stack) == 0 or s[i] != stack[-1]: stack.append(s[i])
        else: stack.pop()

    return 0 if stack else 1

if __name__ == "__main__":
    s = "abbba"
    print(sol2(s))
    