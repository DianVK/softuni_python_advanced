rows = int(input())
matrix = [[int(x) if x[-1].isdigit() else x for x in input().split()] for _ in range(rows)]

cols, result, directions = len(matrix[0]), {}, {
    "up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]
}


def find_starting_position():
    for row in range(rows):
        if "B" in matrix[row]:
            return row, matrix[row].index("B")


def check_valid_index(row, col):
    if 0 <= row < rows and 0 <= col < cols and matrix[row][col] != "X":
        return True


bunny_row, bunny_col = find_starting_position()


def movement():
    for direction, (row, col) in directions.items():
        bunny_move_row, bunny_move_col = bunny_row + row, bunny_col + col
        for jump in range(cols):
            if check_valid_index(bunny_move_row, bunny_move_col):
                result[direction] = result.get(direction, 0) + matrix[bunny_move_row][bunny_move_col]
                bunny_move_row, bunny_move_col = row + bunny_move_row, col + bunny_move_col
            else:
                break


movement()
if sum(result.values()) != 0:
    max_direction = max(result, key=result.get)
    print(max_direction)
    for path in range(cols):
        print_row, print_col = bunny_row + directions[max_direction][0], bunny_col + directions[max_direction][1]
        if check_valid_index(print_row, print_col):
            print(f"[{print_row}, {print_col}]")
            bunny_row, bunny_col = print_row, print_col
        else:
            break
    print(result[max_direction])

# rows = int(input())
# matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(rows)]
# movement = {
#     "UP": [-1, 0], "DOWN": [1, 0], "LEFT": [0, -1], "RIGHT": [0, 1]
# }
# best_sum = 0
# best_way = ""
#
# def check_valid_index(row, col):
#     if 0 <= row < rows and 0 <= col < rows:
#         return True
#
#
# def check_left_sum(row, col):
#     global best_sum
#     global best_way
#     right_sum = 0
#     row += movement['LEFT'][0]
#     col += movement['LEFT'][1]
#     current_item = matrix[row][col]
#     if not check_valid_index(row, col):
#         return
#     if current_item == "X":
#         return
#     for x in range(row, rows):
#         for m in range(col, rows):
#             egg_value = matrix[x][m]
#             if egg_value == "X":
#                 return
#             right_sum += egg_value
#
#             if right_sum > best_sum:
#                 best_sum = right_sum
#                 best_way = "left"
#             row += movement['LEFT'][0]
#             col += movement['LEFT'][1]
#             if not check_valid_index(row, col):
#                 return
#
#
#
# def check_right_sum(row, col):
#     global best_sum
#     global best_way
#     right_sum = 0
#     row += movement['RIGHT'][0]
#     col += movement['RIGHT'][1]
#     current_item = matrix[row][col]
#     if not check_valid_index(row, col):
#         return
#     if current_item == "X":
#         return
#     for x in range(row, rows):
#         for m in range(col, rows):
#             egg_value = matrix[x][m]
#             if egg_value == "X":
#                 return
#             right_sum += egg_value
#             if right_sum > best_sum:
#                 best_sum = right_sum
#                 best_way = "right"
#             row += movement['RIGHT'][0]
#             col += movement['RIGHT'][1]
#             if not check_valid_index(row, col):
#                 return
#
#
#
# def check_up_sum(row, col):
#     global best_sum
#     global best_way
#     right_sum = 0
#     row += movement['UP'][0]
#     col += movement['UP'][1]
#     current_item = matrix[row][col]
#     if not check_valid_index(row, col):
#         return
#     if current_item == "X":
#         return
#     for x in range(row, rows):
#         for m in range(col, rows):
#             egg_value = matrix[x][m]
#             if egg_value == "X":
#                 return
#             right_sum += egg_value
#             if right_sum > best_sum:
#                 best_sum = right_sum
#                 best_way = "up"
#             row += movement['UP'][0]
#             col += movement['UP'][1]
#             if not check_valid_index(row, col):
#                 return
#
#
# def check_down_sum(row, col):
#     global best_sum
#     global best_way
#     right_sum = 0
#     row += movement['DOWN'][0]
#     col += movement['DOWN'][1]
#     current_item = matrix[row][col]
#     if not check_valid_index(row, col):
#         return
#     if current_item == "X":
#         return
#     for x in range(row, rows):
#         for m in range(col, rows):
#             egg_value = matrix[x][m]
#             if egg_value == "X":
#                 return
#             right_sum += egg_value
#             if right_sum > best_sum:
#                 best_sum = right_sum
#                 best_way = "down"
#             row += movement['DOWN'][0]
#             col += movement['DOWN'][1]
#             if not check_valid_index(row, col):
#                 return
#
# position = []
# for row in range(rows):
#     for col in range(rows):
#         if matrix[row][col] == "B":
#             position.append(row)
#             position.append(col)
#             break
#     if position:
#         break
#
#
# if check_valid_index(position[0],position[1]):
#     check_left_sum(position[0],position[1])
#     check_right_sum(position[0],position[1])
#     check_up_sum(position[0],position[1])
#     check_down_sum(position[0],position[1])
#
# if best_way == "left":
#     print(best_way)
#     for r in range(position[0],rows):
#         for c in range(position[1] +1,rows):
#             if matrix[r][c] == "X":
#                 break
#             print(f"{[r, c]}")
#         break
#     print(best_sum)
# if best_way == "right":
#     print(best_way)
#     for r in range(position[0],rows):
#         for c in range(position[1] +1,rows):
#             if matrix[r][c] == "X":
#                 break
#             print(f"{[r, c]}")
#         break
#     print(best_sum)
#
#
# if best_way == "up":
#     print(best_way)
#     for r in range(position[0],rows):
#         for c in range(position[1] +1,rows):
#             if matrix[r][c] == "X":
#                 break
#             print(f"{[r, c]}")
#         break
#     print(best_sum)
# if best_way == "down":
#     print(best_way)
#     for r in range(position[0],rows):
#         for c in range(position[1] +1,rows):
#             if matrix[r][c] == "X":
#                 break
#             print(f"{[r, c]}")
#         break
#     print(best_sum)