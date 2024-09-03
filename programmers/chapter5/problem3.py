def find(data, s, n):
    # 종료 조건
    if n == 6: return

    # 사전에 현재 문자열 추가
    if s != '': data.append(s)

    # 현재 문자열에 다음 모음을 추가해서 추가
    for c in ['A', 'E', 'I', 'O', 'U']:
        find(data, ''.join([s, c]), n + 1)

def solution(word):
    data = []
    find(data, '', 0)

    for i in range(len(data)):
        if word == data[i]:
            return i + 1
