rows = int(input())
matrix = []
diagonal_sum = 0
for i in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)
for j in range(len(matrix)):
    diagonal_sum += matrix[j][j]

print(diagonal_sum)

