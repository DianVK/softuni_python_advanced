def check_location(r,c):
    global coals_counter
    global row
    global column
    global matrix
    global end_reached
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        location_symbol = matrix[r][c]
        if location_symbol == "c":
            coals_counter += 1
            if coals_counter == coals_count:
                print(f"You collected all coal! ({row}, {column})")
                exit()
        elif location_symbol == "e":
            print(f"Game over! ({row}, {column})")
            exit()
        if command == "left" or command == "right" or command == "up" or command == "down":
            matrix[row][column] = "*"
            row = r
            column = c


matrix_size = int(input())
commands = input().split()
matrix=[[x for x in input().split()] for x in range(matrix_size)]

movement = {"up": [-1, 0], "down": [+1, 0], "left": [0, -1], "right": [0, +1]}
row,column = 0,0
coals_count = 0
coals_counter = 0


for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == "s":
            row,column = x,y
        if matrix[x][y] == "c":
            coals_count += 1


for command in commands:
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

coals_left = 0
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[row][column] == "c":
            coals_left += 1
print(f"{coals_left} pieces of coal left. {(row,column)}")

