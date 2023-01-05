def check_location(r,c):
    global matrix_size,matrix,current_player,first_player_score,second_player_score,first_player_counter,second_player_counter
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        current_symbol = matrix[r][c]
        if current_symbol.isnumeric():
            if first_player_turn:
                first_player_score -= int(current_symbol)
            elif second_player_turn:
                second_player_score -= int(current_symbol)
        elif current_symbol == "B":
            if first_player_turn:
                print(f"{first_name} won the game with {first_player_counter} throws!")
                exit()
            elif second_player_turn:
                print(f"{second_name} won the game with {second_player_counter} throws!")
                exit()
        elif current_symbol == "D":
            current_sum = 0
            for o in range(matrix_size):
                for u in range(matrix_size):
                    current_el = matrix[o][u]
                    if u == c and current_el.isdigit():
                        current_sum += int(matrix[o][u])
                    if o == r and current_el.isdigit():
                        current_sum += int(matrix[o][u])
            if first_player_turn:
                first_player_score -= current_sum * 2
            elif second_player_turn:
                second_player_score -= current_sum * 2
        elif current_symbol == "T":
            current_sum = 0
            for o in range(matrix_size):
                for u in range(matrix_size):
                    current_el = matrix[o][u]
                    if u == c and current_el.isdigit():
                        current_sum += int(matrix[o][u])
                    if o == r and current_el.isdigit():
                        current_sum += int(matrix[o][u])
            if first_player_turn:
                first_player_score -= current_sum * 3
            elif second_player_turn:
                second_player_score -= current_sum * 3


first_name, second_name = input().split(", ")
matrix_size = 7
matrix = [[x for x in input().split()] for _ in range(matrix_size)]

first_player_score = 501
second_player_score = 501
first_player_turn = False
second_player_turn = False
first_player_counter = 0
second_player_counter = 0


while first_player_score > 0 and second_player_score > 0:
    location = input()
    row = int(location[1])
    column = int(location[4])
    if not first_player_turn and not second_player_turn:
        first_player_turn = True
        first_player_counter += 1
        current_player = first_player_score
        check_location(row, column)
    elif first_player_turn:
        first_player_turn = False
        second_player_turn = True
        current_player = second_player_score
        second_player_counter += 1
        check_location(row, column)
    elif second_player_turn:
        first_player_turn = True
        second_player_turn = False
        first_player_counter += 1
        current_player = first_player_score
        check_location(row, column)

if first_player_score <= 0:
    print(f"{first_name} won the game with {first_player_counter} throws!")
elif second_player_score <= 0:
    print(f"{second_name} won the game with {second_player_counter} throws!")