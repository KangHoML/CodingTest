import sys
input = sys.stdin.readline

def check_win(pieces):
    x_win = False
    o_win = False

    # 가로
    for i in range(3):
        if pieces[i * 3] == pieces[i * 3 + 1] == pieces[i * 3 + 2]:
            if pieces[i * 3] == 'X':
                x_win = True
            elif pieces[i * 3] == 'O':
                o_win = True

    # 세로
    for i in range(3):
        if pieces[i] == pieces[i + 3] == pieces[i + 6]:
            if pieces[i] == 'X':
                x_win = True
            elif pieces[i] == 'O':
                o_win = True

    # 대각선
    if pieces[0] == pieces[4] == pieces[8] or pieces[2] == pieces[4] == pieces[6]:
        if pieces[4] == 'X':
            x_win = True
        elif pieces[4] == 'O':
            o_win = True

    return x_win, o_win
    
# 유효한 결과인지 판단하여 0 or 1 반환
def is_valid(pieces):
    x_count = pieces.count('X')
    o_count = pieces.count('O')
    x_win, o_win = check_win(pieces)

    # 둘 다 이긴 경우
    if x_win and o_win:
        return False
    
    # x가 이긴 경우
    if x_win and x_count != o_count + 1:
        return False
    
    # o가 이긴 경우
    if o_win and x_count != o_count:
        return False
    
    # 비긴 경우
    if not x_win and not o_win and (x_count != 5 or o_count != 4):
        return False
    
    return True

def main():
    game = []
    while True:
        pieces = input()
        if pieces == 'end':
            break
        game.append(pieces)

    for pieces in game:
        if is_valid(pieces):
            print('valid')
        else:
            print('invalid')
            
        
if __name__ == '__main__':
    main()