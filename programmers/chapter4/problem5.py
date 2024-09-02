def solution1(s):
    min_len = len(s)
    stack = []

    for size in range(1, len(s) // 2 + 1): # 절반보다 크면 반복 불가능
        length, cnt = 0, 1
        
        for i in range(0, len(s), size):
            if i + size <= len(s):
                chunk = s[i : i + size] # 현재 chunk
            else:
                chunk = s[i:]

            if not stack:
                stack.append(chunk)
                continue

            if stack[-1] != chunk:
                if cnt == 1: length += len(stack.pop())
                else: length += (len(stack.pop()) + len(str(cnt)))
                cnt = 1
                stack.append(chunk)

            else:
                cnt += 1
        
        # 남은 스택 비워주기
        if stack:
            if cnt == 1: length += len(stack.pop())
            else: length += (len(stack.pop()) + len(str(cnt)))
        
        min_len = min(length, min_len)
    
    return min_len

def solution2(s):
    min_len = len(s)

    for size in range(1, len(s) // 2 + 1):
        length, cnt = 0, 1
        prev = ''

        for i in range(0, len(s) + 1, size): # 마지막 비교 필요
            curr = s[i:i + size]

            if prev != curr:
                length += len(curr)
                if cnt > 1: length += len(str(cnt))
                prev = curr
                cnt = 1
            else:
                cnt += 1

        min_len = min(length, min_len)

    return min_len

if __name__ == "__main__":
    s = "aabbaccc"
    print(solution2(s))