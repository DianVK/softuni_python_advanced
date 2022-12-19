numbers = (float(x) for x in input().split())
all_numbers_counts = {}
for number in numbers:
    if number not in all_numbers_counts:
        all_numbers_counts[number] = 1
    else:
        all_numbers_counts[number] += 1

for key,value in all_numbers_counts.items():
    print(f"{key} - {value} times")