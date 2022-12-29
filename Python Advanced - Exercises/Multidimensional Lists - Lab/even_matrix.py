rows = int(input())
matrix = []
for i in range(rows):

    number = [int(x) for x in input().split(", ")]
    even_numbers = [int(x) for x in number if x % 2 == 0]
    matrix.append(even_numbers)

print(matrix)