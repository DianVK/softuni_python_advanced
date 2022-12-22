def check_valid_index(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True


def explode(row, col, bomb_damage):
    if matrix[row][col] > 0:
        matrix[row][col] -= bomb_damage


rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]
bombs_coordinates = [int(x) for x in input().replace(" ", ",").split(",")]
cols, alive_cells = len(matrix[0]), []

movement_explosion = {
    "up": [0, -1], "down": [0, 1], "left": [-1, 0], "right": [1, 0],
    "top left diagonal": [-1, -1], "bottom left diagonal": [-1, 1],
    "top right diagonal": [1, -1], "bottom right diagonal": [1, 1]}


for i in range(0, len(bombs_coordinates), 2):
    row, col = bombs_coordinates[i], bombs_coordinates[i + 1]
    if matrix[row][col] > 0:
        bomb_damage, matrix[row][col] = matrix[row][col], 0
        for ind in movement_explosion:
            row_movement, col_movement = movement_explosion[ind]
            if check_valid_index(row + row_movement, col + col_movement):
                explode(row + row_movement, col + col_movement, bomb_damage)

for row in range(len(matrix)):
    for num in matrix[row]:
        if num > 0:
            alive_cells.append(num)

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
for row in range(len(matrix)):
    print(*matrix[row], sep=" ")