def sol(s):
    words = s.split(' ')
    
    for i in range(len(words)):
        w = list(words[i])
        for j in range(len(w)):
            w[j] = w[j].upper() if j % 2 == 0 else w[j].lower()
        words[i] = ''.join(w)

    return ' '.join(words)

def sol2(s):
    s = list(s)
    cnt = 0

    for i in range(len(s)):
        if s[i] == ' ': cnt = 0; continue
        s[i] = s[i].upper() if cnt % 2 == 0 else s[i].lower()
        cnt += 1
    
    return ''.join(s)

if __name__ == "__main__":
    s = "try hello world"
    print(sol2(s))