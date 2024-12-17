def sol(s, n):
    s = list(s)
    for i in range(len(s)):
        if 'a' <= s[i] <= 'z':
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
        elif 'A' <= s[i] <= 'Z':
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
    
    return ''.join(s)

def sol2(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ': continue
        corr = ord('a') if s[i].islower() else ord('A')
        s[i] = chr((ord(s[i]) - corr + n) % 26 + corr)

    return ''.join(s)
        
if __name__ == "__main__":
    s = "AB"
    n = 1
    print(sol2(s, n))