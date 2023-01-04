def check_location(r,c):
    global decorations_count,gifts_count,cookies_count,r_pos,c_pos,decorations_counter,gifts_counter,cookies_counter,collected
    if r == -1:
        r = rows - 1
    elif c == -1:
        c = columns - 1
    if r >= rows:
        r = 0
    elif c >= columns:
        c = 0

    if 0 <= r < rows and 0 <= c < columns:
        location_symbol = matrix[r][c]
        if location_symbol == "D":
            decorations_counter += 1
        elif location_symbol == "G":
            gifts_counter += 1
        elif location_symbol == "C":
            cookies_counter += 1
        if direction == "left" or direction == "right" or direction == "up" or direction == "down":
            matrix[r_pos][c_pos] = "x"
            r_pos = r
            c_pos = c
            matrix[r_pos][c_pos] = "Y"
        if decorations_count == decorations_counter and gifts_count == gifts_counter and cookies_count == cookies_counter:
            print("Merry Christmas!")
            collected = True
            return
        # now_matrix = matrix
        # print(*now_matrix,sep="\n")
        # print("**************")


rows,columns = [int(x) for x in input().split(", ")]
matrix = [[x for x in input().split()] for x in range(rows)]

r_pos,c_pos = 0,0
decorations_count = 0
gifts_count = 0
cookies_count = 0
decorations_counter = 0
gifts_counter = 0
cookies_counter = 0
collected = False


for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == "Y":
            r_pos,c_pos = x,y
        if matrix[x][y] == "D":
            decorations_count += 1
        elif matrix[x][y] == "G":
            gifts_count += 1
        elif matrix[x][y] == "C":
            cookies_count += 1

movement = {"up": [-1, 0], "down": [+1, 0], "left": [0, -1], "right": [0, +1]}

command = input()
while command != "End" or not collected:
    command = command.split("-")
    direction,step = command[0],int(command[1])
    for j in range(step):
        now_row = int(r_pos)
        now_col = int(c_pos)
        if direction == "left":
            now_row += movement['left'][0]
            now_col += movement['left'][1]
            check_location(now_row, now_col)
        elif direction == "right":
            now_row += movement['right'][0]
            now_col += movement['right'][1]
            check_location(now_row, now_col)
        elif direction == "up":
            now_row += movement['up'][0]
            now_col += movement['up'][1]
            check_location(now_row, now_col)
        elif direction == "down":
            now_row += movement['down'][0]
            now_col += movement['down'][1]
            check_location(now_row, now_col)
        if collected:
            break
    if collected:
        break
    command = input()
    if command == "End":
        break

print("You've collected:")
print(f"- {decorations_counter} Christmas decorations")
print(f"- {gifts_counter} Gifts")
print(f"- {cookies_counter} Cookies")
for x in matrix:
    print(*x,sep=" ")