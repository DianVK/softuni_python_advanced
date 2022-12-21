rows,columns = [int(x) for x in input().split(", ")]
matrix = []
biggest_sum = 0
biggest_one_one = 0
biggest_one_two = 0
biggest_two_one = 0
biggest_two_two = 0

for x in range(rows):
    items = [int(x) for x in input().split(", ")]
    matrix.append(items)

for i in range(rows - 1):
    for j in range(columns - 1):
        if i + 1 > rows or j + 1 > columns:
            break
        else:
            one_one = matrix[i][j]
            one_two = matrix[i][j + 1]
            two_one = matrix[i + 1][j]
            two_two = matrix[i + 1][j + 1]
        check_sum = one_one + one_two + two_one + two_two
        if check_sum > biggest_sum:
            biggest_sum = check_sum
            biggest_one_one = one_one
            biggest_one_two = one_two
            biggest_two_one = two_one
            biggest_two_two = two_two

print(f"{biggest_one_one} {biggest_one_two}\n{biggest_two_one} {biggest_two_two}\n{biggest_sum}")