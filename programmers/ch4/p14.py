import re

def sol(s):
    # 길이
    if not (len(s) == 4 or len(s) == 6): return False
    
    # 숫자
    if not s.isdigit(): return False

    return True

def sol2(s):
    return bool(re.match('^(\d{4}|^\d{6})$', s))

if __name__ == "__main__":
    s = "a234"
    print(sol2(s))