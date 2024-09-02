def solution1(s):
    s_list = []
    num = 0

    # 문자열 처리
    for i in range(1, len(s) - 1):
        if s[i] == '{': temp = []
        elif s[i] == '}':
            temp.append(num)
            num = 0
            s_list.append(temp)
        elif s[i] == ',':
            if s[i-1] == '}': continue
            else:
                temp.append(num)
                num = 0
        else:
            num = num * 10 + ord(s[i]) - ord('0')

    s_list.sort(key=lambda x: len(x))
    t_list = []
    for l in s_list:
        for elem in l:
            if not (elem in t_list): t_list.append(elem)

    return t_list
        
def solution2(s):
    s = s[2:-2].split('},{') # 앞에 두 개의 중괄호 제거
    s = sorted(s, key=lambda x: len(x))
    
    answer = {} # dictionary를 사용함으로써 검색 시간을 O(1)로 감소
    for item in s:
        item = list(map(int, item.split(',')))
        for key in item:
            if key not in answer:
                answer[key] = 1

    return list(answer)

if __name__ == "__main__":
    s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
    print(solution2(s))