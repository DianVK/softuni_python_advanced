def check_location(row,col):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        location_symbol = matrix[row][col]
        print(location_symbol)


matrix_size = int(input())
commands = input().split()
matrix=[[x for x in input().split()] for x in range(matrix_size)]

movement = {"up": [0, -1], "down": [0, 1], "left": [-1, 0], "right": [1, 0]}
row,column = 0,0
coals_count = 0
end_reached = False

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == "s":
            row,column = x,y
        if matrix[x][y] == "c":
            coals_count += 1

while not end_reached:
    for command in commands:
        if command == "left":
            left_row = int(row)
            left_column = int(column)
            left_row += movement['left'][0]
            left_column += movement['left'][1]
            check_location(left_row,left_column)
        if command == "right":
            left_row = int(row)
            left_column = int(column)
            left_row += movement['right'][0]
            left_column += movement['right'][1]
            check_location(row,column)
        if command == "up":
            left_row = int(row)
            left_column = int(column)
            left_row += movement['up'][0]
            left_column += movement['up'][1]
            check_location(row,column)
        if command == "down":
            left_row = int(row)
            left_column = int(column)
            left_row += movement['down'][0]
            left_column += movement['down'][1]
            check_location(row,column)
    print()
