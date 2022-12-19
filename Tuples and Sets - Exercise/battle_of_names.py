number_lines = int(input())
odd_numbers = set()
even_numbers = set()

for row in range(1, number_lines +1):
    sum_chars = 0
    name = input()
    for char in name:
        sum_chars += ord(char)
    divide = int(sum_chars / row)
    if divide % 2 == 0:
        even_numbers.add(divide)
    else:
        odd_numbers.add(divide)

if sum(odd_numbers) < sum(even_numbers):
    print(*even_numbers.symmetric_difference(odd_numbers), sep=", ")
elif sum(odd_numbers) > sum(even_numbers):
    print(*odd_numbers.difference(even_numbers), sep=", ")
else:
    print(*odd_numbers.union(even_numbers), sep=", ")