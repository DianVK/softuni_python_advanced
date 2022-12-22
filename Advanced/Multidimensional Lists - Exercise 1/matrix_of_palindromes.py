rows, cols = [int(x) for x in input().split()]

for row in range(97, 97 + rows):
    for col in range(97, 97 + cols):
        print(f"{chr(row)}{chr((row + col) - 97)}{chr(row)}", end=" ")
    print()

# rows,columns = [int(x) for x in input().split()]
# matrix = []
# for letter in range(97,122 + 1):
#     current_letter = chr(letter)
#     for i in range(rows):
#         for j in range(letter + i,columns + letter):
#             letter_1 = chr(letter + i)
#             letter_2 = chr(j)
#             letter_3 = chr(letter + i)
#             matrix.append([letter_1 + letter_2 + letter_3])