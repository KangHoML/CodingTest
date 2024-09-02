import re

def solution(phone_number):
    return re.sub('[0-9](?=[0-9]{4})', '*', phone_number)

if __name__ == "__main__":
    print(solution("01033334444"))
