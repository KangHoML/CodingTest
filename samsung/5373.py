import sys
sys.stdin = open("5373.txt", "r")

color = ['w', 'y', 'r', 'o', 'g', 'b']
face = {'U': 1, 'D': 2, 'F': 3, 'B': 4, 'L': 5, 'R': 6}

def turn(f, d):
    # 큐브 복사
    new_cube = {i: cube[i][:] for i in range(1, 7)}
    
    # 회전하는 면 자체의 회전
    if d == '+':
        new_cube[face[f]] = [cube[face[f]][6], cube[face[f]][3], cube[face[f]][0],
                             cube[face[f]][7], cube[face[f]][4], cube[face[f]][1],
                             cube[face[f]][8], cube[face[f]][5], cube[face[f]][2]]
    else:
        new_cube[face[f]] = [cube[face[f]][2], cube[face[f]][5], cube[face[f]][8],
                             cube[face[f]][1], cube[face[f]][4], cube[face[f]][7],
                             cube[face[f]][0], cube[face[f]][3], cube[face[f]][6]]
        
    if f == 'U':
        if d == '+':
            new_cube[4][6], new_cube[4][7], new_cube[4][8] = cube[5][8], cube[5][5], cube[5][2] # 5 -> 4
            new_cube[5][2], new_cube[5][5], new_cube[5][8] = cube[3][0], cube[3][1], cube[3][2] # 3 -> 5
            new_cube[3][0], new_cube[3][1], new_cube[3][2] = cube[6][6], cube[6][3], cube[6][0] # 6 -> 3
            new_cube[6][0], new_cube[6][3], new_cube[6][6] = cube[4][6], cube[4][7], cube[4][8] # 4 -> 6
        else:
            new_cube[5][8], new_cube[5][5], new_cube[5][2] = cube[4][6], cube[4][7], cube[4][8]
            new_cube[3][0], new_cube[3][1], new_cube[3][2] = cube[5][2], cube[5][5], cube[5][8]
            new_cube[6][6], new_cube[6][3], new_cube[6][0] = cube[3][0], cube[3][1], cube[3][2]
            new_cube[4][6], new_cube[4][7], new_cube[4][8] = cube[6][0], cube[6][3], cube[6][6]

    elif f == 'D':
        if d == '+':
            new_cube[3][6], new_cube[3][7], new_cube[3][8] = cube[5][0], cube[5][3], cube[5][6] # 5 -> 3
            new_cube[6][8], new_cube[6][5], new_cube[6][2] = cube[3][6], cube[3][7], cube[3][8] # 3 -> 6
            new_cube[4][0], new_cube[4][1], new_cube[4][2] = cube[6][2], cube[6][5], cube[6][8] # 6 -> 4
            new_cube[5][6], new_cube[5][3], new_cube[5][0] = cube[4][0], cube[4][1], cube[4][2] # 4 -> 5
        else:
            new_cube[5][0], new_cube[5][3], new_cube[5][6] = cube[3][6], cube[3][7], cube[3][8]
            new_cube[3][6], new_cube[3][7], new_cube[3][8] = cube[6][8], cube[6][5], cube[6][2]
            new_cube[6][2], new_cube[6][5], new_cube[6][8] = cube[4][0], cube[4][1], cube[4][2]
            new_cube[4][0], new_cube[4][1], new_cube[4][2] = cube[5][6], cube[5][3], cube[5][0]

    elif f == 'F':
        if d == '+':
            new_cube[1][6], new_cube[1][7], new_cube[1][8] = cube[5][6], cube[5][7], cube[5][8] # 5 -> 1
            new_cube[6][6], new_cube[6][7], new_cube[6][8] = cube[1][6], cube[1][7], cube[1][8] # 1 -> 6
            new_cube[2][0], new_cube[2][1], new_cube[2][2] = cube[6][8], cube[6][7], cube[6][6] # 6 -> 2
            new_cube[5][8], new_cube[5][7], new_cube[5][6] = cube[2][0], cube[2][1], cube[2][2] # 2 -> 5
        else:
            new_cube[5][6], new_cube[5][7], new_cube[5][8] = cube[1][6], cube[1][7], cube[1][8]
            new_cube[1][6], new_cube[1][7], new_cube[1][8] = cube[6][6], cube[6][7], cube[6][8]
            new_cube[6][8], new_cube[6][7], new_cube[6][6] = cube[2][0], cube[2][1], cube[2][2]
            new_cube[2][0], new_cube[2][1], new_cube[2][2] = cube[5][8], cube[5][7], cube[5][6]

    elif f == 'B':
        if d == '+':
            new_cube[2][6], new_cube[2][7], new_cube[2][8] = cube[5][2], cube[5][1], cube[5][0] # 5 -> 2
            new_cube[6][2], new_cube[6][1], new_cube[6][0] = cube[2][6], cube[2][7], cube[2][8] # 2 -> 6
            new_cube[1][0], new_cube[1][1], new_cube[1][2] = cube[6][0], cube[6][1], cube[6][2] # 6 -> 1
            new_cube[5][0], new_cube[5][1], new_cube[5][2] = cube[1][0], cube[1][1], cube[1][2] # 1 -> 5
        else:
            new_cube[5][2], new_cube[5][1], new_cube[5][0] = cube[2][6], cube[2][7], cube[2][8]
            new_cube[2][6], new_cube[2][7], new_cube[2][8] = cube[6][2], cube[6][1], cube[6][0]
            new_cube[6][0], new_cube[6][1], new_cube[6][2] = cube[1][0], cube[1][1], cube[1][2]
            new_cube[1][0], new_cube[1][1], new_cube[1][2] = cube[5][0], cube[5][1], cube[5][2]

    elif f == 'L':
        if d == '+':
            new_cube[4][0], new_cube[4][3], new_cube[4][6] = cube[2][0], cube[2][3], cube[2][6] # 2 -> 4
            new_cube[1][0], new_cube[1][3], new_cube[1][6] = cube[4][0], cube[4][3], cube[4][6] # 4 -> 1
            new_cube[3][6], new_cube[3][3], new_cube[3][0] = cube[1][6], cube[1][3], cube[1][0] # 1 -> 3
            new_cube[2][6], new_cube[2][3], new_cube[2][0] = cube[3][6], cube[3][3], cube[3][0] # 3 -> 2
        else:
            new_cube[2][0], new_cube[2][3], new_cube[2][6] = cube[4][0], cube[4][3], cube[4][6]
            new_cube[4][0], new_cube[4][3], new_cube[4][6] = cube[1][0], cube[1][3], cube[1][6]
            new_cube[1][6], new_cube[1][3], new_cube[1][0] = cube[3][6], cube[3][3], cube[3][0]
            new_cube[3][6], new_cube[3][3], new_cube[3][0] = cube[2][6], cube[2][3], cube[2][0]
    else:
        if d == '+':
            new_cube[4][8], new_cube[4][5], new_cube[4][2] = cube[1][8], cube[1][5], cube[1][2] # 1 -> 4
            new_cube[2][8], new_cube[2][5], new_cube[2][2] = cube[4][8], cube[4][5], cube[4][2] # 4 -> 2
            new_cube[3][2], new_cube[3][5], new_cube[3][8] = cube[2][2], cube[2][5], cube[2][8] # 2 -> 3
            new_cube[1][2], new_cube[1][5], new_cube[1][8] = cube[3][2], cube[3][5], cube[3][8] # 3 -> 1
        else:
            new_cube[1][8], new_cube[1][5], new_cube[1][2] = cube[4][8], cube[4][5], cube[4][2]
            new_cube[4][8], new_cube[4][5], new_cube[4][2] = cube[2][8], cube[2][5], cube[2][2]
            new_cube[2][2], new_cube[2][5], new_cube[2][8] = cube[3][2], cube[3][5], cube[3][8]
            new_cube[3][2], new_cube[3][5], new_cube[3][8] = cube[1][2], cube[1][5], cube[1][8]
    
    return new_cube

for T in range(1, int(input())+1):
    # 입력
    N = int(input())
    clst = []
    for s in input().split():
        clst.append((s[0], s[1]))

    # 큐브 초기화
    cube = {}
    for i in range(1, 7):
        cube[i] = [color[i-1]] * 9
    
    for f, d in clst:
        cube = turn(f, d)
    
    # 출력
    print(f"{T}: ")
    for i in (0, 3, 6):
        print(''.join(cube[1][i:i+3]))