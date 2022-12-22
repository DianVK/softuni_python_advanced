rows, colons = [int(x) for x in input().split()]

matrix_list = [[int(x) for x in input().split()] for row in range(rows)]
max_sum = {"max number": -181,
           "row": 0,
           "col": 0}


def check_valid_index(row, col):
    if 0 <= row + 3 <= rows and 0 <= col + 3 <= colons:
        return True


def sum_rectangle(row, col):
    if check_valid_index(row, col):
        sum_total = 0
        for row_check in range(row, row + 3):
            sum_total += sum(matrix_list[row_check][col: col + 3])
        if max_sum["max number"] < sum_total:
            max_sum["max number"] = sum_total
            max_sum["row"] = row
            max_sum["col"] = col


for row in range(rows):
    for col in range(colons):
        sum_rectangle(row, col)

print(f"Sum = {max_sum['max number']}")
for row in range(max_sum["row"], max_sum["row"] + 3):
    print(" ".join([str(x) for x in matrix_list[row][max_sum["col"]: max_sum["col"] + 3]]))

# rows,columns = [int(x) for x in input().split()]
# matrix = [[int(x) for x in input().split()]for x in range(rows)]
#
# max_sum = 0
# max_matrix = []
#
# for i in range(rows - 2):
#     for j in range(columns - 2):
#         first_row_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2]
#         second_row_sum = matrix[i+ 1][j] + matrix[i+1][j + 1] + matrix[i+1][j + 2]
#         third_row_sum = matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
#         current_sum = first_row_sum + second_row_sum + third_row_sum
#         if current_sum > max_sum:
#             max_sum = current_sum
#             max_matrix.clear()
#             first_row_nums = [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]]
#             second_row_nums = [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]]
#             third_row_nums = [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]
#             max_matrix = [first_row_nums,second_row_nums,third_row_nums]
#
# print(f"Sum = {max_sum}")
# for el in max_matrix:
#     print(*el)