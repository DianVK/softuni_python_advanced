from collections import deque


def check_location(r,c):
    global water,metal,concrete,row,column
    valid = False
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        valid = True
    if current_direction == "left" and not valid:
        c = 5
    elif current_direction == "right" and not valid:
        c = 1
    elif current_direction == "up" and not valid:
        r = 5
    elif current_direction == "down" and not valid:
        r = 1
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        valid = True

    if valid:
        current_item = matrix[r][c]
        if current_item == "W":
            print(f"Water deposit found at ({r}, {c})")
            water = True
        elif current_item == "M":
            print(f"Metal deposit found at ({r}, {c})")
            metal = True
        elif current_item == "C":
            print(f"Concrete deposit found at ({r}, {c})")
            concrete = True
        elif current_item == "R":
            print(f"Rover got broken at ({r}, {c})")

        if current_direction == "left" or current_direction == "right" or current_direction == "up" or current_direction == "down":
            matrix[row][column] = "."
            row = r
            column = c
            matrix[row][column] = "X"


matrix_size = 6
matrix = [[x for x in input().split()] for _ in range(matrix_size)]

movement = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
water,metal,concrete = False,False,False

row,column = 0,0
for x in range(len(matrix)):
    for y in range(len(matrix)):
        if matrix[x][y] == "E":
            row = x
            column = y
            break

command = deque(input().split(", "))
while command:
    current_direction = command.popleft()
    now_row = int(row)
    now_col = int(column)
    if current_direction == "left":
        now_row += movement['left'][0]
        now_col += movement['left'][1]
        check_location(now_row,now_col)
    elif current_direction == "right":
        now_row += movement['right'][0]
        now_col += movement['right'][1]
        check_location(now_row,now_col)
    elif current_direction == "up":
        now_row += movement['up'][0]
        now_col += movement['up'][1]
        check_location(now_row,now_col)
    elif current_direction == "down":
        now_row += movement['down'][0]
        now_col += movement['down'][1]
        check_location(now_row,now_col)

if water and metal and concrete :
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")