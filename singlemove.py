def single_move(cube,move):
    if move == "F":
        cube[2][6], cube[2][7], cube[2][8], cube[1][0], cube[1][3], cube[1][6], cube[5][0], cube[5][1], cube[5][2], cube[4][2], cube[4][5], cube[4][8] = cube[4][8], cube[4][5], cube[4][2], cube[2][6], cube[2][7], cube[2][8], cube[1][6], cube[1][3], cube[1][0], cube[5][0], cube[5][1], cube[5][2]
        cube[0][0], cube[0][1], cube[0][2], cube[0][3], cube[0][5], cube[0][6], cube[0][7], cube[0][8] = cube[0][6], cube[0][3], cube[0][0], cube[0][7], cube[0][1], cube[0][8], cube[0][5], cube[0][2]  
    elif move == "F'":
        cube[2][6], cube[2][7], cube[2][8], cube[1][0], cube[1][3], cube[1][6], cube[5][0], cube[5][1], cube[5][2], cube[4][2], cube[4][5], cube[4][8] = cube[1][0], cube[1][3], cube[1][6], cube[5][2], cube[5][1], cube[5][0], cube[4][2], cube[4][5], cube[4][8], cube[2][8], cube[2][7], cube[2][6]
        cube[0][0], cube[0][1], cube[0][2], cube[0][3], cube[0][5], cube[0][6], cube[0][7], cube[0][8] = cube[0][2], cube[0][5], cube[0][8], cube[0][1], cube[0][7], cube[0][0], cube[0][3], cube[0][6]  
    elif move == "F2":
        cube[2][6], cube[2][7], cube[2][8], cube[1][0], cube[1][3], cube[1][6], cube[5][0], cube[5][1], cube[5][2], cube[4][2], cube[4][5], cube[4][8] = cube[5][2], cube[5][1], cube[5][0], cube[4][8], cube[4][5], cube[4][2], cube[2][8], cube[2][7], cube[2][6], cube[1][6], cube[1][3], cube[1][0]
        cube[0][0], cube[0][1], cube[0][2], cube[0][3], cube[0][5], cube[0][6], cube[0][7], cube[0][8] = cube[0][8], cube[0][7], cube[0][6], cube[0][5], cube[0][3], cube[0][2], cube[0][1], cube[0][0]
    elif move == "R":
        cube[2][2], cube[2][5], cube[2][8], cube[3][0], cube[3][3], cube[3][6], cube[5][2], cube[5][5], cube[5][8], cube[0][2], cube[0][5], cube[0][8] = cube[0][2], cube[0][5], cube[0][8], cube[2][8], cube[2][5], cube[2][2], cube[3][6], cube[3][3], cube[3][0], cube[5][2], cube[5][5], cube[5][8]
        cube[1][0], cube[1][1], cube[1][2], cube[1][3], cube[1][5], cube[1][6], cube[1][7], cube[1][8] = cube[1][6], cube[1][3], cube[1][0], cube[1][7], cube[1][1], cube[1][8], cube[1][5], cube[1][2]  
    elif move == "R'":
        cube[2][2], cube[2][5], cube[2][8], cube[3][0], cube[3][3], cube[3][6], cube[5][2], cube[5][5], cube[5][8], cube[0][2], cube[0][5], cube[0][8] = cube[3][6], cube[3][3], cube[3][0], cube[5][8], cube[5][5], cube[5][2], cube[0][2], cube[0][5], cube[0][8], cube[2][2], cube[2][5], cube[2][8]
        cube[1][0], cube[1][1], cube[1][2], cube[1][3], cube[1][5], cube[1][6], cube[1][7], cube[1][8] = cube[1][2], cube[1][5], cube[1][8], cube[1][1], cube[1][7], cube[1][0], cube[1][3], cube[1][6]  
    elif move =="R2":
        cube[2][2], cube[2][5], cube[2][8], cube[3][0], cube[3][3], cube[3][6], cube[5][2], cube[5][5], cube[5][8], cube[0][2], cube[0][5], cube[0][8] = cube[5][2], cube[5][5], cube[5][8], cube[0][8], cube[0][5], cube[0][2], cube[2][2], cube[2][5], cube[2][8], cube[3][6], cube[3][3], cube[3][0]
        cube[1][0], cube[1][1], cube[1][2], cube[1][3], cube[1][5], cube[1][6], cube[1][7], cube[1][8] = cube[1][8], cube[1][7], cube[1][6], cube[1][5], cube[1][3], cube[1][2], cube[1][1], cube[1][0]
    elif move == "U":
        cube[0][0], cube[0][1], cube[0][2], cube[1][0], cube[1][1], cube[1][2], cube[3][0], cube[3][1], cube[3][2], cube[4][0], cube[4][1], cube[4][2] = cube[1][0], cube[1][1], cube[1][2], cube[3][0], cube[3][1], cube[3][2], cube[4][0], cube[4][1], cube[4][2], cube[0][0], cube[0][1], cube[0][2]
        cube[2][0], cube[2][1], cube[2][2], cube[2][3], cube[2][5], cube[2][6], cube[2][7], cube[2][8] = cube[2][6], cube[2][3], cube[2][0], cube[2][7], cube[2][1], cube[2][8], cube[2][5], cube[2][2]  
    elif move == "U'":
        cube[0][0], cube[0][1], cube[0][2], cube[1][0], cube[1][1], cube[1][2], cube[3][0], cube[3][1], cube[3][2], cube[4][0], cube[4][1], cube[4][2] = cube[4][0], cube[4][1], cube[4][2], cube[0][0], cube[0][1], cube[0][2], cube[1][0], cube[1][1], cube[1][2], cube[3][0], cube[3][1], cube[3][2]
        cube[2][0], cube[2][1], cube[2][2], cube[2][3], cube[2][5], cube[2][6], cube[2][7], cube[2][8] = cube[2][2], cube[2][5], cube[2][8], cube[2][1], cube[2][7], cube[2][0], cube[2][3], cube[2][6]  
    elif move == "U2":
        cube[0][0], cube[0][1], cube[0][2], cube[1][0], cube[1][1], cube[1][2], cube[3][0], cube[3][1], cube[3][2], cube[4][0], cube[4][1], cube[4][2] = cube[3][0], cube[3][1], cube[3][2], cube[4][0], cube[4][1], cube[4][2], cube[0][0], cube[0][1], cube[0][2], cube[1][0], cube[1][1], cube[1][2]
        cube[2][0], cube[2][1], cube[2][2], cube[2][3], cube[2][5], cube[2][6], cube[2][7], cube[2][8] = cube[2][8], cube[2][7], cube[2][6], cube[2][5], cube[2][3], cube[2][2], cube[2][1], cube[2][0]
    elif move == "B":
        cube[2][0], cube[2][1], cube[2][2], cube[1][2], cube[1][5], cube[1][8], cube[5][6], cube[5][7], cube[5][8], cube[4][0], cube[4][3], cube[4][6] = cube[1][2], cube[1][5], cube[1][8], cube[5][8], cube[5][7], cube[5][6], cube[4][0], cube[4][3], cube[4][6], cube[2][2], cube[2][1], cube[2][0]
        cube[3][0], cube[3][1], cube[3][2], cube[3][3], cube[3][5], cube[3][6], cube[3][7], cube[3][8] = cube[3][6], cube[3][3], cube[3][0], cube[3][7], cube[3][1], cube[3][8], cube[3][5], cube[3][2]  
    elif move == "B'":
        cube[2][0], cube[2][1], cube[2][2], cube[1][2], cube[1][5], cube[1][8], cube[5][6], cube[5][7], cube[5][8], cube[4][0], cube[4][3], cube[4][6] = cube[4][0], cube[4][3], cube[4][6], cube[2][0], cube[2][1], cube[2][2], cube[1][8], cube[1][5], cube[1][2], cube[5][6], cube[5][7], cube[5][8]
        cube[3][0], cube[3][1], cube[3][2], cube[3][3], cube[3][5], cube[3][6], cube[3][7], cube[3][8] = cube[3][2], cube[3][5], cube[3][8], cube[3][1], cube[3][7], cube[3][0], cube[3][3], cube[3][6]  
    elif move == "B2":
        cube[2][0], cube[2][1], cube[2][2], cube[1][2], cube[1][5], cube[1][8], cube[5][6], cube[5][7], cube[5][8], cube[4][0], cube[4][3], cube[4][6] = cube[5][8], cube[5][7], cube[5][6], cube[4][6], cube[4][3], cube[4][0], cube[2][2], cube[2][1], cube[2][0], cube[1][8], cube[1][5], cube[1][2]
        cube[3][0], cube[3][1], cube[3][2], cube[3][3], cube[3][5], cube[3][6], cube[3][7], cube[3][8] = cube[3][8], cube[3][7], cube[3][6], cube[3][5], cube[3][3], cube[3][2], cube[3][1], cube[3][0]
    elif move == "L":
        cube[2][0], cube[2][3], cube[2][6], cube[3][2], cube[3][5], cube[3][8], cube[5][0], cube[5][3], cube[5][6], cube[0][0], cube[0][3], cube[0][6] = cube[3][8], cube[3][5], cube[3][2], cube[5][6], cube[5][3], cube[5][0], cube[0][0], cube[0][3], cube[0][6], cube[2][0], cube[2][3], cube[2][6]
        cube[4][0], cube[4][1], cube[4][2], cube[4][3], cube[4][5], cube[4][6], cube[4][7], cube[4][8] = cube[4][6], cube[4][3], cube[4][0], cube[4][7], cube[4][1], cube[4][8], cube[4][5], cube[4][2]  
    elif move == "L'":
        cube[2][0], cube[2][3], cube[2][6], cube[3][2], cube[3][5], cube[3][8], cube[5][0], cube[5][3], cube[5][6], cube[0][0], cube[0][3], cube[0][6] = cube[0][0], cube[0][3], cube[0][6], cube[2][6], cube[2][3], cube[2][0], cube[3][8], cube[3][5], cube[3][2], cube[5][0], cube[5][3], cube[5][6]
        cube[4][0], cube[4][1], cube[4][2], cube[4][3], cube[4][5], cube[4][6], cube[4][7], cube[4][8] = cube[4][2], cube[4][5], cube[4][8], cube[4][1], cube[4][7], cube[4][0], cube[4][3], cube[4][6]  
    elif move == "L2":
        cube[2][0], cube[2][3], cube[2][6], cube[3][2], cube[3][5], cube[3][8], cube[5][0], cube[5][3], cube[5][6], cube[0][0], cube[0][3], cube[0][6] = cube[5][0], cube[5][3], cube[5][6], cube[0][6], cube[0][3], cube[0][0], cube[2][0], cube[2][3], cube[2][6], cube[3][8], cube[3][5], cube[3][2]
        cube[4][0], cube[4][1], cube[4][2], cube[4][3], cube[4][5], cube[4][6], cube[4][7], cube[4][8] = cube[4][8], cube[4][7], cube[4][6], cube[4][5], cube[4][3], cube[4][2], cube[4][1], cube[4][0]
    elif move == "D":
        cube[0][6], cube[0][7], cube[0][8], cube[1][6], cube[1][7], cube[1][8], cube[3][6], cube[3][7], cube[3][8], cube[4][6], cube[4][7], cube[4][8] = cube[4][6], cube[4][7], cube[4][8], cube[0][6], cube[0][7], cube[0][8], cube[1][6], cube[1][7], cube[1][8], cube[3][6], cube[3][7], cube[3][8]
        cube[5][0], cube[5][1], cube[5][2], cube[5][3], cube[5][5], cube[5][6], cube[5][7], cube[5][8] = cube[5][6], cube[5][3], cube[5][0], cube[5][7], cube[5][1], cube[5][8], cube[5][5], cube[5][2]  
    elif move == "D'":
        cube[0][6], cube[0][7], cube[0][8], cube[1][6], cube[1][7], cube[1][8], cube[3][6], cube[3][7], cube[3][8], cube[4][6], cube[4][7], cube[4][8] = cube[1][6], cube[1][7], cube[1][8], cube[3][6], cube[3][7], cube[3][8], cube[4][6], cube[4][7], cube[4][8], cube[0][6], cube[0][7], cube[0][8]
        cube[5][0], cube[5][1], cube[5][2], cube[5][3], cube[5][5], cube[5][6], cube[5][7], cube[5][8] = cube[5][2], cube[5][5], cube[5][8], cube[5][1], cube[5][7], cube[5][0], cube[5][3], cube[5][6]  
    elif move == "D2":
        cube[0][6], cube[0][7], cube[0][8], cube[1][6], cube[1][7], cube[1][8], cube[3][6], cube[3][7], cube[3][8], cube[4][6], cube[4][7], cube[4][8] = cube[3][6], cube[3][7], cube[3][8], cube[4][6], cube[4][7], cube[4][8], cube[0][6], cube[0][7], cube[0][8], cube[1][6], cube[1][7], cube[1][8]
        cube[5][0], cube[5][1], cube[5][2], cube[5][3], cube[5][5], cube[5][6], cube[5][7], cube[5][8] = cube[5][8], cube[5][7], cube[5][6], cube[5][5], cube[5][3], cube[5][2], cube[5][1], cube[5][0]
    elif move == "M":
        cube[2][1], cube[2][4], cube[2][7], cube[3][1], cube[3][4], cube[3][7], cube[5][1], cube[5][4], cube[5][7], cube[0][1], cube[0][4], cube[0][7] = cube[3][7], cube[3][4], cube[3][1], cube[5][7], cube[5][4], cube[5][1], cube[0][1], cube[0][4], cube[0][7], cube[2][1], cube[2][4], cube[2][7]
    elif move == "M'":
        cube[2][1], cube[2][4], cube[2][7], cube[3][1], cube[3][4], cube[3][7], cube[5][1], cube[5][4], cube[5][7], cube[0][1], cube[0][4], cube[0][7] = cube[0][1], cube[0][4], cube[0][7], cube[2][7], cube[2][4], cube[2][1], cube[3][7], cube[3][4], cube[3][1], cube[5][1], cube[5][4], cube[5][7]
    elif move == "M2":
        cube[2][1], cube[2][4], cube[2][7], cube[3][1], cube[3][4], cube[3][7], cube[5][1], cube[5][4], cube[5][7], cube[0][1], cube[0][4], cube[0][7] = cube[5][1], cube[5][4], cube[5][7], cube[0][7], cube[0][4], cube[0][1], cube[2][1], cube[2][4], cube[2][7], cube[3][7], cube[3][4], cube[3][1]
    elif move == "S2":
        cube[2][3], cube[2][4], cube[2][5], cube[1][1], cube[1][4], cube[1][7], cube[5][3], cube[5][4], cube[5][5], cube[4][1], cube[4][4], cube[4][7] = cube[5][5], cube[5][4], cube[5][3], cube[4][7], cube[4][4], cube[4][1], cube[2][5], cube[2][4], cube[2][3], cube[1][7], cube[1][4], cube[1][1]
def moves(cube,moves):
    for move in moves:
        single_move(cube,move)