def solution(s, n):
    answer = ''
    for c in s:
        if c != ' ':
            m = ord('A') if c.isupper() else ord('a') # 최소값 결정
            c = chr((ord(c) + n - m) % 26 + m)
        answer += c

    return answer

if __name__ == '__main__':
    inString = ["AB", "z", "a B z"]
    dis = [1, 1, 4]

    for i in range(len(inString)):
        print(solution(inString[i], dis[i]))