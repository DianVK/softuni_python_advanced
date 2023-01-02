size_of_battlefield = int(input())
matrix = [[x for x in input()]for _ in range(size_of_battlefield)]
start_pos = []

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == "S":
            start_pos = x,y

movement = {"up": [-1, 0], "down": [+1, 0], "left": [0, -1], "right": [0, +1]}


