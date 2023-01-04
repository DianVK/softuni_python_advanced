def check_coordinates(r,c):
    global total_sum
    current_sum = 0
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        if matrix[r][c] == "B":
            matrix[r][c] = "X"
            for o in range(matrix_size):
                for u in range(matrix_size):
                    current_el = matrix[o][u]
                    if u == c and current_el.isdigit():
                        current_sum += int(matrix[o][u])

    total_sum += current_sum
    check_prizes(total_sum)


def check_prizes(total_sum):
    global prize
    if 100 <= total_sum < 200:
        prize = "Football"
    elif 200 <= total_sum < 300:
        prize = "Teddy Bear"
    elif 300 <= total_sum:
        prize = "Lego Construction Set"


matrix_size = 6
matrix = [[j for j in input().split()] for _ in range(matrix_size)]
total_sum = 0
prize = ""

for _ in range(3):
    coordinates = input().split(", ")
    x = coordinates[0]
    x = int(x[1])
    y = coordinates[1]
    y = int(y[0])
    check_coordinates(x,y)

if prize != "":
    print(f"Good job! You scored {total_sum} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - total_sum} points more to win a prize.")