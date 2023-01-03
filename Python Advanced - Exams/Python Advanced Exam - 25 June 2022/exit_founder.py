def check_location(r,c):
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        current_symbol = matrix[r][c]
        return True


first_name, second_name = input().split(", ")
matrix_size = 6
matrix = [[x for x in input().split()] for _ in range(matrix_size)]
exit_found = False

first_location = (0,0)
second_location = (0,0)

first = False
second = False
while not exit_found:
    location = input()
    row = location[0]
    column = location[1]
    if not first and not second:
        first = True
        check_location(row,column)


