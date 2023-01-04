def check_location(r,c):
    pass

rows,columns = input().split(", ")
matrix = [[x for x in input()] for x in range(rows)]

r_pos,c_pos = 0,0
decorations_count = 0
gifts_count = 0
cookies_count = 0
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == "Y":
            row,column = x,y
        if matrix[x][y] == "D":
            decorations_count += 1
        elif matrix[x][y] == "G":
            gifts_count += 1
        elif matrix[x][y] == "C":
            cookies_count += 1

movement = {"up": [-1, 0], "down": [+1, 0], "left": [0, -1], "right": [0, +1]}

command = input()
while command != "End":
    command = command.split("-")
    direction,step = command[0],int(command[1])
    now_row = int(r_pos)
    now_col = int(c_pos)
    if command == "left":
        now_row += movement['left'][0]
        now_col += movement['left'][1]
        check_location(now_row, now_col)
    elif command == "right":
        now_row += movement['right'][0]
        now_col += movement['right'][1]
        check_location(now_row, now_col)
    elif command == "up":
        now_row += movement['up'][0]
        now_col += movement['up'][1]
        check_location(now_row, now_col)
    elif command == "down":
        now_row += movement['down'][0]
        now_col += movement['down'][1]
        check_location(now_row, now_col)