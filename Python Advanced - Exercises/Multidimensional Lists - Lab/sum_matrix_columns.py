rows,columns = [int(x) for x in input().split(", ")]
matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

current_row_sum = 0
for j in range(columns):
    for i in range(rows):
        current_row_sum += matrix[i][j]
    print(current_row_sum)
    current_row_sum = 0