def solution1(s):
    words = []
    for word in s.split(' '):
        word = list(word)
        for i in range(len(word)):
            if i % 2 == 0: word[i] = word[i].upper()
            else: word[i] = word[i].lower()
            
        words.append(word)

    return ' '.join(''.join(word) for word in words)

def solution2(s):
    s = list(s)
    cnt = 0

    for i in range(len(s)):
        if s[i] == ' ':
            cnt = 0
            continue
        s[i] = s[i].upper() if cnt % 2 == 0 else s[i].lower()
        cnt += 1
    
    return ''.join(s)

if __name__ == "__main__":
    s = "try hello world"
    print(solution2(s))