def sol(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    result = []
    for c in new_id:
        if not (c.isdigit() or c.isalpha() or c == '.' or c == '-' or c == '_'): continue
        result.append(c)

    # 3단계
    result = ''.join(result)
    while '..' in result:
        result = result.replace('..', '.')

    # 4단계
    result = result.strip('.')

    # 5단계
    if not result: result = 'a'

    # 6단계
    if len(result) >= 16: result = result[:15]
    result = result.strip('.')

    # 7단계
    if len(result) <= 2:
        result += (result[-1] * (3 - len(result)))

    return result

if __name__ == '__main__':
    new_id = "abcdefghijklmn.p"
    print(sol(new_id))