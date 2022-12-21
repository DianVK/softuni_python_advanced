rows = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
diagonals = {
    'primary sum': [],
    'secondary sum': []
}
primary_diagonal = []
secondary_diagonal = []
sum_primary = 0
sum_secondary = 0

for i in range(rows):
    diagonals['primary sum'].append(matrix[i][i])
    diagonals['secondary sum'].append(matrix[i][rows - 1])
    break

print(f"Primary diagonal: {', '.join(str(x) for x in diagonals['primary sum'])}. Sum: {sum(diagonals['primary sum'])}")
print(f"Secondary diagonal: {', '.join(map(str, diagonals['secondary sum']))}. Sum: {sum(diagonals['secondary sum'])}")