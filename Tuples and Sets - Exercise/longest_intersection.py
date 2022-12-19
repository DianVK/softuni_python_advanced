import sys

lines = int(input())
max_intersection = -sys.maxsize
combined_intersection = set()
set_a = set()
set_b = set()

for i in range(lines):
    data = input().split("-")
    range_1 = [int(i) for i in data[0].split(",")]
    range_2 = [int(i) for i in data[1].split(",")]
    for i in range(range_1[0], range_1[1] + 1):
        set_a.add(i)
    for j in range(range_2[0], range_2[1] + 1):
        set_b.add(j)
    intersection = set_a.intersection(set_b)
    if len(intersection) > max_intersection:
        max_intersection = len(intersection)
        combined_intersection = intersection
    set_a.clear()
    set_b.clear()

combined_intersection = list(combined_intersection)
print(f"Longest intersection is {combined_intersection} with length {max_intersection}")