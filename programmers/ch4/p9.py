def sol(s):
    s = list(s)
    prev = 0
    
    for i in range(1, len(s)):
        if s[i] == s[prev]:
            s[i], s[prev] = '', ''
            prev = prev - 1 if prev > 0 else 0
        else:
            prev = i
    
    return 1 if ''.join(s) == '' else 0

if __name__ == "__main__":
    s = "aabccbdeed"
    print(sol(s))