rows, columns = [int(x) for x in input().split()]
matrix = []
pairs_found = 0
for _ in range(rows):
    matrix.append(input().split())

for i in range(rows - 1):
    for j in range(columns - 1):
        check_first_letter = matrix[i][j]
        check_second_letter = matrix[i][j + 1]
        check_third_letter = matrix[i + 1][j]
        check_forth_letter = matrix[i + 1][j + 1]
        if check_first_letter == check_second_letter and \
                check_second_letter == check_third_letter and \
                check_third_letter == check_forth_letter:
            pairs_found += 1

print(pairs_found)