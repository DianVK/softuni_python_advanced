def racing(r, c):
    global row, column,teleport
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        current_matrix = matrix
        current_element = matrix[r][c]
        if current_element == "F":
            matrix[row][column] = "."
            matrix[r][c] = "C"
            print(f"Racing car {racing_number} finished the stage!")
            print(*matrix, sep="\n")
            exit()
        elif current_element == "T":
            if r == tunel_entrance[0] and c == tunel_entrance[1]:
                matrix[row][column] = "."
                row = tunel_exit[0]
                column = tunel_exit[1]
                matrix[r][c] = "."
                matrix[row][column] = "."
                teleport = True

        if teleport:
            teleport = False
            entrance_first_index = tunel_entrance[0]
            entrance_second_index = tunel_entrance[1]
            exit_first_index = tunel_exit[0]
            exit_second_index = tunel_exit[1]
            matrix[entrance_first_index][entrance_second_index] = "."
            matrix[exit_first_index][exit_second_index] = "."

        else:
            if command == "left" or command == "right" or command == "up" or command == "down":
                matrix[row][column] = "."
                row = r
                column = c
                matrix[row][column] = "C"


matrix_size = int(input())
racing_number = input()
matrix = [[x for x in input().split()] for _ in range(matrix_size)]

row, column = 0, 0
passed_km = 0
tunel_entrance = (0, 0)
tunel_exit = (0, 0)
teleport = False

for www in range(len(matrix)):
    for xxx in range(len(matrix)):
        current_el = matrix[www][xxx]
        if current_el == "T":
            if tunel_entrance == (0, 0):
                tunel_entrance = (www, xxx)
            else:
                tunel_exit = (www, xxx)

movement = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
command = input()

while command != "End":
    left_row = int(row)
    left_column = int(column)
    if command == "left":
        left_row += movement['left'][0]
        left_column += movement['left'][1]
        racing(left_row,left_column)
    elif command == "right":
        left_row += movement['right'][0]
        left_column += movement['right'][1]
        racing(left_row,left_column)
    elif command == "up":
        left_row += movement['up'][0]
        left_column += movement['up'][1]
        racing(left_row,left_column)
    elif command == "down":
        left_row += movement['down'][0]
        left_column += movement['down'][1]
        racing(left_row,left_column)
    command = input()

print(f"Racing car {racing_number} DNF.")
print(*matrix, sep="\n")