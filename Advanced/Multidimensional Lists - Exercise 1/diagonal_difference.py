matrix_size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(matrix_size)]

compare_diagonals = {
    'primary_diagonal': [],
    'secondary_diagonal': []
}

for i in range(matrix_size):
    compare_diagonals['primary_diagonal'].append(matrix[i][i])
    compare_diagonals['secondary_diagonal'].append(matrix[i][matrix_size - i - 1])

print(f"{abs(sum(compare_diagonals['primary_diagonal']) - sum(compare_diagonals['secondary_diagonal']))}")
