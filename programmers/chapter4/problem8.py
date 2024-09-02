def solution(new_id: str) -> str:
    # 소문자
    id = new_id.lower()

    # 불가능 문자 제거
    id = ''.join([c for c in id if c.isdigit() or c.isalpha() or c in ['-', '.', '_']])

    # 연속된 . 하나로
    while '..' in id: id = id.replace('..', '.')
    
    # 처음 or 마지막 '.' 제거
    id = id.strip('.')
    
    # 빈 문자열
    if len(id) == 0: id = 'a'

    # 길이 초과
    id = id[:15]
    if id.endswith('.'): id = id[:-1]
    
    # 길이 부족
    while len(id) < 3: id += id[-1]

    return id

if __name__ == '__main__':
    new_id = ""
    print(solution(new_id))
