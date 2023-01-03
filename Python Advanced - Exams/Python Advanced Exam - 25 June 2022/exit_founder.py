def check_location(r, c):
    global exit_found, winner, wall, player_on_wall

    if player_on_wall != "" and player_on_wall == current_player:
        player_on_wall = "free"
        return

    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        current_symbol = matrix[r][c]

        if current_symbol == "E":
            exit_found = True
            print(f"{current_player} found the Exit and wins the game!")
            return

        elif current_symbol == "T":
            if current_player == first_name:
                winner = second_name
            elif current_player == second_name:
                winner = first_name
            exit_found = True
            print(f"{current_player} is out of the game! The winner is {winner}.")
            return

        elif current_symbol == "W":
            wall = True
            print(f"{current_player} hits a wall and needs to rest.")
            player_on_wall = current_player
            return


first_name, second_name = input().split(", ")
matrix_size = 6
matrix = [[x for x in input().split()] for _ in range(matrix_size)]
exit_found = False

first = False
second = False
wall = False
player_on_wall = ""
current_player = ""

while not exit_found:
    location = input()
    row = int(location[1])
    column = int(location[4])
    if not first and not second:
        first = True
        current_player = first_name
        check_location(row, column)
    elif first:
        first = False
        second = True
        current_player = second_name
        check_location(row, column)
    elif second:
        first = True
        second = False
        current_player = first_name
        check_location(row, column)