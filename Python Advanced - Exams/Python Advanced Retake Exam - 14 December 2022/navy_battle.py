def check_location(r,c):
    global step_on_mines,matrix_size,matrix,naval_mines,enemy_killed_counter,row,column
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        location_symbol = matrix[r][c]
        if location_symbol == "*":
            step_on_mines += 1
            if step_on_mines == 3:
                print( f"Mission failed, U-9 disappeared! Last known coordinates [{r}, {c}]!")
                if command == "left" or command == "right" or command == "up" or command == "down":
                    matrix[row][column] = "-"
                    row = r
                    column = c
                    matrix[row][column] = "S"
                for x in range(len(matrix)):
                    print(*matrix[x],sep="")
                return
        elif location_symbol == "C":
            enemy_killed_counter += 1
            if enemy_killed_counter == 3:
                print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                if command == "left" or command == "right" or command == "up" or command == "down":
                    matrix[row][column] = "-"
                    row = r
                    column = c
                    matrix[row][column] = "S"
                for x in range(len(matrix)):
                    print(*matrix[x],sep="")
                return
        if command == "left" or command == "right" or command == "up" or command == "down":
            matrix[row][column] = "-"
            row = r
            column = c
            matrix[row][column] = "S"



matrix_size = int(input())
matrix = [[x for x in input()] for x in range(matrix_size)]

movement = {"up": [-1, 0], "down": [+1, 0], "left": [0, -1], "right": [0, +1]}
row,column = 0,0
naval_mines = 0
step_on_mines = 0
enemy_killed_counter = 0

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == "S":
            row,column = x,y
        elif matrix[x][y] == "*":
            naval_mines += 1

while enemy_killed_counter != 3 and step_on_mines != 3:
    command = input()
    left_row = int(row)
    left_column = int(column)
    if command == "left":
        left_row += movement['left'][0]
        left_column += movement['left'][1]
        check_location(left_row,left_column)
    elif command == "right":
        left_row += movement['right'][0]
        left_column += movement['right'][1]
        check_location(left_row,left_column)
    elif command == "up":
        left_row += movement['up'][0]
        left_column += movement['up'][1]
        check_location(left_row,left_column)
    elif command == "down":
        left_row += movement['down'][0]
        left_column += movement['down'][1]
        check_location(left_row,left_column)