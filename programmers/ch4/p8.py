def sol(s):
    elems = s[2:-2].split('},{')
    elems.sort(key=lambda x: len(x))
    
    result = []
    for elem in elems:
        for num in elem.split(','):
            num = int(num)
            if num not in result:
                result.append(num)

    return result

def sol2(s):
    elems = s[2:-2].split('},{')
    elems.sort(key=lambda x: len(x))
    
    result = {}
    for elem in elems:
        for num in elem.split(','):
            num = int(num)
            if num not in result:
                result[num] = 1

    return list(result)

if __name__ == "__main__":
    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    print(sol2(s))
