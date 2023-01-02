def create(r,c,val):
    global matrix,row,col
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        row,col = r,c
        current_char = matrix[r][c]
        if current_char == ".":
            matrix[r][c] = val


def update(r,c,val):
    global matrix,row,col
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        row,col = r,c
        current_char = matrix[r][c]
        if current_char.isalnum():
            matrix[r][c] = val


def delete(r,c):
    global matrix,row,col
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        row,col = r,c
        current_char = matrix[r][c]
        if current_char != ".":
            matrix[r][c] = "."


def read(r,c):
    global matrix,row,col
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        row,col = r,c
        current_char = matrix[r][c]
        if current_char.isalnum():
            print(current_char)


matrix_size = 6
matrix = [[x for x in input().split()] for _ in range(matrix_size)]
start_pos = input()
command = input()

row,col = start_pos[1],start_pos[4]
movement = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while command != "Stop":
    command = command.split(", ")
    action,direction = command[0],command[1]
    current_row = int(row)
    current_column = int(col)

    if direction == "left":
        current_row += movement['left'][0]
        current_column += movement['left'][1]
    elif direction == "right":
        current_row += movement['right'][0]
        current_column += movement['right'][1]
    elif direction == "up":
        current_row += movement['up'][0]
        current_column += movement['up'][1]
    elif direction == "down":
        current_row += movement['down'][0]
        current_column += movement['down'][1]

    if action == "Create":
        value = command[2]
        create(current_row,current_column,value)
    elif action == "Update":
        value = command[2]
        update(current_row,current_column,value)
    elif action == "Delete":
        delete(current_row,current_column)
    elif action == "Read":
        read(current_row,current_column)
    command = input()

for x in matrix:
    print(*x,sep=" ")