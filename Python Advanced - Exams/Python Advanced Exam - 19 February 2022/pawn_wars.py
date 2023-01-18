def check_if_can_capture(coordinates_attacker, coordinates_defender):
    row_a = coordinates_attacker[0]
    col_a = coordinates_attacker[1]
    row_d = coordinates_defender[0]
    col_d = coordinates_defender[1]
    if row_a - 1 >= 0 and col_a - 1 >= 0:
        if row_a - 1 == row_d and col_a - 1 == col_d:
            return [row_a - 1, col_a - 1]
    if row_a - 1 >= 0 and col_a + 1 < 8:
        if row_a - 1 == row_d and col_a + 1 == col_d:
            return [row_a - 1, col_a + 1]
    if row_a + 1 < 8 and col - 1 >= 0:
        if row_a + 1 == row_d and col_a - 1 == col_d:
            return [row_a + 1, col_a - 1]
    if row_a + 1 < 8 and col + 1 < 8:
        if row_a + 1 == row_d and col_a + 1 == col_d:
            return [row_a + 1, col_a + 1]


matrix = []
for _ in range(8):
    matrix.append(input().split())

white_pawn_coordinates = []
black_pawn_coordinates = []

position_row = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}
positions_col = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

for row in range(8):
    for col in range(8):
        if matrix[row][col] == "w":
            white_pawn_coordinates = [row, col]
        if matrix[row][col] == "b":
            black_pawn_coordinates = [row, col]

for _ in range(8):
    capture_on = check_if_can_capture(white_pawn_coordinates, black_pawn_coordinates)
    if capture_on:
        position = positions_col[capture_on[1]] + position_row[capture_on[0]]
        print(f"Game over! White win, capture on {position}.")
        break

    white_pawn_coordinates[0] -= 1

    if white_pawn_coordinates[0] == 0:
        position = positions_col[white_pawn_coordinates[1]] + position_row[white_pawn_coordinates[0]]
        print(f"Game over! White pawn is promoted to a queen at {position}.")
        break

    capture_on = check_if_can_capture(black_pawn_coordinates, white_pawn_coordinates)
    if capture_on:
        position = positions_col[capture_on[1]] + position_row[capture_on[0]]
        print(f"Game over! Black win, capture on {position}.")
        break

    black_pawn_coordinates[0] += 1

    if black_pawn_coordinates[0] == 7:
        position = positions_col[black_pawn_coordinates[1]] + position_row[black_pawn_coordinates[0]]
        print(f"Game over! Black pawn is promoted to a queen at {position}.")
        break

# def movement(current_location):
#     global white_location_r,white_location_c,winner,current_winner,black_location_r
#     if white_turn:
#         current_location -= 1
#         matrix[white_location_r][white_location_c] = "-"
#         matrix[current_location][white_location_c] = "w"
#         white_location_r = current_location
#     elif black_turn:
#         current_location += 1
#         matrix[white_location_r][white_location_c] = "-"
#         matrix[current_location][white_location_c] = "w"
#         black_location_r = current_location
#     if white_location_r == 0:
#         winner = True
#         current_winner = "White"
#     elif black_location_r == 7:
#         winner = True
#         current_winner = "Black"
#
#
# def check_diagonals():
#     global white_location_r,white_location_c,black_location_r,black_location_c
#     found = False
#     if white_turn:
#         current_r = white_location_r
#         current_c = white_location_c
#         x = black_location_r
#         y = black_location_c
#         if current_r + 1 == x and current_c + 1 == y:
#             print(f"Game over! White win, capture on {table[x][y]}.")
#             found = True
#         elif current_r - 1 == x and current_c - 1 == y:
#             print(f"Game over! White win, capture on {table[x][y]}.")
#             found = True
#         elif current_r - 1 == x and current_c + 1 == y:
#             print(f"Game over! White win, capture on {table[x][y]}.")
#             found = True
#         elif current_r + 1 == x and current_c - 1 == y:
#             print(f"Game over! White win, capture on {table[x][y]}.")
#             found = True
#     elif black_turn:
#         current_r = black_location_r
#         current_c = black_location_c
#         x = white_location_r
#         y = white_location_c
#         if current_r + 1 == x and current_c + 1 == y:
#             print(f"Game over! White win, capture on {table[x][y]}.")
#             found = True
#         elif current_r - 1 == x and current_c - 1 == y:
#             print(f"Game over! White win, capture on {table[x][y]}.")
#             found = True
#         elif current_r - 1 == x and current_c + 1 == y:
#             print(f"Game over! White win, capture on {table[x][y]}.")
#             found = True
#         elif current_r + 1 == x and current_c - 1 == y:
#             print(f"Game over! White win, capture on {table[x][y]}.")
#             found = True
#     if found:
#         exit()
#
#
# matrix_size = 8
# matrix = [[x for x in input().split()] for _ in range(matrix_size)]
# table = []
#
# for x in range(matrix_size,0,-1):
#     current_list = []
#     for y in range(97,105):
#         item = chr(y) + str(x)
#         current_list.append(item)
#     table.append(current_list)
#
# white_location_r = 0
# white_location_c = 0
# black_location_r = 0
# black_location_c = 0
#
# white_turn = False
# black_turn = False
#
# current_winner = ""
# winner = False
#
# for x in range(len(matrix)):
#     for y in range(len(matrix)):
#         if matrix[x][y] == "w":
#             white_location_r = x
#             white_location_c = y
#         elif matrix[x][y] == "b":
#             black_location_r = x
#             black_location_c = y
#
# while not winner:
#     if not white_turn and not black_turn:
#         white_turn = True
#         check_diagonals()
#         movement(white_location_r)
#     elif white_turn:
#         white_turn = False
#         black_turn = True
#         check_diagonals()
#         movement(black_location_r)
#
#     elif black_turn:
#         white_turn = True
#         black_turn = False
#         check_diagonals()
#         movement(white_location_r)
#
#
# if winner:
#     if current_winner == "White":
#         x = white_location_r
#         y = white_location_c
#         print(f"Game over! {current_winner} pawn is promoted to a queen at {table[x][y]}.")
#     elif current_winner == "White":
#         x = black_location_r
#         y = black_location_c
#         print(f"Game over! {current_winner} pawn is promoted to a queen at {table[x][y]}.")
