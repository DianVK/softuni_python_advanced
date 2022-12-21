row,column = [int(x) for x in input().split(", ")]
matrix = []
total_sum = 0
for i in range(row):
    text = [int(x) for x in input().split(", ")]
    matrix.append(text)
for s in matrix:
    total_sum += sum(s)
print(total_sum)
print(matrix)