import re

def sol(phone_number):
    return (len(phone_number) - 4) * '*' + phone_number[-4:]

def sol2(phone_number):
    return re.sub('\d(?=\d{4})', '*', phone_number)

if __name__ == "__main__":
    phone_number = "01033334444"
    print(sol2(phone_number))