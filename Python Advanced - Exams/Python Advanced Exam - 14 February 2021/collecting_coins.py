from math import floor


def check_location(r, c):
    global coins, hit_wall, direction, rows, columns, result
    if r == -1:
        r = matrix_size - 1
    elif c == -1:
        c = matrix_size - 1
    if r >= matrix_size:
        r = 0
    elif c >= matrix_size:
        c = 0
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        current_el = matrix[r][c]
        if current_el.isdigit():
            coins += int(current_el)
        elif current_el == "X":
            hit_wall = True
            result += f"[{rows}, {columns}]\n"
            result += f"[{r}, {c}]"
            return
    if direction == "left" or direction == "right" or direction == "up" or direction == "down":
        matrix[rows][columns] = "C"

        result += f"[{rows}, {columns}]\n"
        rows = r
        columns = c
        matrix[rows][columns] = "N"


matrix_size = int(input())
matrix = [[j for j in input().split()] for _ in range(matrix_size)]
movement = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

hit_wall = False
rows, columns = 0, 0
coins = 0
result = ""

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == "P":
            rows = x
            columns = y

while not hit_wall and coins < 100:
    direction = input()
    now_row = int(rows)
    now_col = int(columns)
    if direction == "left":
        now_row += movement['left'][0]
        now_col += movement['left'][1]
        check_location(now_row, now_col)
    elif direction == "right":
        now_row += movement['right'][0]
        now_col += movement['right'][1]
        check_location(now_row, now_col)
    elif direction == "up":
        now_row += movement['up'][0]
        now_col += movement['up'][1]
        check_location(now_row, now_col)
    elif direction == "down":
        now_row += movement['down'][0]
        now_col += movement['down'][1]
        check_location(now_row, now_col)

if hit_wall:
    coins = floor(coins / 2)
    print(f"Game over! You've collected {coins} coins.")
if coins >= 100:
    result += f"[{rows}, {columns}]\n"
    print(f"You won! You've collected {coins} coins.")
print(f"Your path:\n{result.strip()}")
