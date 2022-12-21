row,column = [int(x) for x in input().split(", ")]
matrix = []
total_sum = 0
for i in range(row):
    text = [int(x) for x in input().split(", ")]
    matrix.append(text)
# for s in matrix:
#     total_sum += sum(s)
for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        total_sum += matrix[row_index][col_index]

print(total_sum)
print(matrix)