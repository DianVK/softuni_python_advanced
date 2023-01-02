from collections import deque
seats = input().split(", ")
first_row = deque(map(int, input().split(", ")))
second_row = deque(map(int, input().split(", ")))
matches = []
rotations_count = 0

while rotations_count < 10 and len(matches) < 3:
    rotations_count += 1
    first_num = first_row.popleft()
    second_num = second_row.pop()
    current_char = chr(first_num + second_num)
    check_first_char = str(first_num)+str(current_char)
    check_second_char = str(second_num)+str(current_char)
    if check_second_char in seats:
        matches.append(check_second_char)
        seats.remove(check_second_char)
    elif check_first_char in seats:
        matches.append(check_first_char)
        seats.remove(check_first_char)
    else:
        first_row.append(first_num)
        second_row.appendleft(second_num)

print(f"Seat matches:",end=" ")
print(*matches,sep=", ")
print(f"Rotations count: {rotations_count}")