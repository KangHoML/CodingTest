import re

def solution1(s):
    answer = True

    if len(s) != 4 and len(s) != 6:
        answer = False
    
    for c in s:
        if not c.isdigit():
            answer = False
    
    return answer

def solution2(s):
    return len(s) in {4, 6} and bool(re.match('^[0-9]*$', s))

if __name__ == "__main__":
    print(solution2("1234"))
