import random

def start_game():
    mat = [[0] * 4 for _ in range(4)]
    return mat 

def add_new_2(mat):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        mat[r][c] = 2

def compress(mat):
    changed = False
    new_mat = [[0] * 4 for _ in range(4)]
    
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_mat, changed

def reverse(mat):
    return [row[::-1] for row in mat]

def transpose(mat):
    return [[mat[j][i] for j in range(4)] for i in range(4)]

def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                changed = True
    return mat, changed     

def move_left(grid):
    new_grid, change_1 = compress(grid)
    new_grid, change_2 = merge(new_grid)
    new_grid, _ = compress(new_grid)
    return new_grid, change_1 or change_2

def move_right(grid):
    reverse_grid = reverse(grid)
    new_grid, change_1 = compress(reverse_grid)
    new_grid, change_2 = merge(new_grid)
    new_grid, _ = compress(new_grid)
    final_grid = reverse(new_grid)
    return final_grid, change_1 or change_2

def move_up(grid):
    transpose_grid = transpose(grid)
    new_grid, change_1 = compress(transpose_grid)
    new_grid, change_2 = merge(new_grid)
    new_grid, _ = compress(new_grid)
    final_grid = transpose(new_grid)
    return final_grid, change_1 or change_2

def move_down(grid):
    transpose_grid = transpose(grid)
    reversed_grid = reverse(transpose_grid)
    new_grid, change_1 = compress(reversed_grid)
    new_grid, change_2 = merge(new_grid)
    new_grid, _ = compress(new_grid)
    final_grid = transpose(reverse(new_grid))
    return final_grid, change_1 or change_2

def current_state(mat):
    for row in mat:
        if 2048 in row:
            return "WON"

    for row in mat:
        if 0 in row:
            return "GAME NOT OVER"

    for i in range(4):
        for j in range(3):  # Check horizontal
            if mat[i][j] == mat[i][j + 1]:
                return "GAME NOT OVER"
    
    for j in range(4):
        for i in range(3):  # Check vertical
            if mat[i][j] == mat[i + 1][j]:
                return "GAME NOT OVER"

    return "LOST"
