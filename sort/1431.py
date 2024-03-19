import sys
input = sys.stdin.readline

def sum_num(serial_number):
    sum = 0
    for i in range(len(serial_number)):
        if serial_number[i] >= '0' and serial_number[i] <= '9':
            sum += (int)(serial_number[i])
    return sum

def compare_ascii(serial_number_i, serial_number_j):
    for c_i, c_j in zip(serial_number_i, serial_number_j):
        if c_i > c_j:
            return 1
        elif c_i < c_j:
            return 0

def sol1():
    n = int(input())
    serial_list = [input().strip() for _ in range(n)]

    serial_list.sort(key = lambda x: (len(x), sum_num(x), x))
    
    for serial_number in serial_list:
        print(serial_number)

def sol2():
    n = int(input())
    serial_list = [input().strip() for _ in range(n)]

    for i in range(n-1):
        for j in range(i+1, n):
            if len(serial_list[i]) > len(serial_list[j]):
                serial_list[i], serial_list[j] = serial_list[j], serial_list[i]
            
            elif len(serial_list[i]) == len(serial_list[j]):
                if sum_num(serial_list[i]) > sum_num(serial_list[j]):
                    serial_list[i], serial_list[j] = serial_list[j], serial_list[i]
                
                elif sum_num(serial_list[i]) == sum_num(serial_list[j]):
                    if compare_ascii(serial_list[i], serial_list[j]) == 1:
                        serial_list[i], serial_list[j] = serial_list[j], serial_list[i]

    for serial_number in serial_list:
        print(serial_number)

if __name__ == "__main__":
    sol1()